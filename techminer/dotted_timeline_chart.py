"""
Dotted timeline chart
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/dotted_timeline_chart.png"
>>> data = annual_occurrence_matrix('iso_source_name',  min_occ=8, directory=directory)
>>> dotted_timeline_chart(data, color='grey', figsize=(8, 6)).savefig(file_name)

.. image:: images/dotted_timeline_chart.png
    :width: 700px
    :align: center


"""
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import pandas as pd

TEXTLEN = 40


def dotted_timeline_chart(annual_occurrence_matrix, color="grey", figsize=(8, 6)):

    data = annual_occurrence_matrix.copy()
    data = data.transpose()

    # ---------------------------------------------------------------------------
    sorted_data = annual_occurrence_matrix.copy()
    column = sorted_data.index.name
    sorted_data = sorted_data.reset_index()
    sorted_data = pd.melt(
        sorted_data, id_vars=column, var_name="year", value_name="occurrences"
    )
    sorted_data["occurrences"] = sorted_data.occurrences.map(
        lambda x: np.nan if x == 0 else x
    )
    sorted_data = sorted_data.dropna()
    sorted_data = sorted_data.groupby(column).agg({"year": [np.max, np.min]})
    sorted_data.columns = sorted_data.columns.droplevel(0)
    sorted_data = sorted_data.rename(columns={"amax": "finish", "amin": "start"})
    sorted_data = sorted_data.sort_values(by=["start", "finish"])
    #
    data = data[sorted_data.index]
    # ---------------------------------------------------------------------------

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    for i_column, column in enumerate(data.columns):
        values = data[column]
        values = values[values > 0]
        ax.plot(
            values.index.tolist(),
            [i_column] * len(values),
            "o-k",
        )

    loc = plticker.MultipleLocator(1)

    # ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    ax.set_ylim(-0.5, len(data.columns) - 0.5)

    ax.set_yticklabels([""] + data.columns.tolist(), fontsize=9)

    for x in ["top", "right", "bottom"]:
        ax.spines[x].set_visible(False)

    ax.set_xticks(np.arange(data.index.min(), data.index.max() + 1, 1))

    xticks = [str(int(x)) for x in ax.get_xticks()]
    ax.set_xticklabels(xticks, rotation=90, ha="left", fontsize=9)

    ax.grid(axis="x", color="gray", linestyle=":")

    fig.set_tight_layout(True)

    return fig
