"""
Index keywords trend topics
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/index_keywords_trend_topics.png"
>>> index_keywords_trend_topics(directory=directory).savefig(file_name)

.. image:: images/index_keywords_trend_topics.png
    :width: 650px
    :align: center

>>> index_keywords_trend_topics(directory=directory, plot=False).head()
pub_year            num_documents  year_q1  ...  global_citations  rn
index_keywords                              ...                      
fintech                        48     2016  ...               269   0
financial service              19     2016  ...               347   1
finance                        18     2016  ...               489   2
financial sector                3     2016  ...                 3   3
potential benefits              2     2016  ...                 5   4
<BLANKLINE>
[5 rows x 6 columns]

"""

from .keywords_trend_topics import keywords_trend_topics


def index_keywords_trend_topics(
    n_keywords_per_year=5,
    directory="./",
    plot=True,
    figsize=(6, 6),
):
    return keywords_trend_topics(
        column="index_keywords",
        n_keywords_per_year=n_keywords_per_year,
        directory=directory,
        plot=plot,
        figsize=figsize,
    )
