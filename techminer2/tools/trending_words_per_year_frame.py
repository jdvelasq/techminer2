# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trending Words per Year Frame
===============================================================================

>>> from techminer2.tools import trending_words_per_year_frame
>>> trending_words_per_year_frame(
...     #
...     # PARAMS:
...     field="author_keywords",
...     n_words_per_year=5,
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... ).head()
year              OCC  year_q1  year_med  ...  rn    height  width
author_keywords                           ...                     
CONTENT_ANALYSIS    2     2016      2016  ...   2  0.177333      1
DIGITALIZATION      2     2016      2016  ...   3  0.177333      1
POPULAR_PRESS       2     2016      2016  ...   4  0.177333      1
TECHNOLOGY          2     2016      2016  ...   0  0.177333      2
BANKING             2     2016      2016  ...   1  0.177333      2
<BLANKLINE>
[5 rows x 8 columns]

>>> from techminer2.tools import trending_words_per_year_frame
>>> trending_words_per_year_frame(
...     #
...     # PARAMS:
...     field="author_keywords",
...     n_words_per_year=5,
...     custom_terms=[
...         "FINTECH",
...         "BLOCKCHAIN",
...         "ARTIFICIAL_INTELLIGENCE",
...     ], 
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )    
year                     OCC  year_q1  year_med  ...  rn  height  width
author_keywords                                  ...                   
FINTECH                   31     2017      2018  ...   0    0.97      2
BLOCKCHAIN                 2     2018      2018  ...   1    0.15      2
ARTIFICIAL_INTELLIGENCE    2     2019      2019  ...   0    0.15      1
<BLANKLINE>
[3 rows x 8 columns]

"""
import numpy as np

from .._core.metrics.calculate_global_performance_metrics import calculate_global_performance_metrics
from .._core.metrics.extract_top_n_terms_by_metric import extract_top_n_terms_by_metric
from .._core.metrics.sort_records_by_metric import sort_records_by_metric
from .._core.metrics.term_occurrences_by_year import term_occurrences_by_year


def trending_words_per_year_frame(
    #
    # PARAMS:
    field,
    #
    # ITEM FILTERS:
    n_words_per_year=5,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """:meta private:"""

    #
    # Compute occurrences for all words
    words_by_year = term_occurrences_by_year(
        #
        # FUNCTION PARAMS:
        field=field,
        cumulative=False,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Apply filters
    if custom_terms is None:
        indicators = calculate_global_performance_metrics(
            field=field,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        indicators = sort_records_by_metric(indicators, metric="OCC")

        custom_terms = extract_top_n_terms_by_metric(
            indicators=indicators,
            metric="OCC",
            top_n=None,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    #
    # Select custom items
    words_by_year = words_by_year.loc[custom_terms, :]

    #
    # Compute percentiles
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

    global_citations = calculate_global_performance_metrics(field, root_dir=root_dir).global_citations

    word2citation = dict(zip(global_citations.index, global_citations.values))
    words_by_year = words_by_year.assign(global_citations=words_by_year.index.map(word2citation))

    words_by_year = words_by_year.sort_values(
        by=["year_med", "OCC", "global_citations"],
        ascending=[True, False, False],
    )

    words_by_year = words_by_year.assign(rn=words_by_year.groupby(["year_med"]).cumcount()).sort_values(
        ["year_med", "rn"], ascending=[True, True]
    )

    words_by_year = words_by_year.query(f"rn < {n_words_per_year}")

    min_occ = words_by_year.OCC.min()
    max_occ = words_by_year.OCC.max()
    words_by_year = words_by_year.assign(height=0.15 + 0.82 * (words_by_year.OCC - min_occ) / (max_occ - min_occ))
    words_by_year = words_by_year.assign(width=words_by_year.year_q3 - words_by_year.year_q1 + 1)

    # -----------------------------------------------------------------------------------
    # Reordeer the terms with the aim of improving the visualization
    words_by_year = words_by_year.sort_values(["year_q1", "width", "height"], ascending=[True, True, True])
    #
    # -----------------------------------------------------------------------------------

    return words_by_year

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
