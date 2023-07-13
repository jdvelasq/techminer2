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
>>> production_over_time = bibliometrix.authors.production_over_time(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> production_over_time.fig_.write_html("sphinx/_static/authors_production_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(production_over_time.df_.to_markdown())
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



>>> print(production_over_time.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'authors' in a scientific bibliography database. Summarize the table below, \\
delimited by triple backticks, identify any notable patterns, trends, or \\
outliers in the data, and disc  uss their implications for the research \\
field. Be sure to provide a concise summary of your findings in no more \\
than 150 words.
<BLANKLINE>
Table:
```
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
```
<BLANKLINE>


>>> print(production_over_time.metrics_.head().to_markdown())
|    | authors     |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | Arner DW    |   2017 |     2 |         2 |                161 |                 3 |     7 |                          23 |                      0.429 |
|  1 | Arner DW    |   2020 |     1 |         3 |                 24 |                 5 |     4 |                           6 |                      1.25  |
|  2 | Buckley RP  |   2017 |     2 |         2 |                161 |                 3 |     7 |                          23 |                      0.429 |
|  3 | Buckley RP  |   2020 |     1 |         3 |                 24 |                 5 |     4 |                           6 |                      1.25  |
|  4 | Barberis JN |   2017 |     2 |         2 |                161 |                 3 |     7 |                          23 |                      0.429 |

>>> print(production_over_time.documents_.head().to_markdown())
|    | authors     | title                                                                 |   year | source_title                                                   |   global_citations |   local_citations | doi                         |
|---:|:------------|:----------------------------------------------------------------------|-------:|:---------------------------------------------------------------|-------------------:|------------------:|:----------------------------|
|  0 | Arner DW    | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                         |
|  1 | Barberis JN | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                         |
|  2 | Buckley RP  | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                         |
|  3 | Butler T    | understanding REGTECH for digital REGULATORY_COMPLIANCE               |   2019 | Palgrave Studies in Digital Business and Enabling Technologies |                 33 |                14 | 10.1007/978-3-030-02330-0_6 |
|  4 | Buckley RP  | the road to REGTECH: the (astonishing) example of the EUROPEAN_UNION  |   2020 | Journal of Banking Regulation                                  |                 24 |                 5 | 10.1057/S41261-019-00104-1  |




"""
from ...vantagepoint.discover import terms_by_year

FIELD = "authors"


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
