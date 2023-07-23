# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Production over Time (Recipe)
===============================================================================


>>> from techminer2.performance_analysis import terms_by_year
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> terms.fig_.write_html("sphinx/_static/performance_analysis/fields/countries/production_over_time.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/countries/production_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> print(terms.df_.to_markdown())
| countries            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| United Kingdom 7:199 |      0 |      0 |      3 |      1 |      2 |      0 |      1 |      0 |
| Australia 7:199      |      0 |      2 |      0 |      0 |      3 |      2 |      0 |      0 |
| United States 6:059  |      1 |      0 |      1 |      2 |      0 |      0 |      1 |      1 |
| Ireland 5:055        |      0 |      0 |      1 |      1 |      1 |      1 |      1 |      0 |
| China 5:027          |      0 |      1 |      0 |      0 |      0 |      0 |      3 |      1 |
| Italy 5:005          |      0 |      0 |      0 |      1 |      1 |      1 |      1 |      1 |
| Germany 4:051        |      0 |      0 |      1 |      0 |      2 |      0 |      1 |      0 |
| Switzerland 4:045    |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      1 |
| Bahrain 4:019        |      0 |      0 |      0 |      0 |      1 |      2 |      1 |      0 |
| Hong Kong 3:185      |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |



>>> print(terms.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'countries' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| countries            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| United Kingdom 7:199 |      0 |      0 |      3 |      1 |      2 |      0 |      1 |      0 |
| Australia 7:199      |      0 |      2 |      0 |      0 |      3 |      2 |      0 |      0 |
| United States 6:059  |      1 |      0 |      1 |      2 |      0 |      0 |      1 |      1 |
| Ireland 5:055        |      0 |      0 |      1 |      1 |      1 |      1 |      1 |      0 |
| China 5:027          |      0 |      1 |      0 |      0 |      0 |      0 |      3 |      1 |
| Italy 5:005          |      0 |      0 |      0 |      1 |      1 |      1 |      1 |      1 |
| Germany 4:051        |      0 |      0 |      1 |      0 |      2 |      0 |      1 |      0 |
| Switzerland 4:045    |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      1 |
| Bahrain 4:019        |      0 |      0 |      0 |      0 |      1 |      2 |      1 |      0 |
| Hong Kong 3:185      |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
```
<BLANKLINE>



>>> print(terms.metrics_.head().to_markdown())
|    | countries      |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:---------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | United Kingdom |   2018 |     3 |         3 |                182 |                30 |     6 |                      30.333 |                      5     |
|  1 | United Kingdom |   2019 |     1 |         4 |                  0 |                 0 |     5 |                       0     |                      0     |
|  2 | United Kingdom |   2020 |     2 |         6 |                 14 |                 3 |     4 |                       3.5   |                      0.75  |
|  3 | United Kingdom |   2022 |     1 |         7 |                  3 |                 1 |     2 |                       1.5   |                      0.5   |
|  4 | Australia      |   2017 |     2 |         2 |                161 |                 3 |     7 |                      23     |                      0.429 |

    
>>> print(terms.documents_.head().to_markdown())
|    | countries      | title                                                                                                             |   year | source_title                                                   |   global_citations |   local_citations | doi                            |
|---:|:---------------|:------------------------------------------------------------------------------------------------------------------|-------:|:---------------------------------------------------------------|-------------------:|------------------:|:-------------------------------|
|  0 | United Kingdom | FINTECH and REGTECH: impact on regulators and BANKS                                                               |   2018 | Journal of Economics and Business                              |                153 |                17 | 10.1016/J.JECONBUS.2018.07.003 |
|  1 | Australia      | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION                                             |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                            |
|  2 | Hong Kong      | FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION                                             |   2017 | Northwestern Journal of International Law and Business         |                150 |                 0 | nan                            |
|  3 | Ireland        | understanding REGTECH for digital REGULATORY_COMPLIANCE                                                           |   2019 | Palgrave Studies in Digital Business and Enabling Technologies |                 33 |                14 | 10.1007/978-3-030-02330-0_6    |
|  4 | United States  | adaptive FINANCIAL_REGULATION and REGTECH: a concept ARTICLE on realistic protection for victims of BANK failures |   2016 | Duke Law Journal                                               |                 30 |                 0 | nan                            |




"""
