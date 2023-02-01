"""
Trend Topics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__trend_topics.html"

>>> from techminer2 import bibliometrix__trend_topics
>>> bibliometrix__trend_topics(
...     'author_keywords',
...     directory=directory, 
... ).table_.head(20)
year                        OCC  year_q1  ...  global_citations  rn
author_keywords                           ...                      
regtech                      69     2016  ...               461   0
fintech                      42     2016  ...               406   1
regulatory technology        12     2016  ...                47   2
financial technology          9     2016  ...                32   3
financial regulation          8     2016  ...                91   4
blockchain                   18     2017  ...               109   0
financial services            5     2017  ...               135   1
smart contracts               3     2017  ...                15   2
sandboxes                     2     2017  ...                 7   3
shared ledger technologies    1     2017  ...                 9   4
artificial intelligence      13     2018  ...                65   0
compliance                   12     2018  ...                20   1
regulation                    6     2018  ...               120   2
financial inclusion           5     2018  ...                68   3
cryptocurrency                4     2018  ...                29   4
machine learning              6     2019  ...                13   0
anti-money laundering         4     2019  ...                30   1
crowdfunding                  4     2019  ...                30   2
suptech                       4     2019  ...                 3   3
p2p lending                   3     2019  ...                26   4
<BLANKLINE>
[20 rows x 6 columns]





>>> bibliometrix__trend_topics(
...     'author_keywords', 
...     directory=directory,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__trend_topics.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> bibliometrix__trend_topics(
...     'author_keywords',
...     custom_topics=[
...         "fintech",
...         "regulatory technology",
...         "blockchain",
...         "suptech",
...         "artificial intelligence",
...         "financial inclusion",
...     ], 
...     directory=directory, 
... ).table_.head(10)
year                     OCC  year_q1  year_med  year_q3  global_citations  rn
author_keywords                                                               
fintech                   42     2016      2016     2016               406   0
regulatory technology     12     2016      2016     2016                47   1
blockchain                18     2017      2017     2017               109   0
artificial intelligence   13     2018      2018     2018                65   0
financial inclusion        5     2018      2018     2018                68   1
suptech                    4     2019      2019     2019                 3   0


"""
from dataclasses import dataclass

import numpy as np
import plotly.graph_objects as go

from .techminer.indicators.tm2__annual_occurrence_matrix import (
    tm2__annual_occurrence_matrix,
)
from .techminer.indicators.tm2__indicators_by_topic import tm2__indicators_by_topic


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def bibliometrix__trend_topics(
    criterion,
    n_words_per_year=5,
    custom_topics=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Trend topics"""

    words_by_year = tm2__annual_occurrence_matrix(
        criterion=criterion,
        min_occ=1,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if custom_topics is not None:
        words_by_year = words_by_year.loc[custom_topics, :]

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

    global_citations = tm2__indicators_by_topic(
        criterion, directory=directory
    ).global_citations

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
