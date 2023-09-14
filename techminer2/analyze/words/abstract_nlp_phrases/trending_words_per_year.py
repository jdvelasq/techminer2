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
year                         OCC  year_q1  year_med  ...  rn    height  width
abstract_nlp_phrases                                 ...                     
BANK_EXECUTIVES                1     2016      2016  ...   0  0.150000      1
CLASS_ACTION                   1     2016      2016  ...   1  0.150000      1
COMPLEX_TASK                   1     2016      2016  ...   2  0.150000      1
ECONOMIC_CONDITIONS            1     2016      2016  ...   3  0.150000      1
FOCUS_REGULATORY_DISCRETION    1     2016      2016  ...   4  0.150000      1
ADDRESSES_RISK                 2     2017      2017  ...   1  0.195556      1
ANALOGUE_PROCESSES             2     2017      2017  ...   2  0.195556      1
COMPLIANCE_PROCESSES           2     2017      2017  ...   3  0.195556      1
DIGITAL_IDENTITY               2     2017      2017  ...   4  0.195556      1
NEW_APPROACH                   3     2017      2017  ...   0  0.241111      4
FINANCIAL_SERVICES_INDUSTRY    5     2017      2018  ...   0  0.332222      6
PRACTICAL_IMPLICATIONS         2     2018      2018  ...   1  0.195556      1
FUTURE_AREAS                   2     2018      2018  ...   2  0.195556      2
FINANCIAL_STABILITY            2     2018      2018  ...   3  0.195556      2
OPERATIONAL_RISK               2     2018      2018  ...   4  0.195556      2
TECHNOLOGY_POSES               2     2018      2019  ...   2  0.195556      3
CURRENT_RESEARCH               2     2018      2019  ...   3  0.195556      3
REGULATORY_COMPLIANCE          7     2018      2020  ...   2  0.423333      3
FINANCIAL_TECHNOLOGY           5     2018      2019  ...   1  0.332222      4
FINANCIAL_REGULATION           6     2018      2020  ...   3  0.377778      4
<BLANKLINE>
[20 rows x 8 columns]




>>> words.fig_.write_html("sphinx/_static/performance/words/abstract_nlp_phrases/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/words/abstract_nlp_phrases/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
