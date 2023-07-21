# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Word Cloud
===============================================================================

>>> from techminer2.bibliometrix.abstract_nlp_phrases import word_cloud
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/images/bibliometrix/abstract_nlp_phrases/word_cloud.png"
>>> chart = word_cloud(
...     title="Title NLP Phrases",
...     top_n=50,
...     root_dir=root_dir,
... )
>>> chart.fig_.savefig(file_name)

.. image:: ../../../../images/bibliometrix/abstract_nlp_phrases/word_cloud.png
    :width: 900px
    :align: center





"""
FIELD = "abstract_nlp_phrases"

from ...vantagepoint.report import word_cloud as vp_word_cloud


def word_cloud(
    #
    # CHART PARAMS:
    title=None,
    figsize=(10, 10),
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots a word cloud from a dataframe."""

    return vp_word_cloud(
        #
        # ITEMS PARAMS:
        field=FIELD,
        metric="OCC",
        #
        # CHART PARAMS:
        title=title,
        figsize=figsize,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
