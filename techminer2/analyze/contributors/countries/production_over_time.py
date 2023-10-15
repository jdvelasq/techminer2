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
...     field="countries",
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
>>> terms.fig_.write_html("sphinx/_static/analyze/contributors/countries/production_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/production_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> print(terms.df_.to_markdown())
| countries              |   2015 |   2016 |   2017 |   2018 |   2019 |
|:-----------------------|-------:|-------:|-------:|-------:|-------:|
| United States 16:3189  |      0 |      0 |      1 |      8 |      7 |
| China 08:1085          |      0 |      1 |      2 |      1 |      4 |
| Germany 07:1814        |      0 |      0 |      2 |      4 |      1 |
| South Korea 06:1192    |      0 |      2 |      0 |      3 |      1 |
| Australia 05:0783      |      0 |      0 |      2 |      2 |      1 |
| Switzerland 04:0660    |      0 |      3 |      1 |      0 |      0 |
| United Kingdom 03:0636 |      0 |      0 |      1 |      2 |      0 |
| Netherlands 03:0300    |      0 |      0 |      1 |      1 |      1 |
| Denmark 02:0330        |      0 |      0 |      1 |      1 |      0 |
| Latvia 02:0163         |      0 |      1 |      1 |      0 |      0 |



>>> print(terms.prompt_) # doctest: +ELLIPSIS
Your task is ...


>>> print(terms.metrics_.head().to_markdown())
|    | countries     |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:--------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | United States |   2017 |     1 |         1 |                 85 |                 0 |     3 |                      28.333 |                      0     |
|  1 | United States |   2018 |     8 |         9 |               2163 |                 8 |     2 |                    1081.5   |                      4     |
|  2 | United States |   2019 |     7 |        16 |                941 |                 0 |     1 |                     941     |                      0     |
|  3 | China         |   2016 |     1 |         1 |                 96 |                 1 |     4 |                      24     |                      0.25  |
|  4 | China         |   2017 |     2 |         3 |                265 |                 2 |     3 |                      88.333 |                      0.667 |



    
>>> print(terms.documents_.head().to_markdown())
|    | countries     | document_title                                                                                                         |   year | source_title                              |   global_citations |   local_citations | doi                           |
|---:|:--------------|:-----------------------------------------------------------------------------------------------------------------------|-------:|:------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Germany       | on the FINTECH_REVOLUTION: interpreting the FORCES of INNOVATION, DISRUPTION, and TRANSFORMATION in FINANCIAL_SERVICES |   2018 | Journal of Management Information Systems |                576 |                 3 | 10.1080/07421222.2018.1440766 |
|  1 | United States | on the FINTECH_REVOLUTION: interpreting the FORCES of INNOVATION, DISRUPTION, and TRANSFORMATION in FINANCIAL_SERVICES |   2018 | Journal of Management Information Systems |                576 |                 3 | 10.1080/07421222.2018.1440766 |
|  2 | South Korea   | FINTECH: ECOSYSTEM, BUSINESS_MODELS, INVESTMENT_DECISIONS, and CHALLENGES                                              |   2018 | Business Horizons                         |                557 |                 2 | 10.1016/J.BUSHOR.2017.09.003  |
|  3 | United States | FINTECH: ECOSYSTEM, BUSINESS_MODELS, INVESTMENT_DECISIONS, and CHALLENGES                                              |   2018 | Business Horizons                         |                557 |                 2 | 10.1016/J.BUSHOR.2017.09.003  |
|  4 | Germany       | DIGITAL_FINANCE and FINTECH: CURRENT_RESEARCH and FUTURE_RESEARCH_DIRECTIONS                                           |   2017 | Journal of Business Economics             |                489 |                 4 | 10.1007/S11573-017-0852-X     |




"""
