# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Production over Time
===============================================================================


>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> production_over_time = bibliometrix.sources.production_over_time(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> production_over_time.fig_.write_html("sphinx/_static/bibliometrix/sources/production_over_time.html")

.. raw:: html

    <iframe src="../../../../_static/bibliometrix/sources/production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(production_over_time.df_.to_markdown())
| source_abbr                         |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| J BANK REGUL 2:035                  |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| J FINANC CRIME 2:013                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| FOSTER INNOVCOMPET WITH FINTE 2:001 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |      0 |
| STUD COMPUT INTELL 2:001            |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| INT CONF INF TECHNOL SYST INN 2:000 |      0 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| ROUTLEDGE HANDBFINANCIAL TECH 2:000 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| J ECON BUS 1:153                    |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| NORTHWEST J INTL LAW BUS 1:150      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| PALGRAVE STUD DIGIT BUS ENABL 1:033 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| DUKE LAW J 1:030                    |      1 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |



>>> print(production_over_time.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'source_abbr' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                         |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| J BANK REGUL 2:035                  |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| J FINANC CRIME 2:013                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| FOSTER INNOVCOMPET WITH FINTE 2:001 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |      0 |
| STUD COMPUT INTELL 2:001            |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| INT CONF INF TECHNOL SYST INN 2:000 |      0 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| ROUTLEDGE HANDBFINANCIAL TECH 2:000 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| J ECON BUS 1:153                    |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| NORTHWEST J INTL LAW BUS 1:150      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| PALGRAVE STUD DIGIT BUS ENABL 1:033 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| DUKE LAW J 1:030                    |      1 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |
```
<BLANKLINE>

>>> print(production_over_time.metrics_.head().to_markdown())
|    | source_abbr                   |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:------------------------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | J BANK REGUL                  |   2020 |     1 |         1 |                 24 |                 5 |     4 |                       6     |                      1.25  |
|  1 | J BANK REGUL                  |   2021 |     1 |         2 |                 11 |                 4 |     3 |                       3.667 |                      1.333 |
|  2 | J FINANC CRIME                |   2020 |     1 |         1 |                 10 |                 3 |     4 |                       2.5   |                      0.75  |
|  3 | J FINANC CRIME                |   2022 |     1 |         2 |                  3 |                 1 |     2 |                       1.5   |                      0.5   |
|  4 | FOSTER INNOVCOMPET WITH FINTE |   2020 |     2 |         2 |                  1 |                 1 |     4 |                       0.25  |                      0.25  |


>>> print(production_over_time.documents_.head().to_markdown())
|    | source_abbr                   | title                                                                                                             |   year | source_title                                                   |   global_citations |   local_citations | doi                            |
|---:|:------------------------------|:------------------------------------------------------------------------------------------------------------------|-------:|:---------------------------------------------------------------|-------------------:|------------------:|:-------------------------------|
|  0 | J ECON BUS                    | FINTECH and REGTECH: impact on regulators and BANKS                                                               |   2018 | Journal of Economics and Business                              |                153 |                17 | 10.1016/J.JECONBUS.2018.07.003 |
|  1 | NORTHWEST J INTL LAW BUS      | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION                                             |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                            |
|  2 | PALGRAVE STUD DIGIT BUS ENABL | understanding REGTECH for digital REGULATORY_COMPLIANCE                                                           |   2019 | Palgrave Studies in Digital Business and Enabling Technologies |                 33 |                14 | 10.1007/978-3-030-02330-0_6    |
|  3 | DUKE LAW J                    | adaptive FINANCIAL_REGULATION and REGTECH: a concept ARTICLE on realistic protection for victims of BANK failures |   2016 | Duke Law Journal                                               |                 30 |                 0 | nan                            |
|  4 | J BANK REGUL                  | the road to REGTECH: the (astonishing) example of the EUROPEAN_UNION                                              |   2020 | Journal of Banking Regulation                                  |                 24 |                 5 | 10.1057/S41261-019-00104-1     |




"""
from ...vantagepoint.discover import terms_by_year

FIELD = "source_abbr"


def production_over_time(
    #
    # PARAMS:
    cumulative=False,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Sources production over time."""

    return terms_by_year(
        #
        # PARAMS:
        field=FIELD,
        cumulative=cumulative,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
