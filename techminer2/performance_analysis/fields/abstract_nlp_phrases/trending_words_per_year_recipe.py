# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Trending Words per Year (Recipe)
===============================================================================

>>> from techminer2.performance_analysis import trending_terms_per_year
>>> words = trending_terms_per_year(
...     #
...     # PARAMS:
...     field="abstract_nlp_phrases",
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
year                         OCC  year_q1  year_med  ...  rn   height  width
abstract_nlp_phrases                                 ...                    
ECONOMIC_CONDITIONS            1     2016      2016  ...   0  0.15000      1
DIGITAL_IDENTITY               2     2017      2017  ...   0  0.20125      1
NEW_APPROACH                   2     2017      2017  ...   1  0.20125      1
CONSUMER_PROTECTION            1     2017      2017  ...   2  0.15000      1
MARKET_INTEGRITY               1     2017      2017  ...   3  0.15000      1
REGULATORY_SANDBOXES           1     2017      2017  ...   4  0.15000      1
FINANCIAL_SERVICES_INDUSTRY    5     2017      2018  ...   0  0.35500      6
FINANCIAL_STABILITY            2     2018      2018  ...   1  0.20125      2
OPERATIONAL_RISK               2     2018      2018  ...   2  0.20125      2
ACTION_RESEARCH                1     2018      2018  ...   3  0.15000      1
CURRENT_STATE                  1     2018      2018  ...   4  0.15000      1
FINANCIAL_TECHNOLOGY           5     2018      2019  ...   0  0.35500      4
FINANCIAL_SYSTEM               4     2018      2019  ...   1  0.30375      3
REGULATORY_SYSTEM              2     2018      2019  ...   2  0.20125      3
BLOCKCHAIN_TECHNOLOGY          2     2018      2019  ...   3  0.20125      3
ADDITIONAL_KNOWLEDGE           1     2019      2019  ...   4  0.15000      1
REGULATORY_TECHNOLOGY         17     2020      2020  ...   0  0.97000      3
FINANCIAL_INSTITUTIONS        15     2020      2020  ...   1  0.86750      3
REGULATORY_COMPLIANCE          7     2018      2020  ...   2  0.45750      3
FINANCIAL_REGULATION           6     2018      2020  ...   3  0.40625      4
<BLANKLINE>
[20 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/performance_analysis/fields/abstract_nlp_phrases/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/abstract_nlp_phrases/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
