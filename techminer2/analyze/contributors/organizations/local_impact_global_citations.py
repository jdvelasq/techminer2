# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- Global Citations
===============================================================================


>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
...     metric="global_citations",
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| organizations                        |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:-------------------------------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Goethe Univ. of Frankfurt (DEU)      |          1 |          4 |                576 |                 3 |                          576    |                           3    |                       288   |
| Pennsylvania State Univ. (USA)       |          2 |          5 |                576 |                 3 |                          576    |                           3    |                       288   |
| Singapore Manag. Univ. (SMU) (SGP)   |          3 |          6 |                576 |                 3 |                          576    |                           3    |                       288   |
| Univ. of Delaware (USA)              |          4 |          7 |                576 |                 3 |                          576    |                           3    |                       288   |
| Hankyong Nac. Univ. (KOR)            |          5 |         10 |                557 |                 2 |                          557    |                           2    |                       278.5 |
| Western Illinois Univ. (USA)         |          6 |         11 |                557 |                 2 |                          557    |                           2    |                       278.5 |
| Goethe Univ. Frankfurt (DEU)         |          7 |          2 |                489 |                 4 |                          489    |                           4    |                       163   |
| Univ. of Zurich (CHE)                |          8 |          3 |                434 |                 4 |                          144.67 |                           1.33 |                       108.5 |
| Baylor Univ. (USA)                   |          9 |         43 |                395 |                 0 |                          197.5  |                           0    |                       395   |
| Columbia Graduate Sch. of Bus. (USA) |         10 |         44 |                390 |                 0 |                          390    |                           0    |                       195   |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/organizations/global_citations_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/global_citations_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
