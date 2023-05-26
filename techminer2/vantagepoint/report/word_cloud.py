"""
Word cloud
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/vantagepoint__word_cloud.png"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.extract_topics(
...     criterion='author_keywords',
...     directory=directory,
... )
>>> chart = vantagepoint.report.word_cloud(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.savefig(file_name)

.. image:: ../../images/vantagepoint__word_cloud.png
    :width: 900px
    :align: center

>>> chart.table_.head()
author_keywords
regtech                  28
fintech                  12
regulatory technology     7
compliance                7
regulation                5
Name: OCC, dtype: int64


>>> print(chart.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |
|:------------------------|------:|
| regtech                 |    28 |
| fintech                 |    12 |
| regulatory technology   |     7 |
| compliance              |     7 |
| regulation              |     5 |
| financial services      |     4 |
| financial regulation    |     4 |
| artificial intelligence |     4 |
| anti-money laundering   |     3 |
| risk management         |     3 |
| innovation              |     3 |
| blockchain              |     3 |
| suptech                 |     3 |
| semantic technologies   |     2 |
| data protection         |     2 |
| smart contracts         |     2 |
| charitytech             |     2 |
| english law             |     2 |
| gdpr                    |     2 |
| data protection officer |     2 |
<BLANKLINE>
<BLANKLINE>

"""
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

from ... import chatgpt


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def word_cloud(
    obj,
    title=None,
    figsize=(10, 10),
):
    result = _Chart()
    result.plot_ = _create_plot(
        obj,
        title=title,
        figsize=figsize,
    )

    result.table_ = obj.table_[obj.metric_]
    result.prompt_ = chatgpt.generate_prompt_bibliographic_indicators(
        result.table_
    )

    return result


def _create_plot(
    obj,
    title,
    figsize,
):
    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)

    wordcloud = WordCloud(background_color="white", repeat=True, mask=mask)

    text = dict(zip(obj.table_.index, obj.table_[obj.metric_]))
    wordcloud.generate_from_frequencies(text)
    wordcloud.recolor(color_func=_recolor)

    plt.Figure(figsize=figsize)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    if title is not None:
        plt.title(title)
    plt.tight_layout(pad=0)

    return plt.gcf()


def _recolor(word, **kwargs):
    return "black"
