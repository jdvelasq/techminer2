# flake8: noqa
"""
Bar Trends
===============================================================================

ScientoPy Bar Trends


**Basic Usage.**

>>> from techminer2 import scientopy
>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/scientpy__bar_trends-1.html"
>>> r = scientopy.bar_trends(
...     field="author_keywords",
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-1.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
                    Before 2022  Between 2022-2023
author_keywords                                   
REGTECH                      20                  8
FINTECH                      10                  2
COMPLIANCE                    5                  2
REGULATION                    4                  1
FINANCIAL_SERVICES            3                  1


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top most frequent 20 author_keywords in the dataset. The terms 'Before 2022' and 'Between 2022-2023' in the column 'Period' represent the time windows. The column 'Num Documents' represents the number of documents in the time window. Use the information in the table to draw conclusions about growth trends of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | Author Keywords                 | Period            |   Num Documents |
|---:|:--------------------------------|:------------------|----------------:|
|  0 | REGTECH                         | Before 2022       |              20 |
|  1 | FINTECH                         | Before 2022       |              10 |
|  2 | COMPLIANCE                      | Before 2022       |               5 |
|  3 | REGULATION                      | Before 2022       |               4 |
|  4 | FINANCIAL_SERVICES              | Before 2022       |               3 |
|  5 | FINANCIAL_REGULATION            | Before 2022       |               2 |
|  6 | REGULATORY_TECHNOLOGY (REGTECH) | Before 2022       |               3 |
|  7 | ANTI_MONEY_LAUNDERING           | Before 2022       |               4 |
|  8 | ARTIFICIAL_INTELLIGENCE         | Before 2022       |               3 |
|  9 | RISK_MANAGEMENT                 | Before 2022       |               2 |
| 10 | INNOVATION                      | Before 2022       |               2 |
| 11 | REGULATORY_TECHNOLOGY           | Before 2022       |               2 |
| 12 | BLOCKCHAIN                      | Before 2022       |               3 |
| 13 | SUPTECH                         | Before 2022       |               1 |
| 14 | DATA_PROTECTION                 | Before 2022       |               1 |
| 15 | SMART_CONTRACT                  | Before 2022       |               2 |
| 16 | ENGLISH_LAW                     | Before 2022       |               1 |
| 17 | CHARITYTECH                     | Before 2022       |               1 |
| 18 | DATA_PROTECTION_OFFICER         | Before 2022       |               2 |
| 19 | GDPR                            | Before 2022       |               2 |
| 20 | REGTECH                         | Between 2022-2023 |               8 |
| 21 | FINTECH                         | Between 2022-2023 |               2 |
| 22 | COMPLIANCE                      | Between 2022-2023 |               2 |
| 23 | REGULATION                      | Between 2022-2023 |               1 |
| 24 | FINANCIAL_SERVICES              | Between 2022-2023 |               1 |
| 25 | FINANCIAL_REGULATION            | Between 2022-2023 |               2 |
| 26 | REGULATORY_TECHNOLOGY (REGTECH) | Between 2022-2023 |               1 |
| 27 | ANTI_MONEY_LAUNDERING           | Between 2022-2023 |               0 |
| 28 | ARTIFICIAL_INTELLIGENCE         | Between 2022-2023 |               1 |
| 29 | RISK_MANAGEMENT                 | Between 2022-2023 |               1 |
| 30 | INNOVATION                      | Between 2022-2023 |               1 |
| 31 | REGULATORY_TECHNOLOGY           | Between 2022-2023 |               1 |
| 32 | BLOCKCHAIN                      | Between 2022-2023 |               0 |
| 33 | SUPTECH                         | Between 2022-2023 |               2 |
| 34 | DATA_PROTECTION                 | Between 2022-2023 |               1 |
| 35 | SMART_CONTRACT                  | Between 2022-2023 |               0 |
| 36 | ENGLISH_LAW                     | Between 2022-2023 |               1 |
| 37 | CHARITYTECH                     | Between 2022-2023 |               1 |
| 38 | DATA_PROTECTION_OFFICER         | Between 2022-2023 |               0 |
| 39 | GDPR                            | Between 2022-2023 |               0 |
<BLANKLINE>
<BLANKLINE>


**Time Filter.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-3.html"
>>> r = scientopy.bar_trends(
...     field="author_keywords",
...     year_filter=(2018, 2021),
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-3.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
                       Before 2020  Between 2020-2021
author_keywords                                      
REGTECH                          7                 11
FINTECH                          6                  4
COMPLIANCE                       1                  4
REGULATION                       2                  2
ANTI_MONEY_LAUNDERING            0                  4


**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-4.html"
>>> from techminer2 import scientopy
>>> r = scientopy.bar_trends(
...     field="author_keywords",
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

    <iframe src="../_static/scientpy__bar_trends-4.html" height="800px" width="100%" frameBorder="0"></iframe>




>>> file_name = "sphinx/_static/scientpy__bar_trends-5.html"
>>> r = scientopy.bar_trends(
...     field="author_keywords",
...     trend_analysis=True,
...     year_filter=(2018, 2021),
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-5.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()    
                                 Before 2020  Between 2020-2021
author_keywords                                                
REGULATION                                 2                  2
ANTI_MONEY_LAUNDERING                      0                  4
REGULATORY_TECHNOLOGY (REGTECH)            0                  3
ACCOUNTABILITY                             0                  2
GDPR                                       0                  2




>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 'author_keywords' with the highest average growth rate in the dataset. The terms 'Before 2020' and 'Between 2020-2021' in the column 'Period' represent the time windows. The column 'Num Documents' represents the number of documents in the time window. Use the information in the table to draw conclusions about growth trends of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | Author Keywords                 | Period            |   Num Documents |
|---:|:--------------------------------|:------------------|----------------:|
|  0 | REGULATION                      | Before 2020       |               2 |
|  1 | ANTI_MONEY_LAUNDERING           | Before 2020       |               0 |
|  2 | REGULATORY_TECHNOLOGY (REGTECH) | Before 2020       |               0 |
|  3 | ACCOUNTABILITY                  | Before 2020       |               0 |
|  4 | GDPR                            | Before 2020       |               0 |
|  5 | DATA_PROTECTION_OFFICER         | Before 2020       |               0 |
|  6 | INNOVATION                      | Before 2020       |               0 |
|  7 | REGULATORY_TECHNOLOGY           | Before 2020       |               0 |
|  8 | SMART_TREASURY                  | Before 2020       |               0 |
|  9 | REGULATIONS_AND_COMPLIANCE      | Before 2020       |               0 |
| 10 | CORONAVIRUS                     | Before 2020       |               0 |
| 11 | DIGITAL_TECHNOLOGIES            | Before 2020       |               0 |
| 12 | BAHRAIN                         | Before 2020       |               0 |
| 13 | RESALE_PRICE_MAINTENANCE        | Before 2020       |               0 |
| 14 | COMPETITION_LAW                 | Before 2020       |               0 |
| 15 | ANTITRUST                       | Before 2020       |               0 |
| 16 | VERTICAL_PRICE_FIXING           | Before 2020       |               0 |
| 17 | FINANCIAL_FRAUD_DETECTION       | Before 2020       |               0 |
| 18 | CLASSIFICATION                  | Before 2020       |               0 |
| 19 | ANOMALY_DETECTION               | Before 2020       |               0 |
| 20 | REGULATION                      | Between 2020-2021 |               2 |
| 21 | ANTI_MONEY_LAUNDERING           | Between 2020-2021 |               4 |
| 22 | REGULATORY_TECHNOLOGY (REGTECH) | Between 2020-2021 |               3 |
| 23 | ACCOUNTABILITY                  | Between 2020-2021 |               2 |
| 24 | GDPR                            | Between 2020-2021 |               2 |
| 25 | DATA_PROTECTION_OFFICER         | Between 2020-2021 |               2 |
| 26 | INNOVATION                      | Between 2020-2021 |               2 |
| 27 | REGULATORY_TECHNOLOGY           | Between 2020-2021 |               2 |
| 28 | SMART_TREASURY                  | Between 2020-2021 |               1 |
| 29 | REGULATIONS_AND_COMPLIANCE      | Between 2020-2021 |               1 |
| 30 | CORONAVIRUS                     | Between 2020-2021 |               1 |
| 31 | DIGITAL_TECHNOLOGIES            | Between 2020-2021 |               1 |
| 32 | BAHRAIN                         | Between 2020-2021 |               1 |
| 33 | RESALE_PRICE_MAINTENANCE        | Between 2020-2021 |               1 |
| 34 | COMPETITION_LAW                 | Between 2020-2021 |               1 |
| 35 | ANTITRUST                       | Between 2020-2021 |               1 |
| 36 | VERTICAL_PRICE_FIXING           | Between 2020-2021 |               1 |
| 37 | FINANCIAL_FRAUD_DETECTION       | Between 2020-2021 |               1 |
| 38 | CLASSIFICATION                  | Between 2020-2021 |               1 |
| 39 | ANOMALY_DETECTION               | Between 2020-2021 |               1 |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import plotly.express as px

from ..techminer.indicators.growth_indicators_by_topic import (
    growth_indicators_by_topic,
)
from .bar import _filter_indicators_by_custom_topics


@dataclass(init=False)
class _Results:
    plot_ = None
    table_ = None
    prompt_ = None


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def bar_trends(
    field,
    # Specific params:
    time_window=2,
    trend_analysis=False,
    title="Trend",
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
    """ScientoPy Bar Trend."""

    indicators = growth_indicators_by_topic(
        field=field,
        time_window=time_window,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
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
        topics_length=top_n,
        custom_topics=custom_items,
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
    indicators = indicators.melt(id_vars=field, value_vars=[col0, col1])
    indicators = indicators.rename(
        columns={
            field: field.replace("_", " ").title(),
            "variable": "Period",
            "value": "Num Documents",
        }
    )

    results.plot_ = _make_plot(indicators, field, col0, col1, title)
    results.prompt_ = _create_prompt(
        indicators, field, trend_analysis, col0, col1
    )

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
