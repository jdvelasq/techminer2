# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _performance_analysis.organizations.production_over_time:

Production over Time
===============================================================================


>>> from techminer2.analyze import terms_by_year
>>> terms = terms_by_year(
...     #
...     # PARAMS:
...     field="organizations",
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
>>> terms.fig_.write_html("sphinx/_static/analyze/contributors/organizations/production_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(terms.df_.to_markdown())
| organizations                                               |   2015 |   2016 |   2017 |   2018 |   2019 |
|:------------------------------------------------------------|-------:|-------:|-------:|-------:|-------:|
| Univ. of Zurich (CHE) 3:434                                 |      0 |      2 |      1 |      0 |      0 |
| Federal Reserve Bank of Philadelphia (USA) 3:317            |      0 |      0 |      0 |      2 |      1 |
| Baylor Univ. (USA) 2:395                                    |      0 |      0 |      0 |      0 |      2 |
| Max Planck Inst. for Innovation and Competition (DEU) 2:358 |      0 |      0 |      1 |      0 |      1 |
| Univ. of New South Wales (AUS) 2:340                        |      0 |      0 |      1 |      0 |      1 |
| Pace Univ. (USA) 2:323                                      |      0 |      0 |      1 |      1 |      0 |
| Sungkyunkwan Univ. (KOR) 2:307                              |      0 |      1 |      0 |      1 |      0 |
| Univ. of Sydney (AUS) 2:300                                 |      0 |      0 |      1 |      1 |      0 |
| Federal Reserve Bank of Chicago (USA) 2:253                 |      0 |      0 |      0 |      1 |      1 |
| Univ. of Latvia (LVA) 2:163                                 |      0 |      1 |      1 |      0 |      0 |

    

>>> print(terms.prompt_) # doctest: +ELLIPSIS
Your task is ...


>>> print(terms.metrics_.head().to_markdown())
|    | organizations                              |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:-------------------------------------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | Univ. of Zurich (CHE)                      |   2016 |     2 |         2 |                181 |                 3 |     4 |                      45.25  |                      0.75  |
|  1 | Univ. of Zurich (CHE)                      |   2017 |     1 |         3 |                253 |                 1 |     3 |                      84.333 |                      0.333 |
|  2 | Federal Reserve Bank of Philadelphia (USA) |   2018 |     2 |         2 |                220 |                 2 |     2 |                     110     |                      1     |
|  3 | Federal Reserve Bank of Philadelphia (USA) |   2019 |     1 |         3 |                 97 |                 0 |     1 |                      97     |                      0     |
|  4 | Baylor Univ. (USA)                         |   2019 |     2 |         2 |                395 |                 0 |     1 |                     395     |                      0     |


>>> print(terms.documents_.head().to_markdown())
|    | organizations                                         | document_title                                                                      |   year | source_title                                    |   global_citations |   local_citations | doi                             |
|---:|:------------------------------------------------------|:------------------------------------------------------------------------------------|-------:|:------------------------------------------------|-------------------:|------------------:|:--------------------------------|
|  0 | Max Planck Inst. for Innovation and Competition (DEU) | the EMERGENCE of the GLOBAL_FINTECH_MARKET: economic and TECHNOLOGICAL_DETERMINANTS |   2019 | Small Business Economics                        |                258 |                 1 | 10.1007/S11187-018-9991-X       |
|  1 | Univ. of Zurich (CHE)                                 | FINTECH                                                                             |   2017 | Business and Information Systems Engineering    |                253 |                 1 | 10.1007/S12599-017-0464-6       |
|  2 | Pace Univ. (USA)                                      | a SURVEY on FINTECH                                                                 |   2018 | Journal of Network and Computer Applications    |                238 |                 1 | 10.1016/J.JNCA.2017.10.011      |
|  3 | Baylor Univ. (USA)                                    | how valuable is FINTECH_INNOVATION?                                                 |   2019 | Review of Financial Studies                     |                235 |                 0 | 10.1093/RFS/HHY130              |
|  4 | Univ. of New South Wales (AUS)                        | nurturing a FINTECH_ECOSYSTEM: the CASE of a YOUTH_MICROLOAN_STARTUP in CHINA       |   2017 | International Journal of Information Management |                180 |                 2 | 10.1016/J.IJINFOMGT.2016.11.006 |




"""
