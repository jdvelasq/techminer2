# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _word_cloud:

Word Cloud
===============================================================================


>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> tm2.word_cloud(
...    field='author_keywords',
...    title="Most Frequent Author Keywords",
...    top_n=50,
...    root_dir=root_dir,
... ).savefig("sphinx/_static/word_cloud.png")
... )

.. image:: ../../_static/word_cloud.png
    :width: 900px
    :align: center
    
"""
import numpy as np
from matplotlib.figure import Figure
from wordcloud import WordCloud

# from .list_items_table import list_items_table


def word_cloud(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    figsize=(10, 10),
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a word cloud.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        figsize (tuple, optional): Figure size. Defaults to (10, 10).

    Returns:
        BasicChart: A basic chart object.


    """

    data_frame = list_items_table(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
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

    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)

    wordcloud = WordCloud(background_color="white", repeat=True, mask=mask)

    text = dict(
        zip(
            data_frame.index,
            data_frame[metric],
        )
    )
    wordcloud.generate_from_frequencies(text)
    wordcloud.recolor(color_func=lambda word, **kwargs: "black")

    fig = Figure(figsize=figsize)
    ax_ = fig.add_subplot(111)
    ax_.imshow(wordcloud, interpolation="bilinear")

    ax_.axis("off")

    if title is not None:
        ax_.set_title(title)

    fig.tight_layout(pad=0)

    return fig
