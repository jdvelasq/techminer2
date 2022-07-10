"""Primitive to make a wordcloud."""

import matplotlib.pyplot as plt
import numpy as np

from wordcloud import WordCloud


def _recolor(word, **kwargs):
    return "black"


def word_cloud_py(
    dataframe,
    metric,
    title,
    figsize,
):

    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)
    wc = WordCloud(background_color="white", repeat=True, mask=mask, colormap="Greys")

    text = {key: value for key, value in zip(dataframe.index, dataframe[metric])}
    wc.generate_from_frequencies(text)
    wc.recolor(color_func=_recolor)

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.set_axis_off()
    ax.set_title(title)

    # ax.spines["bottom"].set_color("lightgray")
    # ax.spines["top"].set_color("lightgray")
    # ax.spines["right"].set_color("lightgray")
    # ax.spines["left"].set_color("lightgray")
    # ax.set_xticks([])
    # ax.set_yticks([])

    # fig.set_tight_layout(True)

    return fig
