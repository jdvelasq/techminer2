# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance Metrics
===============================================================================

>>> from techminer2.analyze import performance_metrics
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.head().to_markdown())
| organizations                                         |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:------------------------------------------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| Univ. of Zurich (CHE)                                 |          1 |          8 |          3 |     3 |                434 |                 4 |         3 |         3 |      0.75 |
| Federal Reserve Bank of Philadelphia (USA)            |          2 |         17 |         14 |     3 |                317 |                 2 |         3 |         3 |      1.5  |
| Baylor Univ. (USA)                                    |          3 |          9 |         43 |     2 |                395 |                 0 |         2 |         2 |      2    |
| Max Planck Inst. for Innovation and Competition (DEU) |          4 |         14 |         12 |     2 |                358 |                 2 |         2 |         2 |      0.67 |
| Univ. of New South Wales (AUS)                        |          5 |         15 |         13 |     2 |                340 |                 2 |         2 |         2 |      0.67 |



>>> items.fig_.write_html("sphinx/_static/analyze/contributors/organizations/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/most_relevant_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
