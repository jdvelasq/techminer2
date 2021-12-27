"""
Column Trends
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/column_trends.png"
>>> column_trends('author_keywords', directory=directory).savefig(file_name)

.. image:: images/column_trends.png
    :width: 700px
    :align: center

>>> column_trends('author_keywords', directory=directory, plot=False).head()
pub_year                num_documents  year_q1  ...  global_citations  rn
author_keywords                                 ...                      
fintech                           139     2016  ...              1285   0
financial technologies             28     2016  ...               225   1
innovating                         13     2016  ...               249   2
bank                               13     2016  ...               193   3
financial service                  11     2016  ...               300   4
<BLANKLINE>
[5 rows x 6 columns]

"""

import matplotlib.pyplot as plt
import numpy as np

from .indicators_api.annual_occurrence_matrix import annual_occurrence_matrix
from .indicators_api.column_indicators import column_indicators


def column_trends(
    column,
    n_keywords_per_year=5,
    directory="./",
    plot=True,
    figsize=(6, 6),
):

    keywords_by_year = annual_occurrence_matrix(
        column=column,
        min_occ=1,
        directory=directory,
    )

    year_q1 = []
    year_med = []
    year_q3 = []

    for i_row, row in keywords_by_year.iterrows():

        sequence = []
        for item, year in zip(row, keywords_by_year.columns):
            if item > 0:
                sequence.extend([year] * int(item))

        year_q1.append(int(round(np.percentile(sequence, 0.25))))
        year_med.append(int(round(np.percentile(sequence, 0.50))))
        year_q3.append(int(round(np.percentile(sequence, 0.75))))

    keywords_by_year["year_q1"] = year_q1
    keywords_by_year["year_med"] = year_med
    keywords_by_year["year_q3"] = year_q3

    keywords_by_year = keywords_by_year.assign(
        num_documents=keywords_by_year[keywords_by_year.columns[:-3]].sum(axis=1)
    )

    keywords_by_year = keywords_by_year[
        ["num_documents", "year_q1", "year_med", "year_q3"]
    ]

    global_citations = column_indicators(column, directory=directory).global_citations

    keyword2citation = dict(zip(global_citations.index, global_citations.values))
    keywords_by_year = keywords_by_year.assign(
        global_citations=keywords_by_year.index.map(keyword2citation)
    )

    keywords_by_year = keywords_by_year.sort_values(
        by=["year_med", "num_documents", "global_citations"],
        ascending=[True, False, False],
    )

    keywords_by_year = keywords_by_year.assign(
        rn=keywords_by_year.groupby(["year_med"]).cumcount()
    ).sort_values(["year_med", "rn"], ascending=[True, True])

    keywords_by_year = keywords_by_year.query("rn < @n_keywords_per_year")

    if plot is False:
        return keywords_by_year

    min_documents = keywords_by_year.num_documents.min()
    max_documents = keywords_by_year.num_documents.max()
    keywords_by_year = keywords_by_year.assign(
        height=0.05
        + 0.9
        * (keywords_by_year.num_documents - min_documents)
        / (max_documents - min_documents)
    )
    keywords_by_year = keywords_by_year.assign(
        width=keywords_by_year.year_q3 - keywords_by_year.year_q1 + 1
    )

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.barh(
        y=keywords_by_year.index,
        width=keywords_by_year.width,
        # height=0.8,
        height=keywords_by_year.height,
        left=keywords_by_year.year_q1,
        alpha=0.8,
    )

    for x in ["top", "right", "bottom"]:
        ax.spines[x].set_visible(False)

    ax.grid(axis="x", color="gray", linestyle=":")
    xticks = [str(int(x)) for x in ax.get_xticks()]
    ax.set_xticklabels(xticks, rotation=90, ha="left", fontsize=9)
    ax.spines["left"].set_color("dimgray")
    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    fig.set_tight_layout(True)

    return fig
