# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Local Impact --- H-Index
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
...     metric="h_index",
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
| authors       |   h_index |   g_index |   m_index |
|:--------------|----------:|----------:|----------:|
| Jagtiani J.   |         3 |         3 |      1.5  |
| Gomber P.     |         2 |         2 |      0.67 |
| Hornuf L.     |         2 |         2 |      0.67 |
| Gai K.        |         2 |         2 |      0.67 |
| Qiu M.        |         2 |         2 |      0.67 |
| Sun X./3      |         2 |         2 |      0.67 |
| Lemieux C.    |         2 |         2 |      1    |
| Dolata M.     |         2 |         2 |      0.5  |
| Schwabe G.    |         2 |         2 |      0.5  |
| Zavolokina L. |         2 |         2 |      0.5  |

>>> items.fig_.write_html("sphinx/_static/analyze/contributors/authors/h_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/authors/h_index_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
