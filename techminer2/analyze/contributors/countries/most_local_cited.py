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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| countries      |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:---------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Germany        |          2 |          1 |               1814 |                11 |                          259.14 |                           1.57 |                      604.67 |
| United States  |          1 |          2 |               3189 |                 8 |                          199.31 |                           0.5  |                     1063    |
| South Korea    |          3 |          3 |               1192 |                 8 |                          198.67 |                           1.33 |                      298    |
| China          |          4 |          4 |               1085 |                 4 |                          135.62 |                           0.5  |                      271.25 |
| Switzerland    |          6 |          5 |                660 |                 4 |                          165    |                           1    |                      165    |
| United Kingdom |          7 |          6 |                636 |                 4 |                          212    |                           1.33 |                      212    |
| Australia      |          5 |          7 |                783 |                 3 |                          156.6  |                           0.6  |                      261    |
| Singapore      |          8 |          8 |                576 |                 3 |                          576    |                           3    |                      288    |
| Denmark        |          9 |          9 |                330 |                 3 |                          165    |                           1.5  |                      110    |
| Netherlands    |         10 |         10 |                300 |                 2 |                          100    |                           0.67 |                      100    |

>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/most_local_cited_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
