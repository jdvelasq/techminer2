"""
Keywords trend topics
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/keywords_trend_topics.png"
>>> keywords_trend_topics(column='author_keywords', directory=directory)

# .savefig(file_name)

.. image:: images/keywords_trend_topics.png
    :width: 650px
    :align: center


# >>> keywords_trend_topics(directory=directory, plot=False).head()


"""

from .annual_occurrence_matrix import annual_occurrence_matrix


def keywords_trend_topics(
    column,
    min_occ=1,
    n_keywords_per_year=5,
    directory="./",
):

    keywords_by_year = annual_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        directory=directory,
    )

    keywords_by_year = keywords_by_year.assign(
        num_documents=keywords_by_year.sum(axis=1)
    )

    return keywords_by_year
    keywords_by_year = keywords_by_year.reset_index()
