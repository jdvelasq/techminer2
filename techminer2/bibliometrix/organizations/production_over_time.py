# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _organizations_production_over_time:

Production over Time
===============================================================================


>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> production_over_time = bibliometrix.organizations.production_over_time(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> production_over_time.fig_.write_html("sphinx/_static/organizations_production_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/organizations_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(production_over_time.df_.to_markdown())
| organizations                                                            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------------------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Univ of Hong Kong (HKG) 3:185                                            |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Univ Coll Cork (IRL) 3:041                                               |      0 |      0 |      1 |      1 |      0 |      0 |      1 |      0 |
| Ahlia Univ (BHR) 3:019                                                   |      0 |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| Coventry Univ (GBR) 2:017                                                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Univ of Westminster (GBR) 2:017                                          |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Dublin City Univ (IRL) 2:014                                             |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Politec di Milano (ITA) 2:002                                            |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Kingston Bus Sch (GBR) 1:153                                             |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| FinTech HK, Hong Kong (HKG) 1:150                                        |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |



>>> print(production_over_time.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'organizations' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                                            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------------------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Univ of Hong Kong (HKG) 3:185                                            |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Univ Coll Cork (IRL) 3:041                                               |      0 |      0 |      1 |      1 |      0 |      0 |      1 |      0 |
| Ahlia Univ (BHR) 3:019                                                   |      0 |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| Coventry Univ (GBR) 2:017                                                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Univ of Westminster (GBR) 2:017                                          |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Dublin City Univ (IRL) 2:014                                             |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Politec di Milano (ITA) 2:002                                            |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Kingston Bus Sch (GBR) 1:153                                             |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| FinTech HK, Hong Kong (HKG) 1:150                                        |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
```
<BLANKLINE>

>>> print(production_over_time.metrics_.head().to_markdown())
|    | organizations           |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:------------------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | Univ of Hong Kong (HKG) |   2017 |     2 |         2 |                161 |                 3 |     7 |                      23     |                      0.429 |
|  1 | Univ of Hong Kong (HKG) |   2020 |     1 |         3 |                 24 |                 5 |     4 |                       6     |                      1.25  |
|  2 | Univ Coll Cork (IRL)    |   2018 |     1 |         1 |                  8 |                 5 |     6 |                       1.333 |                      0.833 |
|  3 | Univ Coll Cork (IRL)    |   2019 |     1 |         2 |                 33 |                14 |     5 |                       6.6   |                      2.8   |
|  4 | Univ Coll Cork (IRL)    |   2022 |     1 |         3 |                  0 |                 0 |     2 |                       0     |                      0     |

>>> print(production_over_time.documents_.head().to_markdown())
|    | organizations                                                      | title                                                                 |   year | source_title                                                   |   global_citations |   local_citations | doi                            |
|---:|:-------------------------------------------------------------------|:----------------------------------------------------------------------|-------:|:---------------------------------------------------------------|-------------------:|------------------:|:-------------------------------|
|  0 | Kingston Bus Sch (GBR)                                             | FINTECH and REGTECH: impact on regulators and BANKS                   |   2018 | Journal of Economics and Business                              |                153 |                17 | 10.1016/J.JECONBUS.2018.07.003 |
|  1 | FinTech HK, Hong Kong (HKG)                                        | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                            |
|  2 | Univ of Hong Kong (HKG)                                            | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                            |
|  3 | ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                            |
|  4 | Univ Coll Cork (IRL)                                               | understanding REGTECH for digital REGULATORY_COMPLIANCE               |   2019 | Palgrave Studies in Digital Business and Enabling Technologies |                 33 |                14 | 10.1007/978-3-030-02330-0_6    |




"""
from ...vantagepoint.discover import terms_by_year

FIELD = "organizations"


def production_over_time(
    #
    # PARAMS:
    cumulative=False,
    #
    # CHART PARAMS:
    title=None,
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

    if title is None:
        title = "Organizations Production over Time"

    return terms_by_year(
        #
        # PARAMS:
        field=FIELD,
        cumulative=cumulative,
        #
        # CHART PARAMS:
        title=title,
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