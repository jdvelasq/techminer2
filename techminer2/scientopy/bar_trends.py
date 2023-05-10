"""
Bar Trends
===============================================================================

ScientoPy Bar Trends


**Basic Usage.**

>>> from techminer2 import scientopy
>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/scientpy__bar_trends-1.html"
>>> r = scientopy.bar_trends(
...     criterion="author_keywords",
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-1.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
                       Before 2022  Between 2022-2023
author_keywords                                      
regtech                         20                  8
fintech                         10                  2
regulatory technology            5                  2
compliance                       5                  2
regulation                       4                  1


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top most frequent 20 author_keywords in the dataset. The terms 'Before 2022' and 'Between 2022-2023' in the column 'Period' represent the time windows. The column 'Num Documents' represents the number of documents in the time window. Use the information in the table to draw conclusions about growth trends of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | Author Keywords         | Period            |   Num Documents |
|---:|:------------------------|:------------------|----------------:|
|  0 | regtech                 | Before 2022       |              20 |
|  1 | fintech                 | Before 2022       |              10 |
|  2 | regulatory technology   | Before 2022       |               5 |
|  3 | compliance              | Before 2022       |               5 |
|  4 | regulation              | Before 2022       |               4 |
|  5 | financial services      | Before 2022       |               3 |
|  6 | financial regulation    | Before 2022       |               2 |
|  7 | artificial intelligence | Before 2022       |               3 |
|  8 | anti-money laundering   | Before 2022       |               3 |
|  9 | risk management         | Before 2022       |               2 |
| 10 | innovation              | Before 2022       |               2 |
| 11 | blockchain              | Before 2022       |               3 |
| 12 | suptech                 | Before 2022       |               1 |
| 13 | semantic technologies   | Before 2022       |               2 |
| 14 | data protection         | Before 2022       |               1 |
| 15 | smart contracts         | Before 2022       |               2 |
| 16 | charitytech             | Before 2022       |               1 |
| 17 | english law             | Before 2022       |               1 |
| 18 | gdpr                    | Before 2022       |               2 |
| 19 | data protection officer | Before 2022       |               2 |
| 20 | regtech                 | Between 2022-2023 |               8 |
| 21 | fintech                 | Between 2022-2023 |               2 |
| 22 | regulatory technology   | Between 2022-2023 |               2 |
| 23 | compliance              | Between 2022-2023 |               2 |
| 24 | regulation              | Between 2022-2023 |               1 |
| 25 | financial services      | Between 2022-2023 |               1 |
| 26 | financial regulation    | Between 2022-2023 |               2 |
| 27 | artificial intelligence | Between 2022-2023 |               1 |
| 28 | anti-money laundering   | Between 2022-2023 |               0 |
| 29 | risk management         | Between 2022-2023 |               1 |
| 30 | innovation              | Between 2022-2023 |               1 |
| 31 | blockchain              | Between 2022-2023 |               0 |
| 32 | suptech                 | Between 2022-2023 |               2 |
| 33 | semantic technologies   | Between 2022-2023 |               0 |
| 34 | data protection         | Between 2022-2023 |               1 |
| 35 | smart contracts         | Between 2022-2023 |               0 |
| 36 | charitytech             | Between 2022-2023 |               1 |
| 37 | english law             | Between 2022-2023 |               1 |
| 38 | gdpr                    | Between 2022-2023 |               0 |
| 39 | data protection officer | Between 2022-2023 |               0 |
<BLANKLINE>
<BLANKLINE>



**Time Filter.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-3.html"
>>> r = scientopy.bar_trends(
...     criterion="author_keywords",
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-3.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
                       Before 2020  Between 2020-2021
author_keywords                                      
regtech                          7                 11
fintech                          6                  4
regulatory technology            0                  5
compliance                       1                  4
regulation                       2                  2


**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-4.html"
>>> from techminer2 import scientopy
>>> r = scientopy.bar_trends(
...     criterion="author_keywords",
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

    <iframe src="../_static/scientpy__bar_trends-4.html" height="800px" width="100%" frameBorder="0"></iframe>




>>> file_name = "sphinx/_static/scientpy__bar_trends-5.html"
>>> r = scientopy.bar_trends(
...     criterion="author_keywords",
...     trend_analysis=True,
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-5.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()    
                       Before 2020  Between 2020-2021
author_keywords                                      
regulatory technology            0                  5
regulation                       2                  2
anti-money laundering            0                  3
accountability                   0                  2
gdpr                             0                  2

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 'author_keywords' with the highest average growth rate in the dataset. The terms 'Before 2020' and 'Between 2020-2021' in the column 'Period' represent the time windows. The column 'Num Documents' represents the number of documents in the time window. Use the information in the table to draw conclusions about growth trends of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | Author Keywords                 | Period            |   Num Documents |
|---:|:--------------------------------|:------------------|----------------:|
|  0 | regulatory technology           | Before 2020       |               0 |
|  1 | regulation                      | Before 2020       |               2 |
|  2 | anti-money laundering           | Before 2020       |               0 |
|  3 | accountability                  | Before 2020       |               0 |
|  4 | gdpr                            | Before 2020       |               0 |
|  5 | data protection officer         | Before 2020       |               0 |
|  6 | anti money laundering (aml)     | Before 2020       |               0 |
|  7 | innovation                      | Before 2020       |               0 |
|  8 | smart treasury                  | Before 2020       |               0 |
|  9 | regulations and compliance      | Before 2020       |               0 |
| 10 | coronavirus                     | Before 2020       |               0 |
| 11 | digital technologies            | Before 2020       |               0 |
| 12 | bahrain                         | Before 2020       |               0 |
| 13 | resale price maintenance        | Before 2020       |               0 |
| 14 | competition law                 | Before 2020       |               0 |
| 15 | antitrust                       | Before 2020       |               0 |
| 16 | vertical price fixing           | Before 2020       |               0 |
| 17 | financial fraud detection       | Before 2020       |               0 |
| 18 | classification (of information) | Before 2020       |               0 |
| 19 | anomaly detection               | Before 2020       |               0 |
| 20 | regulatory technology           | Between 2020-2021 |               5 |
| 21 | regulation                      | Between 2020-2021 |               2 |
| 22 | anti-money laundering           | Between 2020-2021 |               3 |
| 23 | accountability                  | Between 2020-2021 |               2 |
| 24 | gdpr                            | Between 2020-2021 |               2 |
| 25 | data protection officer         | Between 2020-2021 |               2 |
| 26 | anti money laundering (aml)     | Between 2020-2021 |               2 |
| 27 | innovation                      | Between 2020-2021 |               2 |
| 28 | smart treasury                  | Between 2020-2021 |               1 |
| 29 | regulations and compliance      | Between 2020-2021 |               1 |
| 30 | coronavirus                     | Between 2020-2021 |               1 |
| 31 | digital technologies            | Between 2020-2021 |               1 |
| 32 | bahrain                         | Between 2020-2021 |               1 |
| 33 | resale price maintenance        | Between 2020-2021 |               1 |
| 34 | competition law                 | Between 2020-2021 |               1 |
| 35 | antitrust                       | Between 2020-2021 |               1 |
| 36 | vertical price fixing           | Between 2020-2021 |               1 |
| 37 | financial fraud detection       | Between 2020-2021 |               1 |
| 38 | classification (of information) | Between 2020-2021 |               1 |
| 39 | anomaly detection               | Between 2020-2021 |               1 |
<BLANKLINE>
<BLANKLINE>


"""
from dataclasses import dataclass

