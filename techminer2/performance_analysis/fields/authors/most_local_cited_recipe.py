# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Local Cited (Recipe)
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
...     metric="local_citations",
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # ITEM FILTERS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| authors           |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Butler T          |         5 |                 41 |                19 |                           20.5  |                           9.5  |                        6.83 |
| Anagnostopoulos I |         4 |                153 |                17 |                          153    |                          17    |                       25.5  |
| OBrien L          |         6 |                 33 |                14 |                           33    |                          14    |                        6.6  |
| Arner DW          |         1 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Buckley RP        |         2 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Breymann W        |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Gross FJ          |        11 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Kavassalis P      |        12 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Saxton K          |        13 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Stieber H         |        14 |                 21 |                 8 |                           21    |                           8    |                        3.5  |


>>> items.fig_.write_html("sphinx/_static/performance_analysis/fields/authors/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/authors/most_local_cited_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'local_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors           |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Butler T          |         5 |                 41 |                19 |                           20.5  |                           9.5  |                        6.83 |
| Anagnostopoulos I |         4 |                153 |                17 |                          153    |                          17    |                       25.5  |
| OBrien L          |         6 |                 33 |                14 |                           33    |                          14    |                        6.6  |
| Arner DW          |         1 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Buckley RP        |         2 |                185 |                 8 |                           61.67 |                           2.67 |                       26.43 |
| Breymann W        |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Gross FJ          |        11 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Kavassalis P      |        12 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Saxton K          |        13 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Stieber H         |        14 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
```
<BLANKLINE>

"""
