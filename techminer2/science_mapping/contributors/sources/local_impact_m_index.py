# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- M-Index
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> root_dir = "data/regtech/"
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='abbr_source_title',
...     metric="m_index",
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
| abbr_source_title       |   h_index |   g_index |   m_index |
|:------------------------|----------:|----------:|----------:|
| Rev. Financ. Stud.      |         2 |         2 |       2   |
| Financ. Manage.         |         2 |         2 |       2   |
| Sustainability          |         2 |         2 |       2   |
| J. Econ. Bus.           |         3 |         3 |       1.5 |
| J Manage Inf Syst       |         2 |         2 |       1   |
| Ind Manage Data Sys     |         2 |         2 |       1   |
| Electron. Mark.         |         2 |         2 |       1   |
| Small Bus. Econ.        |         1 |         1 |       1   |
| Symmetry                |         1 |         1 |       1   |
| J Strategic Inform Syst |         1 |         1 |       1   |



>>> items.fig_.write_html("sphinx/_static/analyze/contributors/sources/m_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/sources/m_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
