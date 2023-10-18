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
...     field="author_keywords",
...     n_words_per_year=5,
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> words.df_.head(20)
year                     OCC  year_q1  year_med  ...  rn    height  width
author_keywords                                  ...                     
RESEARCHERS                1     2016      2016  ...   4  0.150000      1
CONTENT_ANALYSIS           2     2016      2016  ...   2  0.177333      1
POPULAR_PRESS              2     2016      2016  ...   3  0.177333      1
DIGITALIZATION             3     2016      2016  ...   0  0.204667      1
TECHNOLOGIES               2     2016      2016  ...   1  0.177333      2
FINANCIAL_INCLUSION        3     2016      2017  ...   1  0.204667      2
BANKING                    3     2016      2017  ...   2  0.204667      2
INNOVATION                 7     2016      2017  ...   0  0.314000      2
DIGITAL_FINANCE            1     2017      2017  ...   3  0.150000      1
E_FINANCE                  1     2017      2017  ...   4  0.150000      1
FINTECH                   31     2017      2018  ...   0  0.970000      2
BUSINESS                   3     2018      2018  ...   3  0.204667      1
SHADOW_BANKING             3     2018      2018  ...   4  0.204667      1
FINANCIAL_SERVICES         4     2018      2018  ...   1  0.232000      1
BLOCKCHAIN                 3     2018      2019  ...   0  0.204667      2
PEER_TO_PEER_LENDING       3     2018      2019  ...   1  0.204667      2
FINANCIAL_TECHNOLOGY       4     2018      2018  ...   2  0.232000      2
ENTREPRENEURSHIP           1     2019      2019  ...   4  0.150000      1
ARTIFICIAL_INTELLIGENCE    2     2019      2019  ...   2  0.177333      1
ROBOTS                     2     2019      2019  ...   3  0.177333      1
<BLANKLINE>
[20 rows x 8 columns]



>>> words.fig_.write_html("sphinx/_static/analyze/words/author_keywords/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/author_keywords/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
