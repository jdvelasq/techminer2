# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trending Words per Year
===============================================================================


>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix/keywords/trending_words_per_year.html"
>>> words = bibliometrix.keywords.trending_words_per_year(
...     root_dir=root_dir, 
... )
>>> words.df_.head(20)
year                                        OCC  year_q1  ...    height  width
keywords                                                  ...                 
CUSTOMER_REQUIREMENTS                         1     2017  ...  0.150000      1
ELECTRONIC_DOCUMENT_IDENTIFICATION_SYSTEMS    1     2017  ...  0.150000      1
REAL_TIME_MONITORING                          1     2017  ...  0.150000      1
REGULATORY_REGIME                             1     2017  ...  0.150000      1
CORPORATE_SOCIAL_RESPONSIBILITIES (CSR)       1     2017  ...  0.150000      1
SMART_CONTRACTS                               3     2018  ...  0.210741      3
SEMANTIC_TECHNOLOGIES                         2     2018  ...  0.180370      2
BUSINESS_MODELS                               1     2018  ...  0.150000      1
FUTURE_RESEARCH_DIRECTION                     1     2018  ...  0.150000      1
ALGORITHMIC_STANDARDS                         1     2018  ...  0.150000      1
FINANCIAL_SERVICES                            4     2018  ...  0.241111      3
BLOCKCHAIN                                    3     2018  ...  0.210741      3
SANDBOXES                                     2     2018  ...  0.180370      3
STANDARDS                                     1     2019  ...  0.150000      1
DOGMAS                                        1     2019  ...  0.150000      1
REGTECH                                      28     2019  ...  0.970000      4
FINTECH                                      12     2019  ...  0.484074      2
REGULATORY_COMPLIANCE                         9     2020  ...  0.392963      3
COMPLIANCE                                    7     2020  ...  0.332222      3
ANTI_MONEY_LAUNDERING                         6     2020  ...  0.301852      2
<BLANKLINE>
[20 rows x 8 columns]





>>> words.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/bibliometrix/keywords/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
from ..trending_terms_per_year import trending_terms_per_year as analyze_trending_terms_per_year

FIELD = "keywords"


def trending_words_per_year(
    #
    # PARAMS:
    n_words_per_year=5,
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Trend topics"""

    return analyze_trending_terms_per_year(
        #
        # PARAMS:
        field=FIELD,
        n_words_per_year=n_words_per_year,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
