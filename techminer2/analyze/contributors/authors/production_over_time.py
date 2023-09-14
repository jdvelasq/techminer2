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


>>> from techminer2.performance.plots import terms_by_year
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> terms.fig_.write_html("sphinx/_static/performance/contributors/authors/production_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/contributors/authors/production_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> print(terms.df_.to_markdown())
| authors           |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Arner DW 3:185    |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Buckley RP 3:185  |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Barberis JN 2:161 |      0 |      2 |      0 |      0 |      0 |      0 |      0 |      0 |
| Butler T 2:041    |      0 |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
| Hamdan A 2:018    |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Turki M 2:018     |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Lin W 2:017       |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Singh C 2:017     |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Brennan R 2:014   |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Crane M 2:014     |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |



>>> print(terms.prompt_) # doctest: +ELLIPSIS
Your task is ...



>>> print(terms.metrics_.head().to_markdown())
|    | authors     |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | Arner DW    |   2017 |     2 |         2 |                161 |                19 |     7 |                          23 |                      2.714 |
|  1 | Arner DW    |   2020 |     1 |         3 |                 24 |                 5 |     4 |                           6 |                      1.25  |
|  2 | Buckley RP  |   2017 |     2 |         2 |                161 |                19 |     7 |                          23 |                      2.714 |
|  3 | Buckley RP  |   2020 |     1 |         3 |                 24 |                 5 |     4 |                           6 |                      1.25  |
|  4 | Barberis JN |   2017 |     2 |         2 |                161 |                19 |     7 |                          23 |                      2.714 |


>>> print(terms.documents_.head().to_markdown())
|    | authors     | title                                                                 |   year | source_title                                                   |   global_citations |   local_citations | doi                         |
|---:|:------------|:----------------------------------------------------------------------|-------:|:---------------------------------------------------------------|-------------------:|------------------:|:----------------------------|
|  0 | Arner DW    | fintech, regtech, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                16 | nan                         |
|  1 | Barberis JN | fintech, regtech, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                16 | nan                         |
|  2 | Buckley RP  | fintech, regtech, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                16 | nan                         |
|  3 | Butler T    | UNDERSTANDING_REGTECH for DIGITAL_REGULATORY_COMPLIANCE               |   2019 | Palgrave Studies in Digital Business and Enabling Technologies |                 33 |                14 | 10.1007/978-3-030-02330-0_6 |
|  4 | Buckley RP  | the road to REGTECH: the (astonishing) example of the EUROPEAN_UNION  |   2020 | Journal of Banking Regulation                                  |                 24 |                 5 | 10.1057/S41261-019-00104-1  |





"""
