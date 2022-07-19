"""
Thematic evolution plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/thematic_evolution_plot.png"

>>> user_filters(directory=directory, quiet=True, first_year=2016, last_year=2018)
>>> ind_2016_2018 = thematic_map_indicators('author_keywords', min_occ=3, directory=directory)
>>> thematic_map_communities(
...     'author_keywords',
...     min_occ=3,
...     directory=directory,
... ).head()
cluster                          CL_00               CL_01
rn                                                        
0                       fintech 26:797   innovation 06:222
1        financial technologies 07:109   technology 03:156
2             financial service 06:288         bank 03:147
3                    blockchain 05:099  retail bank 03:053
4                business model 04:172                    


>>> user_filters(directory=directory, quiet=True, first_year=2019, last_year=2020)
>>> ind_2019_2020 = thematic_map_indicators('author_keywords', min_occ=3, directory=directory)
>>> thematic_map_communities(
...     'author_keywords',
...     min_occ=3,
...     directory=directory,
... ).head()
cluster                           CL_00  ...                    CL_03
rn                                       ...                         
0                        fintech 54:391  ...        blockchain 06:041
1                     innovation 06:027  ...  cryptocurrencies 04:034
2           financial innovation 05:027  ...                         
3                venture capital 03:024  ...                         
4        artificial intelligence 03:021  ...                         
<BLANKLINE>
[5 rows x 4 columns]

>>> user_filters(directory=directory, quiet=True, first_year=2021, last_year=2021)
>>> ind_2021_2021 = thematic_map_indicators('author_keywords', min_occ=3, directory=directory)
>>> thematic_map_communities(
...     'author_keywords',
...     min_occ=3,
...     directory=directory,
... ).head()
cluster                                CL_00  ...                    CL_04
rn                                            ...                         
0                              fintech 59:97  ...     perceived risk 03:01
1                  financial inclusion 10:14  ...  perceived benefit 03:00
2                                china 03:06  ...                         
3                        green finance 03:05  ...                         
4        sustainable development goals 03:04  ...                         
<BLANKLINE>
[5 rows x 5 columns]

>>> thematic_evolution_plot(
...     indicators=[ind_2016_2018, ind_2019_2020, ind_2021_2021],
...     figsize=(10, 10),
... ).savefig(file_name)

.. image:: images/thematic_evolution_plot.png
    :width: 700px
    :align: center

"""

from os.path import join

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle

from ....co_occ_matrix import co_occ_matrix

# from ....user_filters import _UserFilters


def _sankey_plot(
    data,
    heights,
    figsize=(6, 6),
):
    def compute_params(data, heights):

        params = {}
        for i_matrix, matrix in enumerate(data):

            if i_matrix == 0:
                params[i_matrix] = matrix.shape[0]
                params["space"] = matrix.sum().sum() * 0.1 / (params[i_matrix] - 1)
                params["height"] = matrix.sum().sum() * 1.1
            else:
                params[i_matrix] = matrix.shape[1]
                params["space"] = min(
                    params["space"], matrix.sum().sum() * 0.1 / (params[i_matrix] - 1)
                )

        params["height"] = 0.0
        for key in heights.keys():
            params["height"] = max(
                params["height"],
                heights[key].sum() + (len(heights[key]) - 1) * params["space"],
            )

        return params

    def generate_curve(p0, p2):

        x0, y0 = p0
        x2, y2 = p2

        ys_d = np.array(50 * [y0] + 50 * [y2])
        ys_d = np.convolve(ys_d, 0.05 * np.ones(20), mode="valid")
        yb = np.convolve(ys_d, 0.05 * np.ones(20), mode="valid")

        xb = np.linspace(x0, x2, len(yb))

        return xb, yb

    # def compute_bar_heights(data):

    #     heights = {}

    #     for i_axis in range(len(data) + 1):

    #         if i_axis == 0:
    #             matrix = data[0]
    #             heights[i_axis] = matrix.sum(axis=1)
    #         elif i_axis == len(data):
    #             matrix = data[-1]
    #             heights[i_axis] = matrix.sum(axis=0)
    #         else:
    #             heights[i_axis] = pd.Series(
    #                 np.maximum(data[i_axis - 1].sum(axis=0), data[i_axis].sum(axis=1)),
    #                 index=data[i_axis].index,
    #             )

    #     return heights

    def plot_groups(ax, data, heights, params):

        side = 0.01
        # bar_heights = compute_bar_heights(data)
        bar_heights = heights
        n_groups = len(bar_heights)
        centers = np.linspace(start=0.0, stop=1.0, num=n_groups)

        for i_group in range(n_groups):

            center = centers[i_group]
            base = 0.0
            values = bar_heights[i_group]
            for i_pos, value in enumerate(values):

                r = Rectangle(
                    xy=(center - side, base),
                    width=2 * side,
                    height=value,
                    color="tab:blue",
                )
                ax.add_patch(r)
                #
                text = values.index[i_pos]
                ax.text(
                    center + side + 0.008
                    if i_group < len(data)
                    else center - side - 0.008,
                    base + value / 2.0,
                    text,
                    fontsize=8,
                    horizontalalignment="left" if i_group < len(data) else "right",
                    verticalalignment="center_baseline",
                    zorder=10,
                )
                #
                base += value + params["space"]

    def plot_connections(ax, data, heights, params):
        def compute_max_min(data):
            values = [
                value
                for matrix in data
                for row in matrix.values.tolist()
                for value in row
                if value > 0
            ]
            max_value = max(values)
            min_value = min(values)

            return max_value, min_value

        side = 0.01
        max_value, min_value = compute_max_min(data)
        # bar_heights = compute_bar_heights(data)
        bar_heights = heights
        centers = np.linspace(start=0.0, stop=1.0, num=len(data) + 1)

        for i_panel, matrix in enumerate(data):

            # ----< base de cada barra >-------------------------------------------------
            right_base = pd.Series(0.0, index=matrix.columns)
            for i_column, column in enumerate(matrix.columns):

                if i_column > 0:
                    right_base[column] = (
                        right_base.iloc[i_column - 1]
                        + bar_heights[i_panel + 1][i_column - 1]
                        + params["space"]
                    )

            # ----< dibujo de cada barra >-----------------------------------------------
            left_base = 0.0
            for i_left, index in enumerate(matrix.index):

                for column in matrix.columns:

                    if matrix.loc[index, column] > 0:

                        p_left = centers[i_panel] + side, left_base
                        p_right = centers[i_panel + 1] - side, right_base[column]
                        lower_line = generate_curve(p_left, p_right)
                        x = lower_line[0]
                        y0 = lower_line[1]

                        p_left = (
                            centers[i_panel] + side,
                            left_base + matrix.loc[index, column],
                        )
                        p_right = (
                            centers[i_panel + 1] - side,
                            right_base[column] + matrix.loc[index, column],
                        )
                        upper_line = generate_curve(p_left, p_right)
                        y1 = upper_line[1]

                        alpha = 0.10 + 0.20 * (
                            matrix.loc[index, column] - min_value
                        ) / (max_value - min_value)

                        ax.fill_between(
                            x,
                            y0,
                            y1,
                            color="gray",
                            alpha=alpha,
                        )
                        left_base += matrix.loc[index, column]

                left_base = 0.0
                for i_bar in range(i_left + 1):
                    left_base += bar_heights[i_panel].iloc[i_bar] + params["space"]
                right_base += matrix.loc[index, :]

        return

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    params = compute_params(data, heights)
    plot_groups(ax, data, heights, params)
    plot_connections(ax, data, heights, params)

    ax.set_ylim(0, params["height"])
    ax.set_xlim(-0.05, 1.05)
    ax.set_axis_off()

    return fig


