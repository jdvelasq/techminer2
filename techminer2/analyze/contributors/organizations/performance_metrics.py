# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance Metrics
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
...     metric="OCCGC",
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
>>> print(items.df_.head().to_markdown())
| organizations             |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:--------------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| Univ of Hong Kong (HKG)   |          1 |          1 |          1 |     3 |                185 |                24 |         3 |         3 |      0.43 |
| Univ Coll Cork (IRL)      |          2 |          5 |          2 |     3 |                 41 |                19 |         2 |         2 |      0.33 |
| Ahlia Univ (BHR)          |          3 |         16 |         20 |     3 |                 19 |                 3 |         2 |         2 |      0.5  |
| Coventry Univ (GBR)       |          4 |         17 |         17 |     2 |                 17 |                 4 |         2 |         1 |      0.5  |
| Univ of Westminster (GBR) |          5 |         18 |         18 |     2 |                 17 |                 4 |         2 |         1 |      0.5  |



>>> items.fig_.write_html("sphinx/_static/performance/contributors/organizations/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/contributors/organizations/most_relevant_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
