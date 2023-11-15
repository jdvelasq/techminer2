# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Local Cited
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| organizations                        |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:-------------------------------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Sungkyunkwan Univ. (KOR)             |         20 |          1 |                307 |                 5 |                          153.5  |                           2.5  |                       76.75 |
| Goethe Univ. Frankfurt (DEU)         |          7 |          2 |                489 |                 4 |                          489    |                           4    |                      163    |
| Univ. of Zurich (CHE)                |          8 |          3 |                434 |                 4 |                          144.67 |                           1.33 |                      108.5  |
| Goethe Univ. of Frankfurt (DEU)      |          1 |          4 |                576 |                 3 |                          576    |                           3    |                      288    |
| Pennsylvania State Univ. (USA)       |          2 |          5 |                576 |                 3 |                          576    |                           3    |                      288    |
| Singapore Manag. Univ. (SMU) (SGP)   |          3 |          6 |                576 |                 3 |                          576    |                           3    |                      288    |
| Univ. of Delaware (USA)              |          4 |          7 |                576 |                 3 |                          576    |                           3    |                      288    |
| Univ. of Sydney (AUS)                |         21 |          8 |                300 |                 3 |                          150    |                           1.5  |                      100    |
| SK Telecom, Seoul, South Korea (KOR) |         50 |          9 |                146 |                 3 |                          146    |                           3    |                       36.5  |
| Hankyong Nac. Univ. (KOR)            |          5 |         10 |                557 |                 2 |                          557    |                           2    |                      278.5  |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/organizations/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/most_local_cited_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
