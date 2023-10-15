# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Local Cited
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> root_dir = "data/regtech/"
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='abbr_source_title',
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
| abbr_source_title     |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:----------------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| J Manage Inf Syst     |          1 |          1 |                696 |                 4 |                          348    |                              2 |                      348    |
| J. Bus. Econ.         |          3 |          2 |                489 |                 4 |                          489    |                              4 |                      163    |
| Financial Innov.      |         14 |          3 |                190 |                 4 |                           95    |                              2 |                       47.5  |
| London Bus. Sch. Rev. |         36 |          4 |                 76 |                 4 |                           76    |                              4 |                       15.2  |
| J. Econ. Bus.         |          5 |          5 |                422 |                 3 |                          140.67 |                              1 |                      211    |
| Telecommun Policy     |         21 |          6 |                146 |                 3 |                          146    |                              3 |                       36.5  |
| Bus. Horiz.           |          2 |          7 |                557 |                 2 |                          557    |                              2 |                      278.5  |
| Ind Manage Data Sys   |          7 |          8 |                386 |                 2 |                          193    |                              1 |                      193    |
| New Polit. Econ.      |          8 |          9 |                314 |                 2 |                          314    |                              2 |                      104.67 |
| Int J Inf Manage      |         15 |         10 |                180 |                 2 |                          180    |                              2 |                       60    |



>>> items.fig_.write_html("sphinx/_static/analyze/contributors/sources/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/sources/most_local_cited_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
