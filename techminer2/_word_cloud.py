"""
World cloud graph
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/word_cloud.png"
>>> from techminer2.indicators_api.column_indicators import column_indicators
>>> data = column_indicators('authors', directory=directory).num_documents.head(50)
>>> word_cloud(data).savefig(file_name)

.. image:: images/word_cloud.png
    :width: 700px
    :align: center

"""

import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

TEXTLEN = 40


def _word_cloud(
    series,
    darkness=None,
    figsize=(6, 6),
    font_path=None,
    margin=2,
    ranks_only=None,
    prefer_horizontal=0.9,
    mask=None,
    scale=1,
    max_words=10000,
    min_font_size=4,
    stopwords=None,
    random_state=None,
    background_color="white",
    max_font_size=None,
    font_step=1,
    mode="RGB",
    relative_scaling="auto",
    regexp=None,
    collocations=True,
    cmap="Blues",
    normalize_plurals=True,
    contour_width=0,
    contour_color="white",
    repeat=False,
):
    """Plots a wordcloud from a dataframe."""

    def color_func(word, font_size, position, orientation, font_path, random_state):
        return color_dic[word]

    height = 400
    width = int(height * figsize[0] / figsize[1])

    series.index = series.index.astype(str)
    if darkness is not None:
        darkness.index = darkness.index.astype(str)

    darkness = series if darkness is None else darkness

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    cmap = plt.cm.get_cmap(cmap)

    words = {key: value for key, value in zip(series.index, series)}

    color_dic = {
        key: cmap(
            0.5 + 0.5 * (value - darkness.min()) / (darkness.max() - darkness.min())
        )
        for key, value in zip(darkness.index, darkness)
    }

    for key in color_dic.keys():
        a, b, c, d = color_dic[key]
        color_dic[key] = (
            np.uint8(a * 255),
            np.uint8(b * 255),
            np.uint8(c * 255),
            np.uint8(d * 255),
        )

    wordcloud = WordCloud(
        font_path=font_path,
        width=width,
        height=height,
        margin=margin,
        ranks_only=ranks_only,
        prefer_horizontal=prefer_horizontal,
        mask=mask,
        scale=scale,
        color_func=color_func,
        max_words=max_words,
        min_font_size=min_font_size,
        stopwords=stopwords,
        random_state=random_state,
        background_color=background_color,
        max_font_size=max_font_size,
        font_step=font_step,
        mode=mode,
        relative_scaling=relative_scaling,
        regexp=regexp,
        collocations=collocations,
        normalize_plurals=normalize_plurals,
        contour_width=contour_width,
        contour_color=contour_color,
        repeat=repeat,
    )

    wordcloud.generate_from_frequencies(words)
    ax.imshow(wordcloud, interpolation="bilinear")
    #
    ax.spines["bottom"].set_color("lightgray")
    ax.spines["top"].set_color("lightgray")
    ax.spines["right"].set_color("lightgray")
    ax.spines["left"].set_color("lightgray")
    ax.set_xticks([])
    ax.set_yticks([])

    fig.set_tight_layout(True)

    return fig
