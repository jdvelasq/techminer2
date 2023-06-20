# flake8: noqa
"""
Trending Words per Year
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/report/author_keywords/trending_words_per_year.html"

>>> import techminer2plus
>>> techminer2plus.report.author_keywords.trending_words_per_year(
...     root_dir=root_dir, 
... ).table_.head(20)
year                                     OCC  year_q1  ...  global_citations  rn
author_keywords                                        ...                      
CORPORATE_SOCIAL_RESPONSIBILITIES (CSR)    1     2017  ...                 1   0
CREDIT                                     1     2017  ...                 1   1
SEMANTIC_TECHNOLOGIES                      2     2018  ...                41   0
SMART_CONTRACTS                            2     2017  ...                22   1
BUSINESS_MODELS                            1     2018  ...               153   2
FUTURE_RESEARCH_DIRECTION                  1     2018  ...               153   3
ALGORITHMIC_STANDARDS                      1     2018  ...                21   4
FINANCIAL_SERVICES                         4     2018  ...               168   0
BLOCKCHAIN                                 3     2018  ...                 5   1
SANDBOXES                                  2     2018  ...                12   2
STANDARDS                                  1     2019  ...                33   3
DOGMAS                                     1     2019  ...                 5   4
REGTECH                                   28     2019  ...               329   0
FINTECH                                   12     2019  ...               249   1
COMPLIANCE                                 7     2020  ...                30   2
REGULATION                                 5     2018  ...               164   3
ARTIFICIAL_INTELLIGENCE                    4     2020  ...                23   4
REGULATORY_TECHNOLOGY                      7     2020  ...                37   0
ANTI_MONEY_LAUNDERING                      5     2020  ...                34   1
FINANCIAL_REGULATION                       4     2019  ...                35   2
<BLANKLINE>
[20 rows x 6 columns]






>>> techminer2plus.report.author_keywords.trending_words_per_year(
...     root_dir=root_dir,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/report/author_keywords/trending_words_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> techminer2plus.report.author_keywords.trending_words_per_year(
...     custom_items=[
...         "FINTECH",
...         "REGULATORY_TECHNOLOGY",
...         "BLOCKCHAIN",
...         "SUPTECH",
...         "ARTIFICIAL_INTELLIGENCE",
...     ], 
...     root_dir=root_dir, 
... ).table_.head(10)
year                     OCC  year_q1  year_med  year_q3  global_citations  rn
author_keywords                                                               
BLOCKCHAIN                 3     2018      2019     2020                 5   0
FINTECH                   12     2019      2020     2020               249   0
ARTIFICIAL_INTELLIGENCE    4     2020      2020     2020                23   1
REGULATORY_TECHNOLOGY      7     2020      2021     2022                37   0
SUPTECH                    3     2020      2022     2022                 4   0



# pylint: disable=line-too-long
"""
from ...analyze import (
    trending_terms_per_year as analyze_trending_terms_per_year,
)

FIELD = "author_keywords"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def trending_words_per_year(
    # Parameters:
    n_words_per_year=5,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Trend topics"""

    return analyze_trending_terms_per_year(
        field=FIELD,
        n_words_per_year=n_words_per_year,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
