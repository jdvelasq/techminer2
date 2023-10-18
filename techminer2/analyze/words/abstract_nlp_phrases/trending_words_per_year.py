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
...     field="abstract_nlp_phrases",
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
abstract_nlp_phrases                             ...                     
LONDON_BUSINESS_SCHOOL     1     2015      2015  ...   0  0.150000      1
STATE                      3     2016      2016  ...   0  0.202903      1
YEARS                      3     2016      2016  ...   2  0.202903      1
PRACTICE                   3     2016      2016  ...   1  0.202903      2
DIGITAL_INNOVATION         3     2016      2016  ...   3  0.202903      2
OPPORTUNITIES              3     2016      2016  ...   4  0.202903      2
FINANCE                   13     2016      2017  ...   1  0.467419      3
FIELD                      7     2016      2017  ...   4  0.308710      4
FINANCIAL_SECTOR           9     2017      2017  ...   3  0.361613      2
DEVELOPMENT               11     2017      2017  ...   2  0.414516      2
RESEARCHERS               13     2017      2018  ...   4  0.467419      2
FINANCIAL_INDUSTRY        16     2017      2017  ...   0  0.546774      2
BANKING                   14     2017      2018  ...   3  0.493871      3
AUTHOR                    18     2017      2018  ...   2  0.599677      3
TECHNOLOGIES              23     2017      2018  ...   1  0.731935      3
FINTECH                   32     2017      2018  ...   0  0.970000      3
IMPACT                     6     2018      2019  ...   1  0.282258      2
COUNTRIES                  6     2018      2019  ...   2  0.282258      2
FINANCIAL_TECHNOLOGY      17     2018      2019  ...   0  0.573226      2
ARTIFICIAL_INTELLIGENCE    4     2019      2019  ...   3  0.229355      1
<BLANKLINE>
[20 rows x 8 columns]



>>> words.fig_.write_html("sphinx/_static/analyze/words/abstract_nlp_phrases/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/abstract_nlp_phrases/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
