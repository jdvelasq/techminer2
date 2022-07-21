"""
WordCloud
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/bibliometrix__word_cloud.png"


>>> from techminer2 import bibliometrix__word_cloud
>>> bibliometrix__word_cloud(
...     column='author_keywords',
...     title="Author Keywords",
...     top_n=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../../../images/bibliometrix__word_cloud.png
    :width: 900px
    :align: center

"""
from .wordcloud import wordcloud


def bibliometrix__word_cloud(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="OCC",
    title=None,
    database="documents",
    #
    figsize=(12, 12),
):
    """Plots a word cloud from a dataframe."""

    return wordcloud(
        column=column,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        metric=metric,
        title=title,
        database=database,
        #
        figsize=figsize,
    )
