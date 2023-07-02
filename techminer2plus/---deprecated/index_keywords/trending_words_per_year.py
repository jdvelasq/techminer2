# flake8: noqa
"""
Trending Words per Year
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/index_keywords/trending_words_per_year.html"

>>> import techminer2plus
>>> techminer2plus.publish.index_keywords.trending_words_per_year(
...     root_dir=root_dir, 
... ).table_.head(20)
year                                        OCC  year_q1  ...  global_citations  rn
index_keywords                                            ...                      
CUSTOMER_REQUIREMENTS                         1     2017  ...                11   0
ELECTRONIC_DOCUMENT_IDENTIFICATION_SYSTEMS    1     2017  ...                11   1
FINANCIAL_SERVICES                            1     2017  ...                11   2
REAL_TIME_MONITORING                          1     2017  ...                11   3
REGULATORY_REGIME                             1     2017  ...                11   4
REGTECH                                       5     2017  ...                15   0
SANDBOXES                                     2     2018  ...                12   1
BLOCKCHAIN                                    2     2018  ...                 2   2
SMART_CONTRACTS                               2     2018  ...                 2   3
ADDITIONAL_KNOWLEDGE                          1     2019  ...                 3   4
REGULATORY_COMPLIANCE                         9     2020  ...                34   0
FINANCIAL_INSTITUTIONS                        6     2020  ...                 9   1
FINTECH                                       3     2020  ...                 8   2
INFORMATION_SYSTEMS                           2     2020  ...                14   3
INFORMATION_USE                               2     2020  ...                14   4
FINANCE                                       5     2019  ...                16   0
ANTI_MONEY_LAUNDERING                         3     2020  ...                10   1
LAUNDERING                                    2     2021  ...                 9   2
BANKING_INDUSTRY                              1     2021  ...                 7   3
COMPLIANCE_COSTS                              1     2021  ...                 7   4
<BLANKLINE>
[20 rows x 6 columns]





>>> techminer2plus.publish.index_keywords.trending_words_per_year(
...     root_dir=root_dir,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/examples/index_keywords/trending_words_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> techminer2plus.publish.index_keywords.trending_words_per_year(
...     custom_items=[
...         "FINTECH",
...         "REGULATORY_TECHNOLOGY",
...         "BLOCKCHAIN",
...         "REGULATORY_COMPLIANCE",
...         "ARTIFICIAL_INTELLIGENCE",
...     ], 
...     root_dir=root_dir, 
... ).table_.head(10)
year                     OCC  year_q1  year_med  year_q3  global_citations  rn
index_keywords                                                                
BLOCKCHAIN                 2     2018      2019     2020                 2   0
REGULATORY_COMPLIANCE      9     2020      2020     2022                34   0
FINTECH                    3     2020      2020     2020                 8   1
ARTIFICIAL_INTELLIGENCE    2     2021      2022     2022                 2   0
REGULATORY_TECHNOLOGY      2     2022      2022     2023                 1   1





# pylint: disable=line-too-long
"""
# from ...analyze import (
#     trending_terms_per_year as analyze_trending_terms_per_year,
# )

FIELD = "index_keywords"


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
