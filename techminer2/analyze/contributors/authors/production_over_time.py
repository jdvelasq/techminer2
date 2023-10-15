# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Production over Time
===============================================================================


>>> from techminer2.analyze import terms_by_year
>>> terms = terms_by_year(
...     #
...     # PARAMS:
...     field="authors",
...     cumulative=False,
...     #
...     # CHART PARAMS:
...     title=None,
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
>>> terms.fig_.write_html("sphinx/_static/analyze/contributors/authors/production_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/authors/production_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> print(terms.df_.to_markdown())
| authors              |   2015 |   2016 |   2017 |   2018 |   2019 |
|:---------------------|-------:|-------:|-------:|-------:|-------:|
| Jagtiani J. 3:0317   |      0 |      0 |      0 |      2 |      1 |
| Gomber P. 2:1065     |      0 |      0 |      1 |      1 |      0 |
| Hornuf L. 2:0358     |      0 |      0 |      1 |      0 |      1 |
| Gai K. 2:0323        |      0 |      0 |      1 |      1 |      0 |
| Qiu M. 2:0323        |      0 |      0 |      1 |      1 |      0 |
| Sun X./3 2:0323      |      0 |      0 |      1 |      1 |      0 |
| Lemieux C. 2:0253    |      0 |      0 |      0 |      1 |      1 |
| Dolata M. 2:0181     |      0 |      2 |      0 |      0 |      0 |
| Schwabe G. 2:0181    |      0 |      2 |      0 |      0 |      0 |
| Zavolokina L. 2:0181 |      0 |      2 |      0 |      0 |      0 |



>>> print(terms.prompt_) # doctest: +ELLIPSIS
Your task is ...



>>> print(terms.metrics_.head().to_markdown())
|    | authors     |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | Jagtiani J. |   2018 |     2 |         2 |                220 |                 2 |     2 |                     110     |                      1     |
|  1 | Jagtiani J. |   2019 |     1 |         3 |                 97 |                 0 |     1 |                      97     |                      0     |
|  2 | Gomber P.   |   2017 |     1 |         1 |                489 |                 4 |     3 |                     163     |                      1.333 |
|  3 | Gomber P.   |   2018 |     1 |         2 |                576 |                 3 |     2 |                     288     |                      1.5   |
|  4 | Hornuf L.   |   2017 |     1 |         1 |                100 |                 1 |     3 |                      33.333 |                      0.333 |


>>> print(terms.documents_.head().to_markdown())
|    | authors   | document_title                                                                                                         |   year | source_title                                 |   global_citations |   local_citations | doi                           |
|---:|:----------|:-----------------------------------------------------------------------------------------------------------------------|-------:|:---------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Gomber P. | on the FINTECH_REVOLUTION: interpreting the FORCES of INNOVATION, DISRUPTION, and TRANSFORMATION in FINANCIAL_SERVICES |   2018 | Journal of Management Information Systems    |                576 |                 3 | 10.1080/07421222.2018.1440766 |
|  1 | Gomber P. | DIGITAL_FINANCE and FINTECH: CURRENT_RESEARCH and FUTURE_RESEARCH_DIRECTIONS                                           |   2017 | Journal of Business Economics                |                489 |                 4 | 10.1007/S11573-017-0852-X     |
|  2 | Hornuf L. | the EMERGENCE of the GLOBAL_FINTECH_MARKET: economic and TECHNOLOGICAL_DETERMINANTS                                    |   2019 | Small Business Economics                     |                258 |                 1 | 10.1007/S11187-018-9991-X     |
|  3 | Gai K.    | a SURVEY on FINTECH                                                                                                    |   2018 | Journal of Network and Computer Applications |                238 |                 1 | 10.1016/J.JNCA.2017.10.011    |
|  4 | Qiu M.    | a SURVEY on FINTECH                                                                                                    |   2018 | Journal of Network and Computer Applications |                238 |                 1 | 10.1016/J.JNCA.2017.10.011    |





"""
