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


>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix/index_keywords/trending_words_per_year.html"
>>> words = bibliometrix.index_keywords.trending_words_per_year(
...     root_dir=root_dir, 
... )
>>> words.df_.head(20)
year                                        OCC  year_q1  ...  height  width
index_keywords                                            ...               
CUSTOMER_REQUIREMENTS                         1     2017  ...  0.1500      1
ELECTRONIC_DOCUMENT_IDENTIFICATION_SYSTEMS    1     2017  ...  0.1500      1
FINANCIAL_SERVICES                            1     2017  ...  0.1500      1
REAL_TIME_MONITORING                          1     2017  ...  0.1500      1
REGULATORY_REGIME                             1     2017  ...  0.1500      1
REGTECH                                       5     2017  ...  0.5600      6
SANDBOXES                                     2     2018  ...  0.2525      3
BLOCKCHAIN                                    2     2018  ...  0.2525      3
SMART_CONTRACTS                               2     2018  ...  0.2525      3
ADDITIONAL_KNOWLEDGE                          1     2019  ...  0.1500      1
REGULATORY_COMPLIANCE                         9     2020  ...  0.9700      3
FINANCIAL_INSTITUTIONS                        6     2020  ...  0.6625      3
FINTECH                                       3     2020  ...  0.3550      1
INFORMATION_SYSTEMS                           2     2020  ...  0.2525      2
INFORMATION_USE                               2     2020  ...  0.2525      2
FINANCE                                       5     2019  ...  0.5600      4
ANTI_MONEY_LAUNDERING                         3     2020  ...  0.3550      2
LAUNDERING                                    2     2021  ...  0.2525      1
BANKING_INDUSTRY                              1     2021  ...  0.1500      1
COMPLIANCE_COSTS                              1     2021  ...  0.1500      1
<BLANKLINE>
[20 rows x 8 columns]





>>> words.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/bibliometrix/index_keywords/trending_words_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>


"""
FIELD = "index_keywords"


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

    from ...analyze.terms.trending_terms_per_year import (
        trending_terms_per_year as analyze_trending_terms_per_year,
    )

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
