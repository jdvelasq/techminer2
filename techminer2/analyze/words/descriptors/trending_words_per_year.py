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
...     field="descriptors",
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
year                    OCC  year_q1  year_med  ...  rn    height  width
descriptors                                     ...                     
LONDON_BUSINESS_SCHOOL    1     2015      2015  ...   0  0.150000      1
STATE                     3     2016      2016  ...   1  0.187273      1
YEARS                     3     2016      2016  ...   3  0.187273      1
PRACTICE                  3     2016      2016  ...   2  0.187273      2
DIGITAL_INNOVATION        3     2016      2016  ...   4  0.187273      2
INFORMATION_SYSTEMS       4     2016      2016  ...   0  0.205909      3
FINANCIAL_INNOVATION      8     2016      2017  ...   3  0.280455      3
FIELD                     7     2016      2017  ...   4  0.261818      4
FINANCIAL_SECTOR          9     2017      2017  ...   2  0.299091      2
DEVELOPMENT              11     2017      2017  ...   1  0.336364      2
FINANCIAL_INDUSTRY       18     2017      2017  ...   0  0.466818      2
INNOVATION               20     2017      2018  ...   3  0.504091      2
FINANCE                  22     2017      2018  ...   2  0.541364      2
TECHNOLOGIES             26     2017      2018  ...   1  0.615909      3
FINTECH                  45     2017      2018  ...   0  0.970000      3
BLOCKCHAIN                5     2018      2019  ...   3  0.224545      2
COUNTRIES                 6     2018      2019  ...   2  0.243182      2
ROLE                      7     2018      2019  ...   1  0.261818      2
IMPACT                    9     2018      2019  ...   0  0.299091      2
FINANCIAL_TECHNOLOGY     19     2018      2018  ...   4  0.485455      2
<BLANKLINE>
[20 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/analyze/words/descriptors/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/descriptors/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
