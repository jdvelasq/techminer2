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

    wordcloud = WordCloud(background_color="white", repeat=True, mask=mask)

    text = dict(zip(dataframe.index, dataframe[metric]))
    wordcloud.generate_from_frequencies(text)
    wordcloud.recolor(color_func=_recolor)

    plt.Figure(figsize=figsize)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.tight_layout(pad=0)

    return plt.gcf()
