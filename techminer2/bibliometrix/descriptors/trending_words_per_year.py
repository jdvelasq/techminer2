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
>>> file_name = "sphinx/_static/bibliometrix/descriptors/trending_words_per_year.html"
>>> words = bibliometrix.descriptors.trending_words_per_year(
...     root_dir=root_dir, 
... )
>>> words.df_.head(20)
year                         OCC  year_q1  year_med  ...  rn    height  width
descriptors                                          ...                     
ECONOMIC_CONDITIONS            1     2016      2016  ...   0  0.150000      1
DIGITAL_IDENTITY               3     2017      2017  ...   0  0.208571      2
NEW_APPROACH                   2     2017      2017  ...   1  0.179286      1
CONSUMER_PROTECTION            1     2017      2017  ...   2  0.150000      1
MARKET_INTEGRITY               1     2017      2017  ...   3  0.150000      1
CUSTOMER_REQUIREMENTS          1     2017      2017  ...   4  0.150000      1
FINANCIAL_SERVICES_INDUSTRY    5     2017      2018  ...   0  0.267143      6
FINANCIAL_SYSTEM               5     2018      2018  ...   1  0.267143      3
FINANCIAL_STABILITY            2     2018      2018  ...   2  0.179286      2
SEMANTIC_TECHNOLOGIES          2     2018      2018  ...   3  0.179286      2
OPERATIONAL_RISK               2     2018      2018  ...   4  0.179286      2
BLOCKCHAIN                     3     2018      2019  ...   0  0.208571      3
DISRUPTIVE_INNOVATION          2     2018      2019  ...   1  0.179286      3
REGULATORY_SYSTEM              2     2018      2019  ...   2  0.179286      3
BLOCKCHAIN_TECHNOLOGY          2     2018      2019  ...   3  0.179286      3
SANDBOXES                      2     2018      2019  ...   4  0.179286      3
REGTECH                       29     2019      2020  ...   0  0.970000      4
REGULATORY_TECHNOLOGY         20     2020      2020  ...   1  0.706429      3
FINANCIAL_INSTITUTIONS        16     2020      2020  ...   2  0.589286      2
REGULATORY_COMPLIANCE         15     2019      2020  ...   3  0.560000      3
<BLANKLINE>
[20 rows x 8 columns]




>>> words.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/bibliometrix/descriptors/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
FIELD = "descriptors"


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
