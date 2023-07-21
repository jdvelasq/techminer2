# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Frequent
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> items = bibliometrix.authors.most_frequent(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| authors     |   rank_occ |   OCC |
|:------------|-----------:|------:|
| Arner DW    |          1 |     3 |
| Buckley RP  |          2 |     3 |
| Barberis JN |          3 |     2 |
| Butler T    |          4 |     2 |
| Hamdan A    |          5 |     2 |
| Turki M     |          6 |     2 |
| Lin W       |          7 |     2 |
| Singh C     |          8 |     2 |
| Brennan R   |          9 |     2 |
| Crane M     |         10 |     2 |


>>> items.fig_.write_html("sphinx/_static/bibliometrix/authors/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/bibliometrix/authors/most_frequent_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors     |   rank_occ |   OCC |
|:------------|-----------:|------:|
| Arner DW    |          1 |     3 |
| Buckley RP  |          2 |     3 |
| Barberis JN |          3 |     2 |
| Butler T    |          4 |     2 |
| Hamdan A    |          5 |     2 |
| Turki M     |          6 |     2 |
| Lin W       |          7 |     2 |
| Singh C     |          8 |     2 |
| Brennan R   |          9 |     2 |
| Crane M     |         10 |     2 |
```
<BLANKLINE>

"""
FIELD = "authors"
METRIC = "OCC"


def most_frequent(
    #
    # ITEMS PARAMS:
    field=FIELD,
    metric=METRIC,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a rank chart."""

    from ...vantagepoint.discover import list_items

    return list_items(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # CHART PARAMS:
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
