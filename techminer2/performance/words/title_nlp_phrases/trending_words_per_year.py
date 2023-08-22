# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trending Words per Year
===============================================================================

>>> from techminer2.performance.plots import trending_words_per_year
>>> words = trending_words_per_year(
...     #
...     # PARAMS:
...     field="title_nlp_phrases",
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
year                           OCC  year_q1  year_med  ...  rn  height  width
title_nlp_phrases                                      ...                   
BANK_FAILURES                    1     2016      2016  ...   1    0.15      1
CONCEPT_ARTICLE                  1     2016      2016  ...   2    0.15      1
REALISTIC_PROTECTION             1     2016      2016  ...   3    0.15      1
FINANCIAL_REGULATION             2     2016      2016  ...   0    0.56      2
FINANCIAL_SYSTEM                 1     2017      2017  ...   0    0.15      1
REGTECH_EVOLUTION                1     2017      2017  ...   1    0.15      1
REGULATORY_CRISIS                1     2017      2017  ...   2    0.15      1
FINANCIAL_RISK                   1     2018      2018  ...   0    0.15      1
INNOVATIVE_REGTECH_APPROACH      1     2018      2018  ...   1    0.15      1
DIGITAL_REGULATORY_COMPLIANCE    1     2019      2019  ...   0    0.15      1
UNDERSTANDING_REGTECH            1     2019      2019  ...   1    0.15      1
CORPORATE_EMAILS                 1     2019      2019  ...   2    0.15      1
LINGUISTIC_ANALYSIS              1     2019      2019  ...   3    0.15      1
ZERO_REVELATION_REGTECH          1     2019      2019  ...   4    0.15      1
EUROPEAN_UNION                   1     2020      2020  ...   1    0.15      1
EFFECTIVE_SOLUTIONS              1     2020      2020  ...   2    0.15      1
GDPR_REGTECH                     1     2020      2020  ...   3    0.15      1
REGULATORY_TECHNOLOGY_REGTECH    1     2020      2020  ...   4    0.15      1
FINANCIAL_CRIME                  2     2020      2020  ...   0    0.56      2
REGULATORY_TECHNOLOGY            3     2020      2021  ...   0    0.97      2
<BLANKLINE>
[20 rows x 8 columns]

>>> words.fig_.write_html("sphinx/_static/performance/words/title_nlp_phrases/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../../_static/performance/words/title_nlp_phrases/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
