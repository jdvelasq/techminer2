"""
Bar
===============================================================================






**Basic Usage.**

>>> from techminer2 import scientopy
>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/scientopy__bar-1.html"
>>> r = scientopy.bar(
...    criterion='author_keywords',
...    directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-1.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.table_.head().to_markdown())
| author_keywords       |   OCC |   average_growth_rate |
|:----------------------|------:|----------------------:|
| regtech               |    28 |                  -0.5 |
| fintech               |    12 |                  -0.5 |
| regulatory technology |     7 |                  -1.5 |
| compliance            |     7 |                   0   |
| regulation            |     5 |                  -0.5 |



>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top most frequent 20 author_keywords in the dataset. The column 'OCC' indicates the number of documents in which each item in the column 'author_keywords' appears. The column 'average growth rate' in the table, is obtained by comparing the number of documents published Before 2022 with the number of documents published Between 2022-2023. Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the authors in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords         |   OCC |   average_growth_rate |
|:------------------------|------:|----------------------:|
| regtech                 |    28 |                  -0.5 |
| fintech                 |    12 |                  -0.5 |
| regulatory technology   |     7 |                  -1.5 |
| compliance              |     7 |                   0   |
| regulation              |     5 |                  -0.5 |
| financial services      |     4 |                 nan   |
| financial regulation    |     4 |                 nan   |
| artificial intelligence |     4 |                 nan   |
| anti-money laundering   |     3 |                  -1   |
| risk management         |     3 |                 nan   |
| innovation              |     3 |                  -0.5 |
| blockchain              |     3 |                  -0.5 |
| suptech                 |     3 |                 nan   |
| semantic technologies   |     2 |                 nan   |
| data protection         |     2 |                 nan   |
| smart contracts         |     2 |                 nan   |
| charitytech             |     2 |                 nan   |
| english law             |     2 |                 nan   |
| gdpr                    |     2 |                  -0.5 |
| data protection officer |     2 |                  -0.5 |
<BLANKLINE>
<BLANKLINE>



**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__bar-3.html"
>>> r = scientopy.bar(
...     criterion='author_keywords',
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-3.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())    
| author_keywords       |   OCC |   average_growth_rate |
|:----------------------|------:|----------------------:|
| regtech               |    18 |                  -0.5 |
| fintech               |    10 |                  -1.5 |
| regulatory technology |     5 |                   1.5 |
| compliance            |     5 |                   0   |
| regulation            |     4 |                   0.5 |



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__bar-4.html"
>>> r = scientopy.bar(
...     criterion='author_keywords',
...     custom_topics=[
...         "fintech", 
...         "blockchain", 
...         "financial regulation", 
...         "machine learning",
...         "big data",
...         "cryptocurrency",
...     ],
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-4.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown()) 
| author_keywords      |   OCC |   average_growth_rate |
|:---------------------|------:|----------------------:|
| fintech              |    12 |                  -0.5 |
| financial regulation |     4 |                 nan   |
| blockchain           |     3 |                  -0.5 |
| machine learning     |     1 |                 nan   |
| big data             |     1 |                 nan   |


**Filters.**

>>> file_name = "sphinx/_static/scientopy__bar-5.html"
>>> r = scientopy.bar(
...     criterion='countries',
...     directory=directory,
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
...     criterion='countries',
...     directory=directory,
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
...     criterion='author_keywords',
...     directory=directory,
...     topics_length=5,
...     trend_analysis=True,
...     start_year=2018,
...     end_year=2021,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-7.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown()) 
| author_keywords       |   OCC |   average_growth_rate |
|:----------------------|------:|----------------------:|
| regulatory technology |     5 |                   1.5 |
| regulation            |     4 |                   0.5 |
| anti-money laundering |     3 |                   1   |
| accountability        |     2 |                   0.5 |
| gdpr                  |     2 |                   0.5 |

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 5 'author_keywords' with the highest average growth rate in the dataset, obtained by comparing the number of documents published Before 2020 with the number of documents published Between 2020-2021. The column 'OCC' indicates the number of documents in which each item of the 'author_keywords' appears. Use the information in the table to draw conclusions about the number of occurrences of each item in 'author_keywords' appears. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords       |   OCC |   average_growth_rate |
|:----------------------|------:|----------------------:|
| regulatory technology |     5 |                   1.5 |
| regulation            |     4 |                   0.5 |
| anti-money laundering |     3 |                   1   |
| accountability        |     2 |                   0.5 |
| gdpr                  |     2 |                   0.5 |
<BLANKLINE>
<BLANKLINE>



"""
from dataclasses import dataclass

from .._plots.bar_plot import bar_plot
from ..techminer.indicators.growth_indicators_by_topic import growth_indicators_by_topic


@dataclass(init=False)
class _Results:
    plot_ = None
    table_ = None
    prompt_ = None


def bar(
    criterion,
    time_window=2,
    topics_length=20,
    custom_topics=None,
    trend_analysis=False,
    title=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """ScientoPy Bar Plot."""

    growth_indicators = growth_indicators_by_topic(
        criterion=criterion,
        time_window=time_window,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
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
        topics_length=topics_length,
        custom_topics=custom_topics,
    )

    growth_indicators = growth_indicators.sort_values(
        by=["OCC", "global_citations", "average_growth_rate"],
        ascending=[False, False, False],
    )

    col0 = growth_indicators.columns[0]
    col1 = growth_indicators.columns[1]

    obj = _Results()
    obj.plot_ = bar_plot(dataframe=growth_indicators, metric="OCC", title=title)
    obj.table_ = growth_indicators[["OCC", "average_growth_rate"]]
    obj.prompt_ = _create_prompt(obj.table_, criterion, trend_analysis, col0, col1)

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


def _filter_indicators_by_custom_topics(indicators, topics_length, custom_topics):
    # Copy the indicators dataframe to avoid mutating the original dataframe.
    indicators_copy = indicators.copy()

    # If custom topics are provided, only keep indicators that are in the custom
    # topics list.
    if custom_topics is not None:
        custom_topics = [
            topic for topic in custom_topics if topic in indicators.index.tolist()
        ]
    # If no custom topics are provided, keep the first n rows of the indicators
    # dataframe, where n is the number of topics.
    else:
        custom_topics = indicators.index.copy()
        custom_topics = custom_topics[:topics_length]

    # Filter the indicators dataframe by the custom topics.
    indicators_copy = indicators_copy.loc[custom_topics, :]

    return indicators_copy
