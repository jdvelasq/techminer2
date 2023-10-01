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
| countries      |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:---------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| United Kingdom |          1 |     7 |             6 |                   1 |               14.29 |
| Australia      |          2 |     7 |             7 |                   0 |                0    |
| United States  |          3 |     6 |             4 |                   2 |               33.33 |
| Ireland        |          4 |     5 |             4 |                   1 |               20    |
| China          |          5 |     5 |             1 |                   4 |               80    |
| Italy          |          6 |     5 |             3 |                   2 |               40    |
| Germany        |          7 |     4 |             3 |                   1 |               25    |
| Switzerland    |          8 |     4 |             3 |                   1 |               25    |
| Bahrain        |          9 |     4 |             3 |                   1 |               25    |
| Hong Kong      |         10 |     3 |             3 |                   0 |                0    |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/most_frequent_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
