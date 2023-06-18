# flake8: noqa
"""
Trend Topics
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__key_concepts_trending_topics.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.key_concepts.trending_topics(
...     root_dir=root_dir, 
... ).table_.head(20)
year                         OCC  year_q1  ...  global_citations  rn
key_concepts                               ...                      
ECONOMIC_CONDITIONS            1     2016  ...                30   0
DIGITAL_IDENTITY               3     2017  ...               185   0
NEW_APPROACH                   2     2017  ...               161   1
CONSUMER_PROTECTION            1     2017  ...               150   2
MARKET_INTEGRITY               1     2017  ...               150   3
CUSTOMER_REQUIREMENTS          1     2017  ...                11   4
FINANCIAL_SERVICES_INDUSTRY    5     2017  ...               315   0
FINANCIAL_SYSTEM               5     2018  ...               189   1
SMART_CONTRACTS                3     2018  ...                23   2
FINANCIAL_STABILITY            2     2018  ...               154   3
OPERATIONAL_RISK               2     2018  ...                21   4
BLOCKCHAIN                     3     2018  ...                 5   0
REGULATORY_SYSTEM              2     2018  ...               154   1
BLOCKCHAIN_TECHNOLOGY          2     2018  ...                21   2
SANDBOXES                      2     2018  ...                12   3
SMART_CONTRACT                 2     2018  ...                 2   4
REGTECH                       28     2019  ...               329   0
REGULATORY_TECHNOLOGY         20     2020  ...               274   1
REGULATORY_COMPLIANCE         15     2019  ...               232   2
FINANCIAL_INSTITUTIONS        15     2020  ...               194   3
<BLANKLINE>
[20 rows x 6 columns]


>>> bibliometrix.key_concepts.trending_topics(
...     root_dir=root_dir,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__key_concepts_trending_topics.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> bibliometrix.key_concepts.trending_topics(
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
key_concepts                                                                  
FINANCIAL_SYSTEM           5     2018      2018     2020               189   0
REGULATORY_TECHNOLOGY     20     2020      2020     2022               274   0
FINANCIAL_REGULATION      12     2018      2020     2022               395   1
ARTIFICIAL_INTELLIGENCE    8     2020      2020     2022                36   2
FINANCIAL_CRIME            2     2020      2020     2021                12   3


# pylint: disable=line-too-long
"""
# from ...vantagepoint.analyze.trending_terms import trending_terms

FIELD = "key_concepts"


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
