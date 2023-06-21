# flake8: noqa
"""
Trending Words per Year
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/descriptors/trending_words_per_year.html"

>>> import techminer2plus
>>> techminer2plus.examples.descriptors.trending_words_per_year(
...     root_dir=root_dir, 
... ).table_.head(20)
year                         OCC  year_q1  ...  global_citations  rn
descriptors                                ...                      
ECONOMIC_CONDITIONS            1     2016  ...                30   0
DIGITAL_IDENTITY               3     2017  ...               185   0
NEW_APPROACH                   2     2017  ...               161   1
CONSUMER_PROTECTION            1     2017  ...               150   2
MARKET_INTEGRITY               1     2017  ...               150   3
CUSTOMER_REQUIREMENTS          1     2017  ...                11   4
FINANCIAL_SERVICES_INDUSTRY    5     2017  ...               315   0
FINANCIAL_SYSTEM               5     2018  ...               189   1
FINANCIAL_STABILITY            2     2018  ...               154   2
SEMANTIC_TECHNOLOGIES          2     2018  ...                41   3
OPERATIONAL_RISK               2     2018  ...                21   4
BLOCKCHAIN                     3     2018  ...                 5   0
DISRUPTIVE_INNOVATION          2     2018  ...               154   1
REGULATORY_SYSTEM              2     2018  ...               154   2
BLOCKCHAIN_TECHNOLOGY          2     2018  ...                21   3
SANDBOXES                      2     2018  ...                12   4
REGTECH                       29     2019  ...               330   0
REGULATORY_TECHNOLOGY         20     2020  ...               274   1
FINANCIAL_INSTITUTIONS        16     2020  ...               198   2
REGULATORY_COMPLIANCE         15     2019  ...               232   3
<BLANKLINE>
[20 rows x 6 columns]


>>> techminer2plus.examples.descriptors.trending_words_per_year(
...     root_dir=root_dir,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/examples/descriptors/trending_words_per_year.html" height="900px" width="100%" frameBorder="0"></iframe>



>>> techminer2plus.examples.descriptors.trending_words_per_year(
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
descriptors                                                                   
FINANCIAL_SYSTEM           5     2018      2018     2020               189   0
REGULATORY_TECHNOLOGY     20     2020      2020     2022               274   0
FINANCIAL_REGULATION      12     2018      2020     2022               395   1
ARTIFICIAL_INTELLIGENCE    8     2020      2020     2022                36   2
FINANCIAL_CRIME            2     2020      2020     2021                12   3


# pylint: disable=line-too-long
"""
from ...analyze import (
    trending_terms_per_year as analyze_trending_terms_per_year,
)

FIELD = "descriptors"


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
