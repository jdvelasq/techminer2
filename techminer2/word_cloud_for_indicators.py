"""Primitive to make a wordcloud from an indicators table."""

import matplotlib.pyplot as plt
import numpy as np

from wordcloud import WordCloud


def _recolor(word, **kwargs):
    return "black"


def word_cloud_for_indicators(
    dataframe,
    metric,
    title,
    figsize,
):
    """Wordcloud from a dataframe of indicators"""

    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)
    wc = WordCloud(background_color="white", repeat=True, mask=mask, colormap="Greys")

    text = {key: value for key, value in zip(dataframe.index, dataframe[metric])}
    wc.generate_from_frequencies(text)
    wc.recolor(color_func=_recolor)

    fig = plt.Figure(figsize=figsize)
    axs = fig.subplots()
    axs.imshow(wc, interpolation="bilinear")
    axs.set_axis_off()
    axs.set_title(title)

    return fig
