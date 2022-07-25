"""
WordCloud
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/vantagepoint__word_cloud.png"


>>> from techminer2 import vantagepoint__word_cloud
>>> vantagepoint__word_cloud(
...     column='author_keywords',
...     title="Author Keywords",
...     top_n=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../../images/vantagepoint__word_cloud.png
    :width: 900px
    :align: center

"""
from ._indicators.indicators_by_topic import indicators_by_topic
from ._plots.word_cloud_for_indicators import word_cloud_for_indicators


def vantagepoint__word_cloud(
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

    indicators = indicators_by_topic(
        criterion=column,
        directory=directory,
        database=database,
        use_filter=(database == "documents"),
        sep=";",
    )

    indicators = indicators.sort_values(metric, ascending=False)

    if min_occ is not None:
        indicators = indicators[indicators.OCC >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.OCC <= max_occ]
    if top_n is not None:
        indicators = indicators.head(top_n)

    return word_cloud_for_indicators(
        dataframe=indicators,
        metric=metric,
        title=title,
        figsize=figsize,
    )