def thematic_evolution_plot(
    indicators,
    figsize=(6, 6),
):
    # ----< number of clusters per period >----------------------------------------------
    n_clusters = []
    for indicator in indicators:
        n_clusters.append(indicator[["cluster"]].drop_duplicates().shape[0])

    # ----< co-occurrence matrixes >-----------------------------------------------------
    data = []
    n_rows = n_clusters[0]
    for index in range(1, len(n_clusters)):
        row_names = [f"CL_{i}" for i in range(n_rows)]
        col_names = [f"CL_{i}" for i in range(n_clusters[index])]
        matrix = pd.DataFrame(
            np.zeros((n_rows, n_clusters[index])), index=row_names, columns=col_names
        )
        n_rows = n_clusters[index]
        data.append(matrix)

    # ----< matrices >-------------------------------------------------------------------
    for i_indicator in range(len(indicators) - 1):

        left_table = indicators[i_indicator]
        right_table = indicators[i_indicator + 1]

        for left_keyword in left_table.index:

            if left_keyword in right_table.index.to_list():

                left_cluster = f"CL_{left_table.loc[left_keyword, 'cluster']}"
                right_cluster = f"CL_{right_table.loc[left_keyword, 'cluster']}"
                data[i_indicator].loc[left_cluster, right_cluster] += min(
                    left_table.loc[left_keyword, "num_documents"],
                    right_table.loc[left_keyword, "num_documents"],
                )

    # ----< heights >--------------------------------------------------------------------
    heights = {}
    for i_indicator in range(len(indicators)):
        matrix = indicators[i_indicator][["cluster", "num_documents"]]
        matrix = matrix.groupby("cluster", as_index=True).sum()
        heights[i_indicator] = pd.Series(
            matrix.num_documents.tolist(),
            index=[f"CL_{i}" for i in matrix.index.tolist()],
        )

    # ----< rename clusters >------------------------------------------------------------
    for i_indicator in range(len(indicators)):

        indicator = indicators[i_indicator].copy()
        indicator["keyword"] = indicator.index
        indicator["rnk"] = indicator.groupby("cluster")["num_documents"].rank(
            method="first", ascending=False
        )
        indicator = indicator.query("rnk == 1").sort_values(
            by=["cluster", "num_documents", "global_citations", "node"],
            ascending=[True, False, False, True],
        )
        new_names = {f"CL_{i}": k for i, k in enumerate(indicator.keyword.tolist())}

        if i_indicator == 0:
            data[i_indicator] = data[i_indicator].rename(index=new_names)
        elif i_indicator == len(indicators) - 1:
            data[i_indicator - 1] = data[i_indicator - 1].rename(columns=new_names)
        else:
            data[i_indicator - 1] = data[i_indicator - 1].rename(columns=new_names)
            data[i_indicator] = data[i_indicator].rename(index=new_names)

        heights[i_indicator] = heights[i_indicator].rename(index=new_names)

    return _sankey_plot(
        data,
        heights,
        figsize=figsize,
    )
