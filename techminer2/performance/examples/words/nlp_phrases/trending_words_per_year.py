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
...     field="nlp_phrases",
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
year             OCC  year_q1  year_med  ...  rn  height  width
nlp_phrases                              ...                   
BANK_EXECUTIVES    1     2016      2016  ...   0    0.15      1
BANK_FAILURES      1     2016      2016  ...   1    0.15      1
CLASS_ACTION       1     2016      2016  ...   2    0.15      1
COMPLEX_TASK       1     2016      2016  ...   3    0.15      1
CONCEPT_ARTICLE    1     2016      2016  ...   4    0.15      1
<BLANKLINE>
[5 rows x 8 columns]


>>> words.fig_.write_html("sphinx/_static/performance/words/nlp_phrases/trending_words_per_year.html")

.. raw:: html

    <iframe src="../../../../../../_static/performance/words/nlp_phrases/trending_words_per_year.html" 
    height="900px" width="100%" frameBorder="0"></iframe>


"""
