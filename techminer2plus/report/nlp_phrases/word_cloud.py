# flake8: noqa
"""
WordCloud
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/images/bibliometrix__nlp_phrases_cloud.png"

>>> from techminer2 import bibliometrix
>>> chart = bibliometrix.nlp_phrases.word_cloud(
...     title="Title NLP Phrases",
...     top_n=50,
...     root_dir=root_dir,
... )
>>> chart.plot_.savefig(file_name)

.. image:: ../../../../images/bibliometrix__nlp_phrases_cloud.png
    :width: 900px
    :align: center


"""
# from ...vantagepoint.analyze import list_items
# from ...vantagepoint.charts import word_cloud as vp_word_cloud

FIELD = "nlp_phrases"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def word_cloud(
    # Plot options:
    title=None,
    figsize=(10, 10),
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots a word cloud from a dataframe."""

    obj = list_items(
        field=FIELD,
        root_dir=root_dir,
        database=database,
        metric="OCC",
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return vp_word_cloud(
        obj,
        title=title,
        figsize=figsize,
    )
