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
| author_keywords       |   Before 2022 |   Between 2022-2023 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:----------------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| regtech               |            20 |                   8 |                329 |    28 |                          4   |                  -0.5 |
| fintech               |            10 |                   2 |                249 |    12 |                          1   |                  -0.5 |
| regulatory technology |             5 |                   2 |                 37 |     7 |                          1   |                  -1.5 |
| compliance            |             5 |                   2 |                 30 |     7 |                          1   |                   0   |
| regulation            |             4 |                   1 |                164 |     5 |                          0.5 |                  -0.5 |



>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top most frequent 20 author_keywords in the dataset. In the following text, we use 'item' to represent the term 'author_keywords'. The column 'OCC' indicates the number of documents in which the keyword appears. The column 'global_citations' indicates the sum of citations received by the keyword in the documents in which the keyword appears. The column 'average_growth_rate' indicates the average growth rate of the keyword in the documents in which the keyword appears. Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the authors in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords         |   Before 2022 |   Between 2022-2023 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:------------------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| regtech                 |            20 |                   8 |                329 |    28 |                          4   |                  -0.5 |
| fintech                 |            10 |                   2 |                249 |    12 |                          1   |                  -0.5 |
| regulatory technology   |             5 |                   2 |                 37 |     7 |                          1   |                  -1.5 |
| compliance              |             5 |                   2 |                 30 |     7 |                          1   |                   0   |
| regulation              |             4 |                   1 |                164 |     5 |                          0.5 |                  -0.5 |
| financial services      |             3 |                   1 |                168 |     4 |                          0.5 |                 nan   |
| financial regulation    |             2 |                   2 |                 35 |     4 |                          1   |                 nan   |
| artificial intelligence |             3 |                   1 |                 23 |     4 |                          0.5 |                 nan   |
| anti-money laundering   |             3 |                   0 |                 21 |     3 |                          0   |                  -1   |
| risk management         |             2 |                   1 |                 14 |     3 |                          0.5 |                 nan   |
| innovation              |             2 |                   1 |                 12 |     3 |                          0.5 |                  -0.5 |
| blockchain              |             3 |                   0 |                  5 |     3 |                          0   |                  -0.5 |
| suptech                 |             1 |                   2 |                  4 |     3 |                          1   |                 nan   |
| semantic technologies   |             2 |                   0 |                 41 |     2 |                          0   |                 nan   |
| data protection         |             1 |                   1 |                 27 |     2 |                          0.5 |                 nan   |
| smart contracts         |             2 |                   0 |                 22 |     2 |                          0   |                 nan   |
| charitytech             |             1 |                   1 |                 17 |     2 |                          0.5 |                 nan   |
| english law             |             1 |                   1 |                 17 |     2 |                          0.5 |                 nan   |
| gdpr                    |             2 |                   0 |                 14 |     2 |                          0   |                  -0.5 |
| data protection officer |             2 |                   0 |                 14 |     2 |                          0   |                  -0.5 |
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
| author_keywords       |   Before 2020 |   Between 2020-2021 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:----------------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| regtech               |             7 |                  11 |                297 |    18 |                          5.5 |                  -0.5 |
| fintech               |             6 |                   4 |                235 |    10 |                          2   |                  -1.5 |
| regulatory technology |             0 |                   5 |                 35 |     5 |                          2.5 |                   1.5 |
| compliance            |             1 |                   4 |                 29 |     5 |                          2   |                   0   |
| regulation            |             2 |                   2 |                163 |     4 |                          1   |                   0.5 |
    


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
| author_keywords      |   Before 2022 |   Between 2022-2023 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:---------------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| fintech              |            10 |                   2 |                249 |    12 |                          1   |                  -0.5 |
| financial regulation |             2 |                   2 |                 35 |     4 |                          1   |                 nan   |
| blockchain           |             3 |                   0 |                  5 |     3 |                          0   |                  -0.5 |
| machine learning     |             0 |                   1 |                  3 |     1 |                          0.5 |                 nan   |
| big data             |             0 |                   1 |                  3 |     1 |                          0.5 |                 nan   |



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
| countries      |   Before 2022 |   Between 2022-2023 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:---------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| Australia      |             7 |                   0 |                199 |     7 |                          0   |                  -1   |
| United Kingdom |             6 |                   1 |                199 |     7 |                          0.5 |                 nan   |
| United States  |             4 |                   2 |                 59 |     6 |                          1   |                   0.5 |
| Ireland        |             4 |                   1 |                 55 |     5 |                          0.5 |                  -0.5 |
| China          |             1 |                   4 |                 27 |     5 |                          2   |                   0.5 |


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
| countries      |   Before 2022 |   Between 2022-2023 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:---------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| Australia      |             7 |                   0 |                199 |     7 |                          0   |                  -1   |
| United Kingdom |             6 |                   1 |                199 |     7 |                          0.5 |                 nan   |
| United States  |             4 |                   2 |                 59 |     6 |                          1   |                   0.5 |
| Hong Kong      |             3 |                   0 |                185 |     3 |                          0   |                 nan   |
| Switzerland    |             2 |                   1 |                 45 |     3 |                          0.5 |                   0.5 |


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
| author_keywords       |   Before 2020 |   Between 2020-2021 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:----------------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| regulatory technology |             0 |                   5 |                 35 |     5 |                          2.5 |                   1.5 |
| regulation            |             2 |                   2 |                163 |     4 |                          1   |                   0.5 |
| anti-money laundering |             0 |                   3 |                 21 |     3 |                          1.5 |                   1   |
| accountability        |             0 |                   2 |                 14 |     2 |                          1   |                   0.5 |
| gdpr                  |             0 |                   2 |                 14 |     2 |                          1   |                   0.5 |


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 5 author keywords with the highest average growth rate in the dataset. In the following text, we use 'item' to represent the term 'author keywords'. The column 'OCC' indicates the number of documents in which the item appears. The column 'global_citations' indicates the sum of citations received by the item in the documents in which the item appears. The column 'average_growth_rate' indicates the average growth rate of the keyword in the documents in which the keyword appears. Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the authors in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords       |   Before 2020 |   Between 2020-2021 |   global_citations |   OCC |   average_documents_per_year |   average_growth_rate |
|:----------------------|--------------:|--------------------:|-------------------:|------:|-----------------------------:|----------------------:|
| regulatory technology |             0 |                   5 |                 35 |     5 |                          2.5 |                   1.5 |
| regulation            |             2 |                   2 |                163 |     4 |                          1   |                   0.5 |
| anti-money laundering |             0 |                   3 |                 21 |     3 |                          1.5 |                   1   |
| accountability        |             0 |                   2 |                 14 |     2 |                          1   |                   0.5 |
| gdpr                  |             0 |                   2 |                 14 |     2 |                          1   |                   0.5 |
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

    obj = _Results()
    obj.plot_ = bar_plot(dataframe=growth_indicators, metric="OCC", title=title)
    obj.table_ = growth_indicators
    obj.prompt_ = _create_prompt(growth_indicators, criterion, trend_analysis)

    return obj


def _create_prompt(table, criterion, trend_analysis):
    if trend_analysis is True:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} {criterion.replace('_', ' ')} \
with the highest average growth rate in the dataset. In the following text, \
we use 'item' to represent the term '{criterion.replace('_', ' ')}'. \
The column 'OCC' indicates the number of documents in which the item appears. \
The column 'global_citations' indicates the sum of citations received by the item \
in the documents in which the item appears. The column 'average_growth_rate' \
indicates the average growth rate of the keyword in the documents in which the keyword appears. \
Use the information in the table to draw conclusions about the impact and relevance of \
the reseach published by the authors in the dataset. In your analysis, be sure \
to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}

"""
    else:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top most frequent {table.shape[0]} {criterion} \
in the dataset. In the following text, we use 'item' to represent the term \
'{criterion}'. The column 'OCC' indicates \
the number of documents in which the keyword appears. The column 'global_citations' \
indicates the sum of citations received by the keyword in the documents in which \
the keyword appears. The column 'average_growth_rate' indicates the average \
growth rate of the keyword in the documents in which the keyword appears. \
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
