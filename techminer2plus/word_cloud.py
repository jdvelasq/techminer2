# flake8: noqa
# pylint: disable=line-too-long
"""
.. _word_cloud:

Word cloud
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .list_items(
...         field='author_keywords',
...         top_n=20,
...     )
...     .word_cloud(
...         title="Most Frequent Author Keywords",
...     )
...     .savefig("sphinx/_static/word_cloud_0.png")
... )

.. image:: ../_static/word_cloud_0.png
    :width: 900px
    :align: center



* Functional interface

>>> itemslist = tm2p.list_items(
...     field='author_keywords',
...     top_n=50,
...     root_dir=root_dir,
... )
>>> tm2p.word_cloud(
...     itemslist, 
...     title="Most Frequent Author Keywords",
... ).savefig("sphinx/_static/word_cloud_1.png")

.. image:: ../_static/word_cloud_1.png
    :width: 900px
    :align: center

    
"""
import numpy as np
from matplotlib.figure import Figure
from wordcloud import WordCloud


def word_cloud(
    list_items,
    title=None,
    figsize=(10, 10),
):
    """Creates a word cloud.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        figsize (tuple, optional): Figure size. Defaults to (10, 10).

    Returns:
        BasicChart: A basic chart object.


    """

    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)

    wordcloud = WordCloud(background_color="white", repeat=True, mask=mask)

    text = dict(
        zip(
            list_items.df_.index,
            list_items.df_[list_items.metric],
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
