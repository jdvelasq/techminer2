# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Local Cited
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> items = bibliometrix.countries.most_local_cited(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| countries            |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:---------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| United Kingdom       |         1 |                199 |                34 |                           28.43 |                           4.86 |                       33.17 |
| Ireland              |         5 |                 55 |                22 |                           11    |                           4.4  |                        9.17 |
| Germany              |         6 |                 51 |                17 |                           12.75 |                           4.25 |                        8.5  |
| Australia            |         2 |                199 |                15 |                           28.43 |                           2.14 |                       28.43 |
| Switzerland          |         7 |                 45 |                13 |                           11.25 |                           3.25 |                        6.43 |
| United States        |         4 |                 59 |                11 |                            9.83 |                           1.83 |                        7.38 |
| Hong Kong            |         3 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Luxembourg           |         8 |                 34 |                 8 |                           17    |                           4    |                        8.5  |
| Greece               |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| United Arab Emirates |        12 |                 13 |                 7 |                            6.5  |                           3.5  |                        3.25 |


>>> items.fig_.write_html("sphinx/_static/bibliometrix/countries/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/bibliometrix/countries/most_local_cited_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'local_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries            |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:---------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| United Kingdom       |         1 |                199 |                34 |                           28.43 |                           4.86 |                       33.17 |
| Ireland              |         5 |                 55 |                22 |                           11    |                           4.4  |                        9.17 |
| Germany              |         6 |                 51 |                17 |                           12.75 |                           4.25 |                        8.5  |
| Australia            |         2 |                199 |                15 |                           28.43 |                           2.14 |                       28.43 |
| Switzerland          |         7 |                 45 |                13 |                           11.25 |                           3.25 |                        6.43 |
| United States        |         4 |                 59 |                11 |                            9.83 |                           1.83 |                        7.38 |
| Hong Kong            |         3 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Luxembourg           |         8 |                 34 |                 8 |                           17    |                           4    |                        8.5  |
| Greece               |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| United Arab Emirates |        12 |                 13 |                 7 |                            6.5  |                           3.5  |                        3.25 |
```
<BLANKLINE>




"""
from ...vantagepoint.discover import list_items

FIELD = "countries"
METRIC = "local_citations"


def most_local_cited(
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
