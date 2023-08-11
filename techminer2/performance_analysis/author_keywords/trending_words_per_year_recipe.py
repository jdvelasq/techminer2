# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Trending Words per Year
===============================================================================

>>> from techminer2.time_analysis import trending_terms_per_year
>>> words = trending_terms_per_year(
...     #
...     # PARAMS:
...     field="author_keywords",
...     n_words_per_year=5,
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> words.df_.head(20)
year                                     OCC  year_q1  ...    height  width
author_keywords                                        ...                 
CORPORATE_SOCIAL_RESPONSIBILITIES (CSR)    1     2017  ...  0.150000      1
CREDIT                                     1     2017  ...  0.150000      1
SMART_CONTRACTS                            2     2017  ...  0.180370      2
BUSINESS_MODELS                            1     2018  ...  0.150000      1
FUTURE_RESEARCH_DIRECTION                  1     2018  ...  0.150000      1
ALGORITHMIC_STANDARDS                      1     2018  ...  0.150000      1
SEMANTIC_TECHNOLOGIES                      2     2018  ...  0.180370      2
SANDBOXES                                  2     2018  ...  0.180370      3
BLOCKCHAIN                                 3     2018  ...  0.210741      3
FINANCIAL_SERVICES                         4     2018  ...  0.241111      3
REGULATION                                 5     2018  ...  0.271481      4
STANDARDS                                  1     2019  ...  0.150000      1
DOGMAS                                     1     2019  ...  0.150000      1
FINTECH                                   12     2019  ...  0.484074      2
FINANCIAL_REGULATION                       4     2019  ...  0.241111      4
REGTECH                                   28     2019  ...  0.970000      4
ARTIFICIAL_INTELLIGENCE                    4     2020  ...  0.241111      1
ANTI_MONEY_LAUNDERING                      5     2020  ...  0.271481      2
DATA_PROTECTION                            2     2020  ...  0.180370      3
INNOVATION                                 3     2020  ...  0.210741      3
<BLANKLINE>
[20 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/performance/author_keywords/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../../_static/performance/author_keywords/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
