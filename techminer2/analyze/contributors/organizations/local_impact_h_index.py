# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- H-Index
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
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
| organizations                                         |   h_index |   g_index |   m_index |
|:------------------------------------------------------|----------:|----------:|----------:|
| Univ. of Zurich (CHE)                                 |         3 |         3 |      0.75 |
| Federal Reserve Bank of Philadelphia (USA)            |         3 |         3 |      1.5  |
| Baylor Univ. (USA)                                    |         2 |         2 |      2    |
| Max Planck Inst. for Innovation and Competition (DEU) |         2 |         2 |      0.67 |
| Univ. of New South Wales (AUS)                        |         2 |         2 |      0.67 |
| Pace Univ. (USA)                                      |         2 |         2 |      0.67 |
| Sungkyunkwan Univ. (KOR)                              |         2 |         2 |      0.5  |
| Univ. of Sydney (AUS)                                 |         2 |         2 |      0.67 |
| Federal Reserve Bank of Chicago (USA)                 |         2 |         2 |      1    |
| Univ. of Latvia (LVA)                                 |         2 |         2 |      0.5  |

>>> items.fig_.write_html("sphinx/_static/analyze/contributors/organizations/h_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/h_index_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
