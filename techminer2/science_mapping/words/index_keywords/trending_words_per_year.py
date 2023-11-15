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

>>> from techminer2.analyze.words import trending_words_per_year
>>> words = trending_words_per_year(
...     #
...     # PARAMS:
...     field="index_keywords",
...     n_words_per_year=5,
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> words.df_.head()
year                                       OCC  year_q1  ...  height  width
index_keywords                                           ...               
ACTOR_NETWORK_THEORY                         1     2016  ...    0.15      1
CONVERGENCE_SERVICES                         1     2016  ...    0.15      1
DISCUSSES_POLICY_IMPLICATIONS                1     2016  ...    0.15      1
HISTORICAL_DEVELOPMENT                       1     2016  ...    0.15      1
INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY    1     2016  ...    0.15      1
<BLANKLINE>
[5 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/analyze/words/index_keywords/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/index_keywords/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
