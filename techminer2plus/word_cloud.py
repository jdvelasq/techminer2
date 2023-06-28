# flake8: noqa
"""
.. _word_cloud:

Word cloud
===============================================================================





>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/word_cloud.png"

>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...     field='author_keywords',
...     top_n=50,
...     root_dir=root_dir,
... )
>>> chart = techminer2plus.word_cloud(itemslist, title="Most Frequent Author Keywords")
>>> chart.plot_.savefig(file_name)

.. image:: ../_static/word_cloud.png
    :width: 900px
    :align: center

    
>>> chart.table_.head()
author_keywords
REGTECH                  28
FINTECH                  12
REGULATORY_TECHNOLOGY     7
COMPLIANCE                7
REGULATION                5
Name: OCC, dtype: int64




# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import matplotlib
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from wordcloud import WordCloud

# from ..analyze import list_items
# from ..classes import WordCloudChart
# from ..params_check_lib import check_listview


@dataclass
class WordCloudChart:
    """WordCloud.

    Attributes:
        plot_ (matplotlib): Plotly figure.
        table_ (pd.DataFrame): Table.

    """

    plot_: matplotlib.figure.Figure
    table_: pd.DataFrame


def word_cloud(
    data=None,
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

    def create_plot():
        x_mask, y_mask = np.ogrid[:300, :300]
        mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
        mask = 255 * mask.astype(int)

        wordcloud = WordCloud(background_color="white", repeat=True, mask=mask)

        text = dict(
            zip(
                data.df_.index,
                data.df_[data.metric_],
            )
        )
        wordcloud.generate_from_frequencies(text)
        wordcloud.recolor(color_func=_recolor)

        fig = Figure(figsize=figsize)
        ax_ = fig.add_subplot(111)
        ax_.imshow(wordcloud, interpolation="bilinear")

        ax_.axis("off")

        if title is not None:
            ax_.set_title(title)

        fig.tight_layout(pad=0)

        return fig

    def _recolor(word, **kwargs):
        # pylint: disable=unused-argument
        return "black"

    return WordCloudChart(
        table_=data.df_[data.metric_],
        plot_=create_plot(),
    )
