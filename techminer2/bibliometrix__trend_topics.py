"""
Trend Topics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__trend_topics.html"

>>> from techminer2 import bibliometrix__trend_topics
>>> bibliometrix__trend_topics(
...     'author_keywords',
...     directory=directory, 
... ).table_.head()
year                               OCC  year_q1  ...  global_citations  rn
author_keywords                                  ...                      
regtech                             70     2016  ...               462   0
fintech                             42     2016  ...               406   1
regulatory technologies (regtech)   12     2016  ...                47   2
financial technologies               9     2016  ...                32   3
financial regulation                 8     2016  ...                91   4
<BLANKLINE>
[5 rows x 6 columns]

>>> bibliometrix__trend_topics(
...     'author_keywords', 
...     directory=directory,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__trend_topics.html" height="900px" width="100%" frameBorder="0"></iframe>

"""
from dataclasses import dataclass

import numpy as np
import plotly.graph_objects as go

from ._indicators.annual_occurrence_matrix import annual_occurrence_matrix
from ._indicators.column_indicators import column_indicators


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def bibliometrix__trend_topics(
    column,
    n_words_per_year=5,
    directory="./",
):
    """Trend topics"""

    words_by_year = annual_occurrence_matrix(
        column=column,
        min_occ=1,
        directory=directory,
    )

    year_q1 = []
    year_med = []
    year_q3 = []

    for _, row in words_by_year.iterrows():

        sequence = []
        for item, year in zip(row, words_by_year.columns):
            if item > 0:
                sequence.extend([year] * int(item))

        year_q1.append(int(round(np.percentile(sequence, 0.25))))
        year_med.append(int(round(np.percentile(sequence, 0.50))))
        year_q3.append(int(round(np.percentile(sequence, 0.75))))

    words_by_year["year_q1"] = year_q1
    words_by_year["year_med"] = year_med
    words_by_year["year_q3"] = year_q3

    words_by_year = words_by_year.assign(
        OCC=words_by_year[words_by_year.columns[:-3]].sum(axis=1)
    )

    words_by_year = words_by_year[["OCC", "year_q1", "year_med", "year_q3"]]

    global_citations = column_indicators(column, directory=directory).global_citations

    word2citation = dict(zip(global_citations.index, global_citations.values))
    words_by_year = words_by_year.assign(
        global_citations=words_by_year.index.map(word2citation)
    )

    words_by_year = words_by_year.sort_values(
        by=["year_med", "OCC", "global_citations"],
        ascending=[True, False, False],
    )

    words_by_year = words_by_year.assign(
        rn=words_by_year.groupby(["year_med"]).cumcount()
    ).sort_values(["year_med", "rn"], ascending=[True, True])

    words_by_year = words_by_year.query(f"rn < {n_words_per_year}")

    results = _Results()
    results.table_ = words_by_year

    min_occ = words_by_year.OCC.min()
    max_occ = words_by_year.OCC.max()
    words_by_year = words_by_year.assign(
        height=0.15 + 0.82 * (words_by_year.OCC - min_occ) / (max_occ - min_occ)
    )
    words_by_year = words_by_year.assign(
        width=words_by_year.year_q3 - words_by_year.year_q1 + 1
    )

    fig = go.Figure(
        go.Bar(
            x=words_by_year.width,
            y=words_by_year.index,
            base=words_by_year.year_q1,
            width=words_by_year.height,
            orientation="h",
            marker_color="lightslategrey",
        ),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        dtick=1.0,
    )
    results.plot_ = fig

    return results
