# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Local Cited
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='countries',
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| countries      |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:---------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| United Kingdom |          1 |          1 |                199 |                35 |                           28.43 |                           5    |                       33.17 |
| Australia      |          2 |          2 |                199 |                31 |                           28.43 |                           4.43 |                       28.43 |
| Hong Kong      |          3 |          3 |                185 |                24 |                           61.67 |                           8    |                       26.43 |
| Ireland        |          5 |          4 |                 55 |                22 |                           11    |                           4.4  |                        9.17 |
| United States  |          4 |          5 |                 59 |                19 |                            9.83 |                           3.17 |                        7.38 |
| Germany        |          6 |          6 |                 51 |                15 |                           12.75 |                           3.75 |                        8.5  |
| Switzerland    |          7 |          7 |                 45 |                13 |                           11.25 |                           3.25 |                        6.43 |
| Luxembourg     |          8 |          8 |                 34 |                 8 |                           17    |                           4    |                        8.5  |
| Greece         |         10 |          9 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| China          |          9 |         10 |                 27 |                 5 |                            5.4  |                           1    |                        3.86 |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/most_local_cited_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
