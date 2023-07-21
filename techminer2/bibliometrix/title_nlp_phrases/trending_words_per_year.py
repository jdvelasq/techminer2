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
>>> file_name = "sphinx/_static/bibliometrix/title_nlp_phrases/trending_words_per_year.html"
>>> words = bibliometrix.title_nlp_phrases.trending_words_per_year(
...     root_dir=root_dir, 
... )
>>> words.df_.head(20)
year                           OCC  year_q1  year_med  ...  rn  height  width
title_nlp_phrases                                      ...                   
FINANCIAL_REGULATION             2     2016      2016  ...   0    0.56      2
FINANCIAL_SYSTEM                 1     2017      2017  ...   0    0.15      1
FINANCIAL_RISK                   1     2018      2018  ...   0    0.15      1
REVIEW_ARTICLE                   1     2019      2019  ...   0    0.15      1
FINANCIAL_CRIME                  2     2020      2020  ...   0    0.56      2
EUROPEAN_UNION                   1     2020      2020  ...   1    0.15      1
EFFECTIVE_SOLUTIONS              1     2020      2020  ...   2    0.15      1
REGULATORY_TECHNOLOGY_REGTECH    1     2020      2020  ...   3    0.15      1
AML_COMPLIANCE                   1     2020      2020  ...   4    0.15      1
REGULATORY_TECHNOLOGY            3     2020      2021  ...   0    0.97      2
ARTIFICIAL_INTELLIGENCE          3     2020      2021  ...   1    0.97      3
BANK_TREASURY                    1     2021      2021  ...   2    0.15      1
DIGITAL_TRANSFORMATION           1     2021      2021  ...   3    0.15      1
GDPR_COMPLIANCE_TOOLS            1     2021      2021  ...   4    0.15      1
FINANCIAL_DEVELOPMENT            1     2022      2022  ...   0    0.15      1
CHARITABLE_ORGANISATIONS         1     2022      2022  ...   1    0.15      1
FINTECH_SUSTAINABILITY           1     2022      2022  ...   2    0.15      1
MACHINE_LEARNING                 1     2022      2022  ...   3    0.15      1
REGTECH                          1     2022      2022  ...   4    0.15      1
FIRM_PERFORMANCE                 1     2023      2023  ...   0    0.15      1
<BLANKLINE>
[20 rows x 8 columns]





>>> words.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/bibliometrix/title_nlp_phrases/trending_words_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>


"""
from ...analyze.terms.trending_terms_per_year import (
    trending_terms_per_year as analyze_trending_terms_per_year,
)

FIELD = "title_nlp_phrases"


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
