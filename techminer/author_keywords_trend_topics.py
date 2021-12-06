"""
Author keywords trend topics
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/author_keywords_trend_topics.png"
>>> author_keywords_trend_topics(directory=directory).savefig(file_name)

.. image:: images/author_keywords_trend_topics.png
    :width: 650px
    :align: center

>>> author_keywords_trend_topics(directory=directory, plot=False).head()
pub_year                num_documents  year_q1  ...  global_citations  rn
author_keywords                                 ...                      
fintech                           139     2016  ...              1285   0
financial technologies             28     2016  ...               225   1
innovation                         13     2016  ...               249   2
bank                               13     2016  ...               193   3
financial service                  11     2016  ...               300   4
<BLANKLINE>
[5 rows x 6 columns]

"""

from .keywords_trend_topics import keywords_trend_topics


def author_keywords_trend_topics(
    n_keywords_per_year=5,
    directory="./",
    plot=True,
    figsize=(6, 6),
):
    return keywords_trend_topics(
        column="author_keywords",
        n_keywords_per_year=n_keywords_per_year,
        directory=directory,
        plot=plot,
        figsize=figsize,
    )
