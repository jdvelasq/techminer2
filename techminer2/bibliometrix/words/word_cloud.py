# flake8: noqa
"""
WordCloud
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__word_cloud.html"


>>> from techminer2 import bibliometrix
>>> chart = bibliometrix.words.word_cloud(
...     field='author_keywords',
...     title="Author Keywords",
...     top_n=50,
...     root_dir=root_dir,
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__word_cloud.html" 
    height="400px" width="100%" frameBorder="0"></iframe>


"""
from ...vantagepoint.analyze import list_view
from ...vantagepoint.report import word_cloud as vp_word_cloud


def word_cloud(
    field,
    root_dir="./",
    database="documents",
    metric="OCC",
    # Plot options:
    title=None,
    figsize=(12, 12),
    # Item filters:
    top_n=250,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots a word cloud from a dataframe."""

    obj = list_view(
        field=field,
        root_dir=root_dir,
        database=database,
        metric=metric,
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
