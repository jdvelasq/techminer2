# flake8: noqa
"""
WordCloud
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/images/report/keywords/word_cloud.png"

>>> import techminer2plus
>>> chart = techminer2plus.report.keywords.word_cloud(
...     title="Index & Author Keywords",
...     top_n=50,
...     root_dir=root_dir,
... )
>>> chart.plot_.savefig(file_name)

.. image:: ../../../../images/report/keywords/word_cloud.png
    :width: 900px
    :align: center


"""
from ...analyze import list_items
from ...visualize import word_cloud as visualize_word_cloud

FIELD = "keywords"


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

    return visualize_word_cloud(
        obj,
        title=title,
        figsize=figsize,
    )
