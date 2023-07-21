# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trending Terms per Year
===============================================================================

>>> from techminer2.analyze.terms import trending_terms_per_year
>>> terms = trending_terms_per_year(
...     #
...     # PARAMS:
...     field="author_keywords",
...     n_words_per_year=5,
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> terms.fig_.write_html("sphinx/_static/visualize/trending_terms_per_year.html")

.. raw:: html

    <iframe src="../../../../_static/visualize/trending_terms_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>




>>> terms.df_.head(20)
year                                     OCC  year_q1  ...    height  width
author_keywords                                        ...                 
CORPORATE_SOCIAL_RESPONSIBILITIES (CSR)    1     2017  ...  0.150000      1
CREDIT                                     1     2017  ...  0.150000      1
SEMANTIC_TECHNOLOGIES                      2     2018  ...  0.180370      2
SMART_CONTRACTS                            2     2017  ...  0.180370      2
BUSINESS_MODELS                            1     2018  ...  0.150000      1
FUTURE_RESEARCH_DIRECTION                  1     2018  ...  0.150000      1
ALGORITHMIC_STANDARDS                      1     2018  ...  0.150000      1
FINANCIAL_SERVICES                         4     2018  ...  0.241111      3
BLOCKCHAIN                                 3     2018  ...  0.210741      3
SANDBOXES                                  2     2018  ...  0.180370      3
STANDARDS                                  1     2019  ...  0.150000      1
DOGMAS                                     1     2019  ...  0.150000      1
REGTECH                                   28     2019  ...  0.970000      4
FINTECH                                   12     2019  ...  0.484074      2
COMPLIANCE                                 7     2020  ...  0.332222      3
REGULATION                                 5     2018  ...  0.271481      4
ARTIFICIAL_INTELLIGENCE                    4     2020  ...  0.241111      1
REGULATORY_TECHNOLOGY                      7     2020  ...  0.332222      3
ANTI_MONEY_LAUNDERING                      5     2020  ...  0.271481      2
FINANCIAL_REGULATION                       4     2019  ...  0.241111      4
<BLANKLINE>
[20 rows x 8 columns]


>>> from techminer2.analyze.terms import trending_terms_per_year
>>> terms = trending_terms_per_year(
...     #
...     # PARAMS:
...     field="author_keywords",
...     n_words_per_year=5,
...     custom_items=[
...         "FINTECH",
...         "REGULATORY_TECHNOLOGY",
...         "BLOCKCHAIN",
...         "SUPTECH",
...         "ARTIFICIAL_INTELLIGENCE",
...     ], 
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )    
>>> terms.df_
year                     OCC  year_q1  year_med  ...  rn    height  width
author_keywords                                  ...                     
BLOCKCHAIN                 3     2018      2019  ...   0  0.150000      3
FINTECH                   12     2019      2020  ...   0  0.970000      2
ARTIFICIAL_INTELLIGENCE    4     2020      2020  ...   1  0.241111      1
REGULATORY_TECHNOLOGY      7     2020      2021  ...   0  0.514444      3
SUPTECH                    3     2020      2022  ...   0  0.150000      3
<BLANKLINE>
[5 rows x 8 columns]


"""
from dataclasses import dataclass

import numpy as np
import plotly.graph_objects as go

from ...techminer.metrics.global_indicators_by_field import global_indicators_by_field
from ...techminer.metrics.items_occurrences_by_year import items_occurrences_by_year


def trending_terms_per_year(
    #
    # PARAMS:
    field,
    n_words_per_year=5,
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Trend topics

    :meta private:
    """

    words_by_year = items_occurrences_by_year(
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

    words_by_year = words_by_year.assign(OCC=words_by_year[words_by_year.columns[:-3]].sum(axis=1))

    words_by_year = words_by_year[["OCC", "year_q1", "year_med", "year_q3"]]

    global_citations = global_indicators_by_field(field, root_dir=root_dir).global_citations

    word2citation = dict(zip(global_citations.index, global_citations.values))
    words_by_year = words_by_year.assign(global_citations=words_by_year.index.map(word2citation))

    words_by_year = words_by_year.sort_values(
        by=["year_med", "OCC", "global_citations"],
        ascending=[True, False, False],
    )

    words_by_year = words_by_year.assign(
        rn=words_by_year.groupby(["year_med"]).cumcount()
    ).sort_values(["year_med", "rn"], ascending=[True, True])

    words_by_year = words_by_year.query(f"rn < {n_words_per_year}")

    min_occ = words_by_year.OCC.min()
    max_occ = words_by_year.OCC.max()
    words_by_year = words_by_year.assign(
        height=0.15 + 0.82 * (words_by_year.OCC - min_occ) / (max_occ - min_occ)
    )
    words_by_year = words_by_year.assign(width=words_by_year.year_q3 - words_by_year.year_q1 + 1)

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

    @dataclass
    class Results:
        df_ = words_by_year
        fig_ = fig

    return Results()
