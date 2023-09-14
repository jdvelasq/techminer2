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
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
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
| organizations                                                      |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:-------------------------------------------------------------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Univ of Hong Kong (HKG)                                            |          1 |          1 |                185 |                24 |                           61.67 |                           8    |                       26.43 |
| Univ Coll Cork (IRL)                                               |          5 |          2 |                 41 |                19 |                           13.67 |                           6.33 |                        6.83 |
| Kingston Bus Sch (GBR)                                             |          2 |          3 |                153 |                17 |                          153    |                          17    |                       25.5  |
| FinTech HK, Hong Kong (HKG)                                        |          3 |          4 |                150 |                16 |                          150    |                          16    |                       21.43 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |          4 |          5 |                150 |                16 |                          150    |                          16    |                       21.43 |
| Duke Univ Sch of Law (USA)                                         |          6 |          6 |                 30 |                 8 |                           30    |                           8    |                        3.75 |
| European Central B (DEU)                                           |         11 |          7 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Harvard Univ Weatherhead ctr for International Affairs (USA)       |         12 |          8 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| KS Strategic, London, United Kingdom (GBR)                         |         13 |          9 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Panepistemio Aigaiou, Chios, Greece (GRC)                          |         14 |         10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/organizations/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/most_local_cited_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
