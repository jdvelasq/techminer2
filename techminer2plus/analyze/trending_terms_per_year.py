# flake8: noqa
"""
Trending Terms per Year
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/analyze/trending_terms_per_year.html"

>>> import techminer2plus
>>> techminer2plus.analyze.trending_terms_per_year(
...     field="author_keywords",
...     root_dir=root_dir, 
... ).table_.head(20)
year                                     OCC  year_q1  ...  global_citations  rn
author_keywords                                        ...                      
CORPORATE_SOCIAL_RESPONSIBILITIES (CSR)    1     2017  ...                 1   0
CREDIT                                     1     2017  ...                 1   1
SEMANTIC_TECHNOLOGIES                      2     2018  ...                41   0
SMART_CONTRACTS                            2     2017  ...                22   1
BUSINESS_MODELS                            1     2018  ...               153   2
FUTURE_RESEARCH_DIRECTION                  1     2018  ...               153   3
ALGORITHMIC_STANDARDS                      1     2018  ...                21   4
FINANCIAL_SERVICES                         4     2018  ...               168   0
BLOCKCHAIN                                 3     2018  ...                 5   1
SANDBOXES                                  2     2018  ...                12   2
STANDARDS                                  1     2019  ...                33   3
DOGMAS                                     1     2019  ...                 5   4
REGTECH                                   28     2019  ...               329   0
FINTECH                                   12     2019  ...               249   1
COMPLIANCE                                 7     2020  ...                30   2
REGULATION                                 5     2018  ...               164   3
ARTIFICIAL_INTELLIGENCE                    4     2020  ...                23   4
REGULATORY_TECHNOLOGY                      7     2020  ...                37   0
ANTI_MONEY_LAUNDERING                      5     2020  ...                34   1
FINANCIAL_REGULATION                       4     2019  ...                35   2
<BLANKLINE>
[20 rows x 6 columns]



>>> techminer2plus.analyze.trending_terms_per_year(
...     field="author_keywords",
...     root_dir=root_dir,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/report/analyze/trending_terms_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> techminer2plus.analyze.trending_terms_per_year(
...     field="author_keywords",
...     custom_items=[
...         "FINTECH",
...         "REGULATORY_TECHNOLOGY",
...         "BLOCKCHAIN",
...         "SUPTECH",
...         "ARTIFICIAL_INTELLIGENCE",
...     ], 
...     root_dir=root_dir, 
... ).table_.head(10)
year                     OCC  year_q1  year_med  year_q3  global_citations  rn
author_keywords                                                               
BLOCKCHAIN                 3     2018      2019     2020                 5   0
FINTECH                   12     2019      2020     2020               249   0
ARTIFICIAL_INTELLIGENCE    4     2020      2020     2020                23   1
REGULATORY_TECHNOLOGY      7     2020      2021     2022                37   0
SUPTECH                    3     2020      2022     2022                 4   0




# pylint: disable=line-too-long
"""
import numpy as np
import plotly.graph_objects as go

from ..classes import BasicChart
from ..query import indicators_by_field, items_occ_by_year


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def trending_terms_per_year(
    field,
    n_words_per_year=5,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Trend topics"""

    words_by_year = items_occ_by_year(
        field=field,
        # min_occ=1,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if custom_items is not None:
        words_by_year = words_by_year.loc[custom_items, :]

    year_q1 = []
    year_med = []
    year_q3 = []

    for _, row in words_by_year.iterrows():
        sequence = []
        for item, year in zip(row, words_by_year.columns):
            if item > 0:
                sequence.extend([year] * int(item))

        year_q1.append(int(round(np.percentile(sequence, 25))))
        year_med.append(int(round(np.percentile(sequence, 50))))
        year_q3.append(int(round(np.percentile(sequence, 75))))

    words_by_year["year_q1"] = year_q1
    words_by_year["year_med"] = year_med
    words_by_year["year_q3"] = year_q3

    words_by_year = words_by_year.assign(
        OCC=words_by_year[words_by_year.columns[:-3]].sum(axis=1)
    )

    words_by_year = words_by_year[["OCC", "year_q1", "year_med", "year_q3"]]

    global_citations = indicators_by_field(
        field, root_dir=root_dir
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

    results = BasicChart()
    results.table_ = words_by_year

    min_occ = words_by_year.OCC.min()
    max_occ = words_by_year.OCC.max()
    words_by_year = words_by_year.assign(
        height=0.15
        + 0.82 * (words_by_year.OCC - min_occ) / (max_occ - min_occ)
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