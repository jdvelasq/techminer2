# flake8: noqa
"""
Word cloud
===============================================================================




Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__word_cloud.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_view(
...     field='author_keywords',
...     root_dir=root_dir,
... )
>>> chart = vantagepoint.report.word_cloud(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

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
Analyze the table below, which provides bibliometric indicators for the field 'author_keywords' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| regtech                 |    28 |                329 |                74 |                           11.75 |                           2.64 |
| fintech                 |    12 |                249 |                49 |                           20.75 |                           4.08 |
| regulatory technology   |     7 |                 37 |                14 |                            5.29 |                           2    |
| compliance              |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| regulation              |     5 |                164 |                22 |                           32.8  |                           4.4  |
| financial services      |     4 |                168 |                20 |                           42    |                           5    |
| financial regulation    |     4 |                 35 |                 8 |                            8.75 |                           2    |
| artificial intelligence |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| anti-money laundering   |     3 |                 21 |                 4 |                            7    |                           1.33 |
| risk management         |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""

import matplotlib.pyplot as plt
import numpy as np
import plotly.tools as tls
from wordcloud import WordCloud

from ...classes import BasicChart


def word_cloud(
    obj,
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

        text = dict(zip(obj.table_.index, obj.table_[obj.metric_]))
        wordcloud.generate_from_frequencies(text)
        wordcloud.recolor(color_func=_recolor)

        plt.Figure(figsize=figsize)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        if title is not None:
            plt.title(title)
        plt.tight_layout(pad=0)

        fig = tls.mpl_to_plotly(plt.gcf())

        return fig

    def _recolor(word, **kwargs):
        # pylint: disable=unused-argument
        return "black"

    #
    # Main code:
    #

    chart = BasicChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart
