# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trending Words per Year
===============================================================================

>>> from techminer2.analyze.words import trending_words_per_year
>>> words = trending_words_per_year(
...     #
...     # PARAMS:
...     field="keywords",
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
year                 OCC  year_q1  year_med  ...  rn    height  width
keywords                                     ...                     
RESEARCHERS            1     2016      2016  ...   3  0.150000      1
TERMINOLOGY            1     2016      2016  ...   4  0.150000      1
CONTENT_ANALYSIS       2     2016      2016  ...   1  0.176452      1
POPULAR_PRESS          2     2016      2016  ...   2  0.176452      1
FINANCIAL_INCLUSION    3     2016      2017  ...   3  0.202903      2
<BLANKLINE>
[5 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/analyze/words/keywords/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/keywords/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>

"""
