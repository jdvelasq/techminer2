# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Frequent
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='countries',
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
| countries      |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:---------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| United States  |          1 |    16 |             1 |                  15 |               93.75 |
| China          |          2 |     8 |             3 |                   5 |               62.5  |
| Germany        |          3 |     7 |             2 |                   5 |               71.43 |
| South Korea    |          4 |     6 |             2 |                   4 |               66.67 |
| Australia      |          5 |     5 |             2 |                   3 |               60    |
| Switzerland    |          6 |     4 |             4 |                   0 |                0    |
| United Kingdom |          7 |     3 |             1 |                   2 |               66.67 |
| Netherlands    |          8 |     3 |             1 |                   2 |               66.67 |
| Denmark        |          9 |     2 |             1 |                   1 |               50    |
| Latvia         |         10 |     2 |             2 |                   0 |                0    |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/most_frequent_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
