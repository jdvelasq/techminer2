# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trending Words per Year
===============================================================================

>>> from techminer2.time_analysis import trending_terms_per_year
>>> words = trending_terms_per_year(
...     #
...     # PARAMS:
...     field="nlp_phrases",
...     n_words_per_year=5,
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> words.df_.head(20)
year                         OCC  year_q1  year_med  ...  rn    height  width
nlp_phrases                                          ...                     
ECONOMIC_CONDITIONS            1     2016      2016  ...   0  0.150000      1
CONSUMER_PROTECTION            1     2017      2017  ...   2  0.150000      1
MARKET_INTEGRITY               1     2017      2017  ...   3  0.150000      1
REGULATORY_SANDBOXES           1     2017      2017  ...   4  0.150000      1
DIGITAL_IDENTITY               2     2017      2017  ...   0  0.198235      1
NEW_APPROACH                   2     2017      2017  ...   1  0.198235      1
INFORMATION_TECHNOLOGY         5     2017      2020  ...   4  0.342941      5
FINANCIAL_SERVICES_INDUSTRY    5     2017      2018  ...   0  0.342941      6
ACTION_RESEARCH                1     2018      2018  ...   4  0.150000      1
FINANCIAL_STABILITY            2     2018      2018  ...   2  0.198235      2
OPERATIONAL_RISK               2     2018      2018  ...   3  0.198235      2
REGULATORY_SYSTEM              2     2018      2019  ...   2  0.198235      3
BLOCKCHAIN_TECHNOLOGY          2     2018      2019  ...   3  0.198235      3
FINANCIAL_SYSTEM               5     2018      2018  ...   1  0.342941      3
REGULATORY_COMPLIANCE          7     2018      2020  ...   2  0.439412      3
FINANCIAL_TECHNOLOGY           5     2018      2019  ...   1  0.342941      4
FINANCIAL_CRISIS               6     2018      2020  ...   3  0.391176      4
FINANCIAL_REGULATION           7     2018      2019  ...   0  0.439412      4
ADDITIONAL_KNOWLEDGE           1     2019      2019  ...   4  0.150000      1
GLOBAL_FINANCIAL_CRISIS        6     2019      2021  ...   2  0.391176      4
<BLANKLINE>
[20 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/performance/nlp_phrases/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../../_static/performance/nlp_phrases/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""