# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- Global Citations
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> items = bibliometrix.authors.local_impact_global_citations(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| authors           |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Arner DW          |         1 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Buckley RP        |         2 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Barberis JN       |         3 |                161 |                 3 |                           80.5  |                           1.5  |                       23    |
| Anagnostopoulos I |         4 |                153 |                17 |                          153    |                          17    |                       25.5  |
| Butler T          |         5 |                 41 |                19 |                           20.5  |                           9.5  |                        6.83 |
| OBrien L          |         6 |                 33 |                14 |                           33    |                          14    |                        6.6  |
| Baxter LG         |         7 |                 30 |                 0 |                           30    |                           0    |                        3.75 |
| Weber RH          |         8 |                 24 |                 5 |                           24    |                           5    |                        6    |
| Zetzsche DA       |         9 |                 24 |                 5 |                           24    |                           5    |                        6    |
| Breymann W        |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |




>>> items.fig_.write_html("sphinx/_static/bibliometrix/authors/global_citations_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/bibliometrix/authors/global_citations_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'global_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors           |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Arner DW          |         1 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Buckley RP        |         2 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Barberis JN       |         3 |                161 |                 3 |                           80.5  |                           1.5  |                       23    |
| Anagnostopoulos I |         4 |                153 |                17 |                          153    |                          17    |                       25.5  |
| Butler T          |         5 |                 41 |                19 |                           20.5  |                           9.5  |                        6.83 |
| OBrien L          |         6 |                 33 |                14 |                           33    |                          14    |                        6.6  |
| Baxter LG         |         7 |                 30 |                 0 |                           30    |                           0    |                        3.75 |
| Weber RH          |         8 |                 24 |                 5 |                           24    |                           5    |                        6    |
| Zetzsche DA       |         9 |                 24 |                 5 |                           24    |                           5    |                        6    |
| Breymann W        |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
```
<BLANKLINE>



"""
from ...vantagepoint.discover import list_items

FIELD = "authors"
METRIC = "global_citations"


def local_impact_global_citations(
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
