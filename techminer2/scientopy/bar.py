# flake8: noqa
"""
Bar
===============================================================================






**Basic Usage.**

>>> from techminer2 import scientopy
>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/scientopy__bar-1.html"
>>> r = scientopy.bar(
...     field='author_keywords',
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-1.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.table_.head().to_markdown())
| author_keywords    |   OCC |   average_growth_rate |
|:-------------------|------:|----------------------:|
| REGTECH            |    28 |                  -0.5 |
| FINTECH            |    12 |                  -0.5 |
| COMPLIANCE         |     7 |                   0   |
| REGULATION         |     5 |                  -0.5 |
| FINANCIAL_SERVICES |     4 |                 nan   |



>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top most frequent 20 author_keywords in the dataset. The column 'OCC' indicates the number of documents in which each item in the column 'author_keywords' appears. The column 'average growth rate' in the table, is obtained by comparing the number of documents published Before 2022 with the number of documents published Between 2022-2023. Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the authors in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords                 |   OCC |   average_growth_rate |
|:--------------------------------|------:|----------------------:|
| REGTECH                         |    28 |                  -0.5 |
| FINTECH                         |    12 |                  -0.5 |
| COMPLIANCE                      |     7 |                   0   |
| REGULATION                      |     5 |                  -0.5 |
| FINANCIAL_SERVICES              |     4 |                 nan   |
| FINANCIAL_REGULATION            |     4 |                 nan   |
| REGULATORY_TECHNOLOGY (REGTECH) |     4 |                  -1   |
| ANTI_MONEY_LAUNDERING           |     4 |                  -1.5 |
| ARTIFICIAL_INTELLIGENCE         |     4 |                 nan   |
| RISK_MANAGEMENT                 |     3 |                 nan   |
| INNOVATION                      |     3 |                  -0.5 |
| REGULATORY_TECHNOLOGY           |     3 |                  -0.5 |
| BLOCKCHAIN                      |     3 |                  -0.5 |
| SUPTECH                         |     3 |                 nan   |
| DATA_PROTECTION                 |     2 |                 nan   |
| SMART_CONTRACT                  |     2 |                 nan   |
| ENGLISH_LAW                     |     2 |                 nan   |
| CHARITYTECH                     |     2 |                 nan   |
| DATA_PROTECTION_OFFICER         |     2 |                  -0.5 |
| GDPR                            |     2 |                  -0.5 |
<BLANKLINE>
<BLANKLINE>



**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__bar-3.html"
>>> r = scientopy.bar(
...     field='author_keywords',
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-3.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())    
| author_keywords       |   OCC |   average_growth_rate |
|:----------------------|------:|----------------------:|
| REGTECH               |    18 |                  -0.5 |
| FINTECH               |    10 |                  -1.5 |
| COMPLIANCE            |     5 |                   0   |
| REGULATION            |     4 |                   0.5 |
| ANTI_MONEY_LAUNDERING |     4 |                   1.5 |



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__bar-4.html"
>>> r = scientopy.bar(
...     field='author_keywords',
...     custom_items=[
...         "FINTECH", 
...         "BLOCKCHAIN", 
...         "FINANCIAL_REGULATION", 
...         "MACHINE_LEARNING",
...         "BIG_DATA",
...         "CRYPTOCURRENCY",
...     ],
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-4.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown()) 
| author_keywords      |   OCC |   average_growth_rate |
|:---------------------|------:|----------------------:|
| FINTECH              |    12 |                  -0.5 |
| FINANCIAL_REGULATION |     4 |                 nan   |
| BLOCKCHAIN           |     3 |                  -0.5 |
| MACHINE_LEARNING     |     1 |                 nan   |
| BIG_DATA             |     1 |                 nan   |


**Filters.**

>>> file_name = "sphinx/_static/scientopy__bar-5.html"
>>> r = scientopy.bar(
...     field='countries',
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-5.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())    
| countries      |   OCC |   average_growth_rate |
|:---------------|------:|----------------------:|
| Australia      |     7 |                  -1   |
| United Kingdom |     7 |                 nan   |
| United States  |     6 |                   0.5 |
| Ireland        |     5 |                  -0.5 |
| China          |     5 |                   0.5 |


>>> file_name = "sphinx/_static/scientopy__bar-6.html"
>>> r = scientopy.bar(
...     field='countries',
...     root_dir=root_dir,
...     countries=['Australia', 'United Kingdom', 'United States'],
... )
>>> r.plot_.write_html(file_name)


.. raw:: html

    <iframe src="../_static/scientopy__bar-6.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown()) 
| countries      |   OCC |   average_growth_rate |
|:---------------|------:|----------------------:|
| Australia      |     7 |                  -1   |
| United Kingdom |     7 |                 nan   |
| United States  |     6 |                   0.5 |
| Hong Kong      |     3 |                 nan   |
| Switzerland    |     3 |                   0.5 |


>>> file_name = "sphinx/_static/scientopy__bar-7.html"
>>> r = scientopy.bar(
...     field='author_keywords',
...     trend_analysis=True,
...     top_n=5,
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-7.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown()) 
| author_keywords                 |   OCC |   average_growth_rate |
|:--------------------------------|------:|----------------------:|
| REGULATION                      |     4 |                   0.5 |
| ANTI_MONEY_LAUNDERING           |     4 |                   1.5 |
| REGULATORY_TECHNOLOGY (REGTECH) |     3 |                   1   |
| ACCOUNTABILITY                  |     2 |                   0.5 |
| GDPR                            |     2 |                   0.5 |

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 5 'author_keywords' with the highest average growth rate in the dataset, obtained by comparing the number of documents published Before 2020 with the number of documents published Between 2020-2021. The column 'OCC' indicates the number of documents in which each item of the 'author_keywords' appears. Use the information in the table to draw conclusions about the number of occurrences of each item in 'author_keywords' appears. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords                 |   OCC |   average_growth_rate |
|:--------------------------------|------:|----------------------:|
| REGULATION                      |     4 |                   0.5 |
| ANTI_MONEY_LAUNDERING           |     4 |                   1.5 |
| REGULATORY_TECHNOLOGY (REGTECH) |     3 |                   1   |
| ACCOUNTABILITY                  |     2 |                   0.5 |
| GDPR                            |     2 |                   0.5 |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""


from .._plots.bar_plot import bar_plot
from ..classes import ScientopyBar
from ..techminer.indicators.growth_indicators_by_topic import (
    growth_indicators_by_topic,
)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def bar(
    field,
    # Specific params:
    time_window=2,
    trend_analysis=False,
    title=None,
    # Item filters:
    top_n=20,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """ScientoPy Bar Plot."""

    growth_indicators = growth_indicators_by_topic(
        field=field,
        time_window=time_window,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if trend_analysis is True:
        growth_indicators = growth_indicators.sort_values(
            by=["average_growth_rate", "OCC", "global_citations"],
            ascending=[False, False, False],
        )
    else:
        growth_indicators = growth_indicators.sort_values(
            by=["OCC", "global_citations", "average_growth_rate"],
            ascending=[False, False, False],
        )

    growth_indicators = _filter_indicators_by_custom_topics(
        indicators=growth_indicators,
        topics_length=top_n,
        custom_topics=custom_items,
    )

    growth_indicators = growth_indicators.sort_values(
        by=["OCC", "global_citations", "average_growth_rate"],
        ascending=[False, False, False],
    )

    col0 = growth_indicators.columns[0]
    col1 = growth_indicators.columns[1]

    obj = ScientopyBar()
    obj.plot_ = bar_plot(
        dataframe=growth_indicators, metric="OCC", title=title
    )
    obj.table_ = growth_indicators[["OCC", "average_growth_rate"]]
    obj.prompt_ = _create_prompt(obj.table_, field, trend_analysis, col0, col1)

    return obj


def _create_prompt(table, criterion, trend_analysis, col0, col1):
    if trend_analysis is True:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. \
The table below provides data on top {table.shape[0]} '{criterion}' \
with the highest average growth rate in the dataset, obtained by \
comparing the number of documents published {col0} \
with the number of documents published {col1}. \
The column 'OCC' indicates the number of documents in which each item of \
the '{criterion}' appears. \
Use the information in the table to draw conclusions about the number of occurrences \
of each item in '{criterion}' appears. \
In your analysis, be sure to describe in a clear and concise way, any \
findings or any patterns you observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}

"""
    else:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. \
The table below provides data on top most frequent {table.shape[0]} {criterion} in the dataset. \
The column 'OCC' indicates the number of documents in which each item in the column '{criterion}' appears. \
The column 'average growth rate' in the table, is obtained by \
comparing the number of documents published {col0} \
with the number of documents published {col1}. \
Use the information in the table to draw conclusions about the impact and relevance of \
the reseach published by the authors in the dataset. In your analysis, be sure \
to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}

"""


def _filter_indicators_by_custom_topics(
    indicators, topics_length, custom_topics
):
    # Copy the indicators dataframe to avoid mutating the original dataframe.
    indicators_copy = indicators.copy()

    # If custom topics are provided, only keep indicators that are in the custom
    # topics list.
    if custom_topics is not None:
        custom_topics = [
            topic
            for topic in custom_topics
            if topic in indicators.index.tolist()
        ]
    # If no custom topics are provided, keep the first n rows of the indicators
    # dataframe, where n is the number of topics.
    else:
        custom_topics = indicators.index.copy()
        custom_topics = custom_topics[:topics_length]

    # Filter the indicators dataframe by the custom topics.
    indicators_copy = indicators_copy.loc[custom_topics, :]

    return indicators_copy
