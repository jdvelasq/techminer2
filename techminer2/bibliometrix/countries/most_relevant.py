# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Relevant
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> items = bibliometrix.countries.most_relevant(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| countries      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:---------------|-----------:|----------:|------:|-------------------:|
| United Kingdom |          1 |         1 |     7 |                199 |
| Australia      |          2 |         2 |     7 |                199 |
| United States  |          3 |         4 |     6 |                 59 |
| Ireland        |          4 |         5 |     5 |                 55 |
| China          |          5 |         9 |     5 |                 27 |
| Italy          |          6 |        16 |     5 |                  5 |
| Germany        |          7 |         6 |     4 |                 51 |
| Switzerland    |          8 |         7 |     4 |                 45 |
| Bahrain        |          9 |        11 |     4 |                 19 |
| Hong Kong      |         10 |         3 |     3 |                185 |
| Luxembourg     |         11 |         8 |     2 |                 34 |
| Greece         |         15 |        10 |     1 |                 21 |


>>> items.fig_.write_html("sphinx/_static/bibliometrix/countries/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/bibliometrix/countries/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:---------------|-----------:|----------:|------:|-------------------:|
| United Kingdom |          1 |         1 |     7 |                199 |
| Australia      |          2 |         2 |     7 |                199 |
| United States  |          3 |         4 |     6 |                 59 |
| Ireland        |          4 |         5 |     5 |                 55 |
| China          |          5 |         9 |     5 |                 27 |
| Italy          |          6 |        16 |     5 |                  5 |
| Germany        |          7 |         6 |     4 |                 51 |
| Switzerland    |          8 |         7 |     4 |                 45 |
| Bahrain        |          9 |        11 |     4 |                 19 |
| Hong Kong      |         10 |         3 |     3 |                185 |
| Luxembourg     |         11 |         8 |     2 |                 34 |
| Greece         |         15 |        10 |     1 |                 21 |
```
<BLANKLINE>



"""
from ...vantagepoint.discover import list_items

FIELD = "countries"
METRIC = "OCCGC"


def most_relevant(
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
