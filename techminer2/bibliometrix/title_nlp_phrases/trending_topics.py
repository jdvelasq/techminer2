# flake8: noqa
"""
Trend Topics
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__title_nlp_phrases_trending_topics.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.title_nlp_phrases.trending_topics(
...     root_dir=root_dir, 
... ).table_.head(20)
year                           OCC  year_q1  ...  global_citations  rn
title_nlp_phrases                            ...                      
FINANCIAL_REGULATION             2     2016  ...               180   0
FINANCIAL_SYSTEM                 1     2017  ...                11   0
FINANCIAL_RISK                   1     2018  ...                21   0
REVIEW_ARTICLE                   1     2019  ...                 3   0
FINANCIAL_CRIME                  2     2020  ...                12   0
EUROPEAN_UNION                   1     2020  ...                24   1
EFFECTIVE_SOLUTIONS              1     2020  ...                14   2
REGULATORY_TECHNOLOGY_REGTECH    1     2020  ...                11   3
AML_COMPLIANCE                   1     2020  ...                10   4
REGULATORY_TECHNOLOGY            3     2020  ...                20   0
ARTIFICIAL_INTELLIGENCE          3     2020  ...                17   1
BANK_TREASURY                    1     2021  ...                11   2
DIGITAL_TRANSFORMATION           1     2021  ...                11   3
GDPR_COMPLIANCE_TOOLS            1     2021  ...                 2   4
FINANCIAL_DEVELOPMENT            1     2022  ...                13   0
CHARITABLE_ORGANISATIONS         1     2022  ...                 3   1
FINTECH_SUSTAINABILITY           1     2022  ...                 3   2
MACHINE_LEARNING                 1     2022  ...                 3   3
REGTECH_APPROACH                 1     2022  ...                 3   4
FIRM_PERFORMANCE                 1     2023  ...                 0   0
<BLANKLINE>
[20 rows x 6 columns]





>>> bibliometrix.title_nlp_phrases.trending_topics(
...     root_dir=root_dir,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__title_nlp_phrases_trending_topics.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> bibliometrix.title_nlp_phrases.trending_topics(
...     custom_items=[
...         "FINANCIAL_REGULATION",
...         "REGULATORY_TECHNOLOGY",
...         "FINANCIAL_CRIME",
...         "FINANCIAL_SYSTEM",
...         "ARTIFICIAL_INTELLIGENCE",
...     ], 
...     root_dir=root_dir, 
... ).table_.head(10)
year                     OCC  year_q1  year_med  year_q3  global_citations  rn
title_nlp_phrases                                                             
FINANCIAL_REGULATION       2     2016      2016     2017               180   0
FINANCIAL_SYSTEM           1     2017      2017     2017                11   0
FINANCIAL_CRIME            2     2020      2020     2021                12   0
REGULATORY_TECHNOLOGY      3     2020      2021     2021                20   0
ARTIFICIAL_INTELLIGENCE    3     2020      2021     2022                17   1

# pylint: disable=line-too-long
"""
# from ...vantagepoint.analyze.trending_terms import trending_terms

FIELD = "title_nlp_phrases"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def trending_topics(
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

    return trending_terms(
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
