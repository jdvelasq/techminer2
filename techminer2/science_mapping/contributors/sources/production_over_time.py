# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Production over Time
===============================================================================


>>> from techminer2.analyze import terms_by_year
>>> terms = terms_by_year(
...     #
...     # PARAMS:
...     field="abbr_source_title",
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
>>> terms.fig_.write_html("sphinx/_static/analyze/contributors/sources/production_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/sources/production_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> print(terms.df_.to_markdown())
| abbr_source_title         |   2015 |   2016 |   2017 |   2018 |   2019 |
|:--------------------------|-------:|-------:|-------:|-------:|-------:|
| J. Econ. Bus. 3:422       |      0 |      0 |      0 |      3 |      0 |
| J Manage Inf Syst 2:696   |      0 |      0 |      0 |      2 |      0 |
| Rev. Financ. Stud. 2:432  |      0 |      0 |      0 |      0 |      2 |
| Ind Manage Data Sys 2:386 |      0 |      0 |      0 |      1 |      1 |
| Electron. Mark. 2:287     |      0 |      0 |      0 |      2 |      0 |
| Financial Innov. 2:190    |      0 |      1 |      1 |      0 |      0 |
| Financ. Manage. 2:161     |      0 |      0 |      0 |      0 |      2 |
| Sustainability 2:150      |      0 |      0 |      0 |      0 |      2 |
| Bus. Horiz. 1:557         |      0 |      0 |      0 |      1 |      0 |
| J. Bus. Econ. 1:489       |      0 |      0 |      1 |      0 |      0 |



>>> print(terms.prompt_) # doctest: +ELLIPSIS
Your task is ...

>>> print(terms.metrics_.head().to_markdown())
|    | abbr_source_title   |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:--------------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | J. Econ. Bus.       |   2018 |     3 |         3 |                422 |                 3 |     2 |                       211   |                        1.5 |
|  1 | J Manage Inf Syst   |   2018 |     2 |         2 |                696 |                 4 |     2 |                       348   |                        2   |
|  2 | Rev. Financ. Stud.  |   2019 |     2 |         2 |                432 |                 0 |     1 |                       432   |                        0   |
|  3 | Ind Manage Data Sys |   2018 |     1 |         1 |                161 |                 2 |     2 |                        80.5 |                        1   |
|  4 | Ind Manage Data Sys |   2019 |     1 |         2 |                225 |                 0 |     1 |                       225   |                        0   |


>>> print(terms.documents_.head().to_markdown())
|    | abbr_source_title   | document_title                                                                                                         |   year | source_title                              |   global_citations |   local_citations | doi                           |
|---:|:--------------------|:-----------------------------------------------------------------------------------------------------------------------|-------:|:------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | J Manage Inf Syst   | on the FINTECH_REVOLUTION: interpreting the FORCES of INNOVATION, DISRUPTION, and TRANSFORMATION in FINANCIAL_SERVICES |   2018 | Journal of Management Information Systems |                576 |                 3 | 10.1080/07421222.2018.1440766 |
|  1 | Bus. Horiz.         | FINTECH: ECOSYSTEM, BUSINESS_MODELS, INVESTMENT_DECISIONS, and CHALLENGES                                              |   2018 | Business Horizons                         |                557 |                 2 | 10.1016/J.BUSHOR.2017.09.003  |
|  2 | J. Bus. Econ.       | DIGITAL_FINANCE and FINTECH: CURRENT_RESEARCH and FUTURE_RESEARCH_DIRECTIONS                                           |   2017 | Journal of Business Economics             |                489 |                 4 | 10.1007/S11573-017-0852-X     |
|  3 | Rev. Financ. Stud.  | how valuable is FINTECH_INNOVATION?                                                                                    |   2019 | Review of Financial Studies               |                235 |                 0 | 10.1093/RFS/HHY130            |
|  4 | Ind Manage Data Sys | ARTIFICIAL_INTELLIGENCE in FINTECH: UNDERSTANDING ROBO_ADVISORS ADOPTION among CUSTOMERS                               |   2019 | Industrial Management and Data Systems    |                225 |                 0 | 10.1108/IMDS-08-2018-0368     |


"""
