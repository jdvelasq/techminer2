# flake8: noqa
"""
Trending Words per Year
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/report/nlp_phrases/trending_words_per_year.html"

>>> import techminer2plus
>>> techminer2plus.report.nlp_phrases.trending_words_per_year(
...     root_dir=root_dir, 
... ).table_.head(20)
year                         OCC  year_q1  ...  global_citations  rn
nlp_phrases                                ...                      
ECONOMIC_CONDITIONS            1     2016  ...                30   0
DIGITAL_IDENTITY               2     2017  ...               161   0
NEW_APPROACH                   2     2017  ...               161   1
CONSUMER_PROTECTION            1     2017  ...               150   2
MARKET_INTEGRITY               1     2017  ...               150   3
REGULATORY_SANDBOXES           1     2017  ...                11   4
FINANCIAL_SERVICES_INDUSTRY    5     2017  ...               315   0
FINANCIAL_SYSTEM               5     2018  ...               189   1
FINANCIAL_STABILITY            2     2018  ...               154   2
OPERATIONAL_RISK               2     2018  ...                21   3
ACTION_RESEARCH                1     2018  ...               153   4
FINANCIAL_REGULATION           7     2018  ...               360   0
FINANCIAL_TECHNOLOGY           5     2018  ...               173   1
REGULATORY_SYSTEM              2     2018  ...               154   2
BLOCKCHAIN_TECHNOLOGY          2     2018  ...                21   3
ADDITIONAL_KNOWLEDGE           1     2019  ...                 3   4
REGULATORY_TECHNOLOGY         18     2020  ...               273   0
FINANCIAL_INSTITUTIONS        15     2020  ...               194   1
REGULATORY_COMPLIANCE          7     2018  ...               198   2
FINANCIAL_CRISIS               6     2018  ...                58   3
<BLANKLINE>
[20 rows x 6 columns]


>>> techminer2plus.report.nlp_phrases.trending_words_per_year(
...     root_dir=root_dir,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/report/nlp_phrases/trending_words_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> techminer2plus.report.nlp_phrases.trending_words_per_year(
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
nlp_phrases                                                                   
FINANCIAL_SYSTEM           5     2018      2018     2020               189   0
FINANCIAL_REGULATION       7     2018      2019     2021               360   0
REGULATORY_TECHNOLOGY     18     2020      2020     2022               273   0
FINANCIAL_CRIME            2     2020      2020     2021                12   1
ARTIFICIAL_INTELLIGENCE    7     2020      2021     2022                33   0

# pylint: disable=line-too-long
"""
from ...analyze import (
    trending_terms_per_year as analyze_trending_terms_per_year,
)

FIELD = "nlp_phrases"


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
