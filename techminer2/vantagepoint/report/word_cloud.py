# flake8: noqa
"""
Word cloud
===============================================================================




Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/images/vantagepoint__word_cloud.png"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_items(
...     field='author_keywords',
...     root_dir=root_dir,
... )
>>> chart = vantagepoint.report.word_cloud(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.savefig(file_name)

.. image:: ../../images/vantagepoint__word_cloud.png
    :width: 900px
    :align: center

    
>>> chart.table_.head()
author_keywords
REGTECH               28
FINTECH               12
COMPLIANCE             7
REGULATION             5
FINANCIAL_SERVICES     4
Name: OCC, dtype: int64


>>> print(chart.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'author_keywords' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                 |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:--------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| REGTECH                         |    28 |                329 |                74 |                           11.75 |                           2.64 |
| FINTECH                         |    12 |                249 |                49 |                           20.75 |                           4.08 |
| COMPLIANCE                      |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| REGULATION                      |     5 |                164 |                22 |                           32.8  |                           4.4  |
| FINANCIAL_SERVICES              |     4 |                168 |                20 |                           42    |                           5    |
| FINANCIAL_REGULATION            |     4 |                 35 |                 8 |                            8.75 |                           2    |
| REGULATORY_TECHNOLOGY (REGTECH) |     4 |                 30 |                10 |                            7.5  |                           2.5  |
| ARTIFICIAL_INTELLIGENCE         |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| ANTI_MONEY_LAUNDERING           |     4 |                 23 |                 4 |                            5.75 |                           1    |
| RISK_MANAGEMENT                 |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""


import numpy as np
from matplotlib.figure import Figure
from wordcloud import WordCloud

from ...classes import WordCloudChart


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

    #
    # Main code:
    #

    chart = WordCloudChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart
