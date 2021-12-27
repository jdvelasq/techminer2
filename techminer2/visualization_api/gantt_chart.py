"""
Gantt Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/gantt_chart.png"
>>> from techminer2.indicators_api.annual_occurrence_matrix import annual_occurrence_matrix
>>> data = annual_occurrence_matrix('iso_source_name',  min_occ=10, directory=directory)
>>> gantt_chart(data, color='tab:blue', figsize=(8, 6)).savefig(file_name)

.. image:: images/gantt_chart.png
    :width: 700px
    :align: center

"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TEXTLEN = 40


def gantt_chart(annual_occurrence_matrix, color="tab:blue", figsize=(8, 6)):

    data = annual_occurrence_matrix.copy()
    column = data.index.name
    data = data.reset_index()
    data = pd.melt(data, id_vars=column, var_name="year", value_name="occurrences")
    data["occurrences"] = data.occurrences.map(lambda x: np.nan if x == 0 else x)
    data = data.dropna()
    data = data.groupby(column).agg({"year": [np.max, np.min]})
    data.columns = data.columns.droplevel(0)
    data = data.rename(columns={"amax": "finish", "amin": "start"})
    data = data.assign(width=data.finish - data.start + 1)

    data["finish"] = data.finish + 1

    data = data.sort_values(by=["start", "finish"])

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.barh(
        y=data.index,
        width=data.width,
        left=data.start,
        color=color,
        edgecolor="k",
        linewidth=0.5,
        zorder=10,
    )

    for x in ["top", "right", "bottom"]:
        ax.spines[x].set_visible(False)

    years_range = np.arange(
        annual_occurrence_matrix.columns.values.min(),
        annual_occurrence_matrix.columns.values.max() + 1,
    )
    ax.set_xticks(years_range)

    # ax.tick_params(axis="x", labelrotation=90)
    xticks = [str(int(x)) for x in ax.get_xticks()]
    ax.set_xticklabels(xticks, rotation=90, ha="left", fontsize=9)

    ax.set_yticklabels(data.index, fontsize=9)

    ax.grid(axis="x", color="gray", linestyle=":")

    fig.set_tight_layout(True)

    return fig
