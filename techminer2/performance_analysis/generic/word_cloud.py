# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
.. _performance_analysis.graphs.word_cloud:

Word Cloud
===============================================================================


>>> from techminer2.performance_analysis.graphs import word_cloud
>>> chart = word_cloud(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Author Keywords",
...     width=400, 
...     height=400,
...     #
...     # ITEM FILTERS:
...     top_n=50,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.save("sphinx/_static/performance_analysis/graphs/word_cloud.png")

.. image:: ../../../_static/performance_analysis/graphs/word_cloud.png
    :width: 900px
    :align: center
    
>>> chart.df_.head()
                       rank_occ  OCC
author_keywords                     
REGTECH                       1   28
FINTECH                       2   12
REGULATORY_TECHNOLOGY         3    7
COMPLIANCE                    4    7
REGULATION                    5    5

>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                           |   rank_occ |   OCC |
|:------------------------------------------|-----------:|------:|
| REGTECH                                   |          1 |    28 |
| FINTECH                                   |          2 |    12 |
| REGULATORY_TECHNOLOGY                     |          3 |     7 |
| COMPLIANCE                                |          4 |     7 |
| REGULATION                                |          5 |     5 |
| ANTI_MONEY_LAUNDERING                     |          6 |     5 |
| FINANCIAL_SERVICES                        |          7 |     4 |
| FINANCIAL_REGULATION                      |          8 |     4 |
| ARTIFICIAL_INTELLIGENCE                   |          9 |     4 |
| RISK_MANAGEMENT                           |         10 |     3 |
| INNOVATION                                |         11 |     3 |
| BLOCKCHAIN                                |         12 |     3 |
| SUPTECH                                   |         13 |     3 |
| SEMANTIC_TECHNOLOGIES                     |         14 |     2 |
| DATA_PROTECTION                           |         15 |     2 |
| SMART_CONTRACTS                           |         16 |     2 |
| CHARITYTECH                               |         17 |     2 |
| ENGLISH_LAW                               |         18 |     2 |
| ACCOUNTABILITY                            |         19 |     2 |
| DATA_PROTECTION_OFFICER                   |         20 |     2 |
| GDPR                                      |         21 |     2 |
| SANDBOXES                                 |         22 |     2 |
| TECHNOLOGY                                |         23 |     2 |
| FINANCE                                   |         24 |     2 |
| REPORTING                                 |         25 |     2 |
| BUSINESS_MODELS                           |         26 |     1 |
| FUTURE_RESEARCH_DIRECTION                 |         27 |     1 |
| STANDARDS                                 |         28 |     1 |
| DIGITAL_IDENTITY                          |         29 |     1 |
| EUROPEAN_UNION                            |         30 |     1 |
| GENERAL_DATA_PROTECTION_REGULATION (GDPR) |         31 |     1 |
| OPEN_BANKING                              |         32 |     1 |
| PAYMENT_SERVICES_DIRECTIVE_2 (PSD_2)      |         33 |     1 |
| ALGORITHMIC_STANDARDS                     |         34 |     1 |
| DOCUMENT_ENGINEERING                      |         35 |     1 |
| COUNTER_TERROR_FINANCE                    |         36 |     1 |
| CHINA                                     |         37 |     1 |
| FINANCIAL_DEVELOPMENT                     |         38 |     1 |
| CORONAVIRUS                               |         39 |     1 |
| DIGITAL_TECHNOLOGY                        |         40 |     1 |
| REGULATIONS_AND_COMPLIANCE                |         41 |     1 |
| SMART_TREASURY                            |         42 |     1 |
| BUSINESS_MANAGEMENT                       |         43 |     1 |
| BUSINESS_POLICY                           |         44 |     1 |
| CORPORATE_FINANCE                         |         45 |     1 |
| INTERNATIONAL_FINANCE                     |         46 |     1 |
| KNOW_YOUR_CUSTOMER (KYC)_COMPLIANCE       |         47 |     1 |
| SUSTAINABLE_BUSINESS                      |         48 |     1 |
| FINANCIAL_CRIME                           |         49 |     1 |
| MONEY_LAUNDERING                          |         50 |     1 |
```
<BLANKLINE>



"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from wordcloud import WordCloud

from ..performance_metrics import performance_metrics


def word_cloud(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # CHART PARAMS:
    width=400,
    height=400,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a word cloud.

    :meta private:
    """

    items = performance_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = items.df_.copy()

    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)

    wordcloud = WordCloud(
        background_color="white",
        repeat=True,
        mask=mask,
        width=width,
        height=height,
    )

    text = dict(
        zip(
            data_frame.index,
            data_frame[metric],
        )
    )
    wordcloud.generate_from_frequencies(text)
    wordcloud.recolor(color_func=lambda word, **kwargs: "black")

    # fig = Figure(figsize=figsize)
    # ax_ = fig.add_subplot(111)
    # ax_.imshow(wordcloud, interpolation="bilinear")
    # ax_.axis("off")
    # if title is not None:
    #     ax_.set_title(title)
    # fig.tight_layout(pad=0)
    # items.fig_ = fig

    items.fig_ = wordcloud.to_image()

    return items
