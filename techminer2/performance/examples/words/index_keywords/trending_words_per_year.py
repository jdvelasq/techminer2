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
...     field="index_keywords",
...     n_words_per_year=5,
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> words.df_.head()
year                                        OCC  year_q1  ...  height  width
index_keywords                                            ...               
CUSTOMER_REQUIREMENTS                         1     2017  ...    0.15      1
ELECTRONIC_DOCUMENT_IDENTIFICATION_SYSTEMS    1     2017  ...    0.15      1
FINANCIAL_SERVICES                            1     2017  ...    0.15      1
REAL_TIME_MONITORING                          1     2017  ...    0.15      1
REGULATORY_REGIME                             1     2017  ...    0.15      1
<BLANKLINE>
[5 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/performance/words/index_keywords/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../../_static/performance/words/index_keywords/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
