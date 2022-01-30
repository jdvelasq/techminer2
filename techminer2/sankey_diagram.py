"""
Sankey Diagram
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/sankey_diagram.png"
>>> matrix = occurrence_matrix(column='authors', by='author_keywords', min_occ=3, min_occ_by=6, directory=directory)
>>> sankey_diagram(matrix).savefig(file_name)

.. image:: images/sankey_diagram.png
    :width: 700px
    :align: center

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle


def sankey_diagram(
    data,
    figsize=(6, 6),
):
    def compute_params(data):

        params = {}
        params["n_rows"] = data.shape[0]
        params["n_cols"] = data.shape[1]

        row_values = data.sum(axis=1)
        col_values = data.sum(axis=0)

        params["space"] = min(
            row_values.sum() * 0.1 / (params["n_rows"] - 1),
            col_values.sum() * 0.1 / (params["n_cols"] - 1),
        )

        params["height"] = max(
            row_values.sum() * 1.1,
            col_values.sum() * 1.1,
        )

        return params

    def generate_curve(p0, p2):
        x0, y0 = p0
        x2, y2 = p2

        ys_d = np.array(50 * [y0] + 50 * [y2])
        ys_d = np.convolve(ys_d, 0.05 * np.ones(20), mode="valid")
        yb = np.convolve(ys_d, 0.05 * np.ones(20), mode="valid")

        xb = np.linspace(0.05, 0.95, len(yb))
        return xb, yb

    def plot_groups(ax, data, params):

        data = data.copy()

        row_values = data.sum(axis=1)
        col_values = data.sum(axis=0)

        base = 0.0
        for i_row, row_value in enumerate(row_values):
            r = Rectangle(
                xy=(0, base),
                width=0.05,
                height=row_value,
                color="tab:blue",
            )
            ax.add_patch(r)
            #
            text = data.index[i_row]
            ax.text(
                0.058,
                base + row_value / 2.0,
                text,
                fontsize=8,
                verticalalignment="center_baseline",
                zorder=10,
            )
            #
            base += row_value + params["space"]

        base = 0.0
        for i_col, col_value in enumerate(col_values):
            r = Rectangle(
                xy=(1, base),
                width=-0.05,
                height=col_value,
            )
            ax.add_patch(r)
            #
            text = data.columns[i_col]
            ax.text(
                0.942,
                base + col_value / 2.0,
                text,
                fontsize=8,
                horizontalalignment="right",
                verticalalignment="center_baseline",
                zorder=10,
            )
            #
            base += col_value + params["space"]

    def plot_connections(ax, data, params):

        left_base = 0.0
        left_heights = data.sum(axis=1)
        right_heights = data.sum(axis=0)

        right_base = pd.Series(0.0, index=data.columns)
        for i_col, col in enumerate(data.columns):
            if i_col > 0:
                right_base[col] = (
                    right_base.iloc[i_col - 1]
                    + right_heights.iloc[i_col - 1]
                    + params["space"]
                )

        max_value = data.max().max()
        min_value = min(
            [
                data.loc[index, col]
                for index in data.index
                for col in data.columns
                if data.loc[index, col] > 0
            ]
        )

        for index in data.index:
            for col in data.columns:

                if data.loc[index, col] > 0:

                    p_left = (0.05, left_base)
                    p_right = (0.95, right_base[col])
                    lower_line = generate_curve(p_left, p_right)
                    x = lower_line[0]
                    y0 = lower_line[1]

                    p_left = (0.05, left_base + data.loc[index, col])
                    p_right = (0.95, right_base[col] + data.loc[index, col])
                    upper_line = generate_curve(p_left, p_right)
                    y1 = upper_line[1]

                    alpha = 0.10 + 0.20 * (data.loc[index, col] - min_value) / (
                        max_value - min_value
                    )

                    ax.fill_between(
                        x,
                        y0,
                        y1,
                        color="gray",
                        alpha=alpha,
                    )
                    left_base += data.loc[index, col]

            left_base += params["space"]
            right_base += data.loc[index, :]

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    params = compute_params(data)
    plot_groups(ax, data, params)
    plot_connections(ax, data, params)

    ax.set_ylim(0, params["height"])
    ax.set_axis_off()

    fig.set_tight_layout(True)

    return fig
