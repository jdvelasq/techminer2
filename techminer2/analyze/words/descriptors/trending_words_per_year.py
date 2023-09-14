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

>>> from techminer2.performance.plots import trending_words_per_year
>>> words = trending_words_per_year(
...     #
...     # PARAMS:
...     field="descriptors",
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
descriptors                                          ...                     
BANK_EXECUTIVES                1     2016      2016  ...   0  0.150000      1
BANK_FAILURES                  1     2016      2016  ...   1  0.150000      1
CLASS_ACTION                   1     2016      2016  ...   2  0.150000      1
COMPLEX_TASK                   1     2016      2016  ...   3  0.150000      1
CONCEPT_ARTICLE                1     2016      2016  ...   4  0.150000      1
ADDRESSES_RISK                 2     2017      2017  ...   2  0.179286      1
ANALOGUE_PROCESSES             2     2017      2017  ...   3  0.179286      1
COMPLIANCE_PROCESSES           2     2017      2017  ...   4  0.179286      1
DIGITAL_IDENTITY               3     2017      2017  ...   0  0.208571      2
NEW_APPROACH                   3     2017      2017  ...   1  0.208571      4
FINANCIAL_SERVICES_INDUSTRY    5     2017      2018  ...   0  0.267143      6
PRACTICAL_IMPLICATIONS         2     2018      2018  ...   1  0.179286      1
FUTURE_AREAS                   2     2018      2018  ...   2  0.179286      2
FINANCIAL_STABILITY            2     2018      2018  ...   3  0.179286      2
SEMANTIC_TECHNOLOGIES          2     2018      2018  ...   4  0.179286      2
DISRUPTIVE_INNOVATION          2     2018      2019  ...   3  0.179286      3
TECHNOLOGY_POSES               2     2018      2019  ...   4  0.179286      3
BLOCKCHAIN                     3     2018      2019  ...   2  0.208571      3
FINANCIAL_SYSTEM               8     2018      2019  ...   0  0.355000      5
FINANCIAL_REGULATION          12     2018      2020  ...   4  0.472143      5
<BLANKLINE>
[20 rows x 8 columns]

>>> words.fig_.write_html("sphinx/_static/performance/words/descriptors/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/words/descriptors/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
