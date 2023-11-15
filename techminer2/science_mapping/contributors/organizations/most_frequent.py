# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
...     metric="OCC",
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
| organizations                                         |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:------------------------------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| Univ. of Zurich (CHE)                                 |          1 |     3 |             3 |                   0 |                   0 |
| Federal Reserve Bank of Philadelphia (USA)            |          2 |     3 |             0 |                   3 |                 100 |
| Baylor Univ. (USA)                                    |          3 |     2 |             0 |                   2 |                 100 |
| Max Planck Inst. for Innovation and Competition (DEU) |          4 |     2 |             1 |                   1 |                  50 |
| Univ. of New South Wales (AUS)                        |          5 |     2 |             1 |                   1 |                  50 |
| Pace Univ. (USA)                                      |          6 |     2 |             1 |                   1 |                  50 |
| Sungkyunkwan Univ. (KOR)                              |          7 |     2 |             1 |                   1 |                  50 |
| Univ. of Sydney (AUS)                                 |          8 |     2 |             1 |                   1 |                  50 |
| Federal Reserve Bank of Chicago (USA)                 |          9 |     2 |             0 |                   2 |                 100 |
| Univ. of Latvia (LVA)                                 |         10 |     2 |             2 |                   0 |                   0 |




>>> items.fig_.write_html("sphinx/_static/analyze/contributors/organizations/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
