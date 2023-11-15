# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance metrics
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> root_dir = "data/regtech/"
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='abbr_source_title',
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
| abbr_source_title   |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:--------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| J. Econ. Bus.       |          1 |          5 |          5 |     3 |                422 |                 3 |         3 |         3 |       1.5 |
| J Manage Inf Syst   |          2 |          1 |          1 |     2 |                696 |                 4 |         2 |         2 |       1   |
| Rev. Financ. Stud.  |          3 |          4 |         20 |     2 |                432 |                 0 |         2 |         2 |       2   |
| Ind Manage Data Sys |          4 |          7 |          8 |     2 |                386 |                 2 |         2 |         2 |       1   |
| Electron. Mark.     |          5 |          9 |         11 |     2 |                287 |                 1 |         2 |         2 |       1   |



>>> items.fig_.write_html("sphinx/_static/analyze/contributors/sources/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/sources/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
