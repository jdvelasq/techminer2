# flake8: noqa
"""
Word cloud
===============================================================================





>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/images/system/report/word_cloud.png"

>>> import techminer2plus
>>> obj = techminer2plus.system.analyze.list_items(
...     field='author_keywords',
...     root_dir=root_dir,
... )
>>> chart = techminer2plus.system.report.word_cloud(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.savefig(file_name)

.. image:: ../../images/system/report/word_cloud.png
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

>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 word.
<BLANKLINE>
Table:
```
| author_keywords         |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY   |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE              |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| REGULATION              |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING   |     5 |             5 |                   0 |                 34 |                 8 |                            6.8  |                           1.6  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES      |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| FINANCIAL_REGULATION    |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                   0.25      |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| ARTIFICIAL_INTELLIGENCE |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                   0.125     |                     2019 |     5 |                        4.6  |         3 |         2 |      0.6  |
| RISK_MANAGEMENT         |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        2.33 |         2 |         2 |      0.33 |
```
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
