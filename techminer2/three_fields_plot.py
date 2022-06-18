"""
Three fields plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/three_fields_plot.png"
>>> three_fields_plot(
...     directory=directory,
...     left_column='authors',
...     middle_column='countries',
...     right_column='author_keywords',
...     min_occ_left=2, 
...     min_occ_middle=6,
...     min_occ_right=8,
...     figsize=(10, 10),
... ).savefig(file_name)

.. image:: images/three_fields_plot.png
    :width: 700px
    :align: center

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle

from .occurrence_matrix import occurrence_matrix


def _sankey_3fields_diagram(
    data_left,
    data_right,
    figsize=(6, 6),
):
    def compute_params(data_left, data_right):

        params = {}
        params["n_left"] = data_left.shape[0]
        params["n_middle"] = data_left.shape[1]
        params["n_right"] = data_right.shape[1]

        left_values = data_left.sum(axis=1)
        middle_values = data_left.sum(axis=0)
        right_values = data_right.sum(axis=0)

        params["space"] = max(
            left_values.sum() * 0.1 / (params["n_left"] - 1),
            middle_values.sum() * 0.1 / (params["n_middle"] - 1),
            right_values.sum() * 0.1 / (params["n_right"] - 1),
        )

        middle_heights_left = data_left.sum(axis=0)
        middle_heights_right = data_right.sum(axis=1)
        middle_heights = pd.Series(
            np.maximum(middle_heights_left, middle_heights_right),
            index=middle_heights_left.index,
        )

        params["height"] = max(
            middle_heights_left.sum() + (params["n_left"] - 1) * params["space"],
            middle_heights_right.sum() + (params["n_right"] - 1) * params["space"],
            middle_heights.sum() + (params["n_middle"] - 1) * params["space"],
        )

        return params

    def generate_curve(p0, p2, is_left=True):
        x0, y0 = p0
        x2, y2 = p2
        ys_d = np.array(50 * [y0] + 50 * [y2])
        ys_d = np.convolve(ys_d, 0.05 * np.ones(20), mode="valid")
        yb = np.convolve(ys_d, 0.05 * np.ones(20), mode="valid")
        if is_left:
            xb = np.linspace(0.02, 0.49, len(yb))
        else:
            xb = np.linspace(0.51, 0.98, len(yb))

        return xb, yb

    def plot_groups(ax, data_left, data_right, params):

        data_left = data_left.copy()
        data_right = data_right.copy()

        left_values = data_left.sum(axis=1)
        right_values = data_right.sum(axis=0)

        middle_heights_left = data_left.sum(axis=0)
        middle_heights_right = data_right.sum(axis=1)
        middle_heights = pd.Series(
            np.maximum(middle_heights_left, middle_heights_right),
            index=middle_heights_left.index,
        )

        # ----<left column >---------------------------------------
        base = 0.0
        for i_pos, value in enumerate(left_values):
            r = Rectangle(
                xy=(0, base),
                width=0.02,
                height=value,
                color="tab:blue",
            )
            ax.add_patch(r)
            #
            text = data_left.index[i_pos]
            ax.text(
                0.028,
                base + value / 2.0,
                text,
                fontsize=8,
                verticalalignment="center_baseline",
                zorder=10,
            )
            #
            base += value + params["space"]

        # ----<middle column >---------------------------------------
        base = 0.0
        for i_pos, value in enumerate(middle_heights):
            r = Rectangle(
                xy=(0.49, base),
                width=0.02,
                height=value,
                color="tab:blue",
            )
            ax.add_patch(r)
            #
            text = data_left.columns[i_pos]
            ax.text(
                0.51 + 0.008,
                base + value / 2.0,
                text,
                fontsize=8,
                verticalalignment="center_baseline",
                zorder=10,
            )
            #
            base += value + params["space"]

        # ----<right column>------------------------------------------
        base = 0.0
        for i_pos, value in enumerate(right_values):
            r = Rectangle(
                xy=(1, base),
                width=-0.02,
                height=value,
            )
            ax.add_patch(r)
            #
            text = data_right.columns[i_pos]
            ax.text(
                0.98 - 0.008,
                base + value / 2.0,
                text,
                fontsize=8,
                horizontalalignment="right",
                verticalalignment="center_baseline",
                zorder=10,
            )
            #
            base += value + params["space"]

    def plot_connections(ax, data_left, data_right, params):

        left_base = 0.0
        left_heights = data_left.sum(axis=1)
        right_heights = data_right.sum(axis=0)

        middle_heights_left = data_left.sum(axis=0)
        middle_heights_right = data_right.sum(axis=1)
        middle_heights = pd.Series(
            np.maximum(middle_heights_left, middle_heights_right),
            index=middle_heights_left.index,
        )

        middle_base = pd.Series(0.0, index=data_left.columns)
        for i_col, col in enumerate(data_left.columns):
            if i_col > 0:
                middle_base[col] = (
                    middle_base.iloc[i_col - 1]
                    + middle_heights.iloc[i_col - 1]
                    + params["space"]
                )

        max_value = max(data_left.max().max(), data_right.max().max())
        min_value = min(
            min(
                [
                    data_left.loc[index, col]
                    for index in data_left.index
                    for col in data_left.columns
                    if data_left.loc[index, col] > 0
                ],
                [
                    data_right.loc[index, col]
                    for index in data_right.index
                    for col in data_right.columns
                    if data_right.loc[index, col] > 0
                ],
            )
        )

        # ----<left side>------------------------------------------------------------
        for index in data_left.index:
            for col in data_left.columns:

                if data_left.loc[index, col] > 0:

                    p_left = (0.02, left_base)
                    p_middle = (0.49, middle_base[col])
                    lower_line = generate_curve(p_left, p_middle)
                    x = lower_line[0]
                    y0 = lower_line[1]

                    p_left = (0.02, left_base + data_left.loc[index, col])
                    p_middle = (0.49, middle_base[col] + data_left.loc[index, col])
                    upper_line = generate_curve(p_left, p_middle)
                    y1 = upper_line[1]

                    alpha = 0.10 + 0.20 * (data_left.loc[index, col] - min_value) / (
                        max_value - min_value
                    )

                    ax.fill_between(
                        x,
                        y0,
                        y1,
                        color="gray",
                        alpha=alpha,
                    )
                    left_base += data_left.loc[index, col]

            left_base += params["space"]
            middle_base += data_left.loc[index, :]

        # ----<right side>------------------------------------------------------------

        middle_base = 0.0
        right_base = pd.Series(0.0, index=data_right.columns)
        for i_col, col in enumerate(data_right.columns):
            if i_col > 0:
                right_base[col] = (
                    right_base.iloc[i_col - 1]
                    + right_heights.iloc[i_col - 1]
                    + params["space"]
                )

        for index in data_right.index:
            for col in data_right.columns:

                if data_right.loc[index, col] > 0:

                    p_middle = (0.51, middle_base)
                    p_right = (0.98, right_base[col])
                    lower_line = generate_curve(p_middle, p_right, is_left=False)
                    x = lower_line[0]
                    y0 = lower_line[1]

                    p_middle = (0.51, middle_base + data_right.loc[index, col])
                    p_right = (0.98, right_base[col] + data_right.loc[index, col])
                    upper_line = generate_curve(p_middle, p_right, is_left=False)
                    y1 = upper_line[1]

                    alpha = 0.10 + 0.20 * (data_right.loc[index, col] - min_value) / (
                        max_value - min_value
                    )

                    ax.fill_between(
                        x,
                        y0,
                        y1,
                        color="gray",
                        alpha=alpha,
                    )
                    middle_base += data_right.loc[index, col]

            middle_base += params["space"]
            right_base += data_right.loc[index, :]

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    params = compute_params(data_left, data_right)
    plot_groups(ax, data_left, data_right, params)
    plot_connections(ax, data_left, data_right, params)

    ax.set_ylim(0, params["height"])
    ax.set_axis_off()

    return fig


def three_fields_plot(
    left_column,
    middle_column,
    right_column,
    min_occ_left=1,
    max_occ_left=None,
    min_occ_middle=1,
    max_occ_middle=None,
    min_occ_right=1,
    max_occ_right=None,
    directory="./",
    figsize=(6, 6),
):
    matrix_left = occurrence_matrix(
        column=middle_column,
        by=left_column,
        min_occ=min_occ_middle,
        max_occ=max_occ_middle,
        min_occ_by=min_occ_left,
        max_occ_by=max_occ_left,
        directory=directory,
    )

    matrix_right = occurrence_matrix(
        column=right_column,
        by=middle_column,
        min_occ=min_occ_right,
        max_occ=max_occ_right,
        min_occ_by=min_occ_middle,
        max_occ_by=max_occ_middle,
        directory=directory,
    )

    matrix_left.columns = matrix_left.columns.get_level_values(0)
    matrix_right.columns = matrix_right.columns.get_level_values(0)
    matrix_left.index = matrix_left.index.get_level_values(0)
    matrix_right.index = matrix_right.index.get_level_values(0)

    for col in matrix_left.columns:
        if col not in matrix_right.index:
            matrix_right.loc[col] = 0

    for index in matrix_right.index:
        if index not in matrix_left.columns:
            matrix_left[index] = 0

    matrix_left = matrix_left.sort_index(axis=1, ascending=True)
    matrix_right = matrix_right.sort_index(axis=0, ascending=True)

    return _sankey_3fields_diagram(
        data_left=matrix_left,
        data_right=matrix_right,
        figsize=figsize,
    )