import plotly.express as px

from ..techminer.indicators.growth_indicators_by_topic import growth_indicators_by_topic
from .bar import _filter_indicators_by_custom_topics


@dataclass(init=False)
class _Results:
    plot_ = None
    table_ = None
    prompt_ = None


def bar_trends(
    criterion,
    time_window=2,
    topics_length=20,
    custom_topics=None,
    trend_analysis=False,
    title="Trend",
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """ScientoPy Bar Trend."""

    indicators = growth_indicators_by_topic(
        criterion=criterion,
        time_window=time_window,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if trend_analysis is True:
        indicators = indicators.sort_values(
            by=["average_growth_rate", "OCC", "global_citations"],
            ascending=[False, False, False],
        )
    else:
        indicators = indicators.sort_values(
            by=["OCC", "global_citations", "average_growth_rate"],
            ascending=[False, False, False],
        )

    indicators = _filter_indicators_by_custom_topics(
        indicators=indicators,
        topics_length=topics_length,
        custom_topics=custom_topics,
    )

    indicators = indicators.sort_values(
        by=["OCC", "global_citations", "average_growth_rate"],
        ascending=[False, False, False],
    )

    col0 = indicators.columns[0]
    col1 = indicators.columns[1]

    indicators = indicators[[col0, col1]]

    results = _Results()
    results.table_ = indicators.copy()

    indicators = indicators.reset_index()
    indicators = indicators.melt(id_vars=criterion, value_vars=[col0, col1])
    indicators = indicators.rename(
        columns={
            criterion: criterion.replace("_", " ").title(),
            "variable": "Period",
            "value": "Num Documents",
        }
    )

    results.plot_ = _make_plot(indicators, criterion, col0, col1, title)
    results.prompt_ = _create_prompt(indicators, criterion, trend_analysis, col0, col1)

    return results


def _create_prompt(table, criterion, trend_analysis, col0, col1):
    if trend_analysis is True:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. \
The table below provides data on top {int(table.shape[0] / 2)} '{criterion}' \
with the highest average growth rate in the dataset. \
The terms '{col0}' and '{col1}' in the column 'Period' represent the time windows. \
The column 'Num Documents' represents the number of documents in the time window. \
Use the information in the table to draw conclusions about growth trends of the '{criterion}'. \
In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}

"""
    else:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. \
The table below provides data on top most frequent {int(table.shape[0] / 2)} {criterion} in the dataset. \
The terms '{col0}' and '{col1}' in the column 'Period' represent the time windows. \
The column 'Num Documents' represents the number of documents in the time window. \
Use the information in the table to draw conclusions about growth trends of the '{criterion}'. \
In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you \
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


def _make_plot(indicators, criterion, col0, col1, title):
    fig = px.bar(
        indicators,
        x="Num Documents",
        y=criterion.replace("_", " ").title(),
        color="Period",
        title=title,
        hover_data=["Num Documents"],
        orientation="h",
        color_discrete_map={
            col0: "#8da4b4",
            col1: "#556f81",
        },
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    return fig

    ###############################################################################


#     records = read_records(
#         directory=directory,
#         database=database,
#         start_year=start_year,
#         end_year=end_year,
#         **filters,
#     )

#     indicators = _growth_indicators_from_records(
#         column=criterion,
#         time_window=time_window,
#         directory=directory,
#         records=records,
#     )

#     indicators = _make_table(indicators)
#     results = _Results()
#     results.table_ = indicators.copy()

#     indicators = _filter_indicators(
#         indicators,
#         topics_length,
#         custom_topics,
#     )

#     results = _Results()
#     results.table_ = indicators.copy()

#     col0 = indicators.columns[0]
#     col1 = indicators.columns[1]
#     indicators = indicators.head(topics_length)
#     indicators = indicators.reset_index()

#     indicators = indicators.melt(id_vars=criterion, value_vars=[col0, col1])
#     indicators = indicators.rename(
#         columns={
#             criterion: criterion.replace("_", " ").title(),
#             "variable": "Period",
#             "value": "Num Documents",
#         }
#     )

#     results.plot_ = _make_plot(indicators, criterion, col0, col1)
#     return results


# def _filter_indicators(indicators, topics_length, custom_topics):
#     indicators = indicators.copy()
#     if custom_topics is not None:
#         custom_topics = [
#             topic for topic in custom_topics if topic in indicators.index.tolist()
#         ]
#     else:
#         custom_topics = indicators.index.copy()
#         custom_topics = custom_topics[:topics_length]

#     indicators = indicators.loc[custom_topics, :]

#     return indicators


# def _make_table(indicators):

#     indicators = indicators[indicators.columns[:2]]
#     indicators = indicators.assign(
#         num_documents=indicators[indicators.columns[0]]
#         + indicators[indicators.columns[1]]
#     )
#     indicators = indicators.sort_values(by="num_documents", ascending=False)
#     indicators.pop("num_documents")
#     return indicators
