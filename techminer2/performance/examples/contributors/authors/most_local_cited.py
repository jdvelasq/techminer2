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

>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
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
| authors           |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Arner DW          |          1 |          1 |                185 |                24 |                           61.67 |                            8   |                       26.43 |
| Buckley RP        |          2 |          2 |                185 |                24 |                           61.67 |                            8   |                       26.43 |
| Barberis JN       |          3 |          3 |                161 |                19 |                           80.5  |                            9.5 |                       23    |
| Butler T          |          5 |          4 |                 41 |                19 |                           20.5  |                            9.5 |                        6.83 |
| Anagnostopoulos I |          4 |          5 |                153 |                17 |                          153    |                           17   |                       25.5  |
| OBrien L          |          6 |          6 |                 33 |                14 |                           33    |                           14   |                        6.6  |
| Baxter LG         |          7 |          7 |                 30 |                 8 |                           30    |                            8   |                        3.75 |
| Breymann W        |         10 |          8 |                 21 |                 8 |                           21    |                            8   |                        3.5  |
| Gross FJ          |         11 |          9 |                 21 |                 8 |                           21    |                            8   |                        3.5  |
| Kavassalis P      |         12 |         10 |                 21 |                 8 |                           21    |                            8   |                        3.5  |


>>> items.fig_.write_html("sphinx/_static/performance/contributors/authors/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/authors/most_local_cited_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
