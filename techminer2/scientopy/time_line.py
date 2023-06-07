# flake8: noqa
"""
Time Line
===============================================================================

ScientoPy Time Line Plot.


>>> root_dir = "data/regtech/"
>>> from techminer2 import scientopy

>>> file_name = "sphinx/_static/scientopy__time_line-1.html"
>>> r = scientopy.time_line(
...     field="author_keywords",
...     top_n=5,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-1.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
   Year Author Keywords  OCC
0  2017      COMPLIANCE    0
1  2018      COMPLIANCE    0
2  2019      COMPLIANCE    1
3  2020      COMPLIANCE    3
4  2021      COMPLIANCE    1

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top most frequent 5 author_keywords in the dataset. The columns in the table are the publication years. The table contains the number of documents in each year by item in 'author_keywords' .Use the information in the table to draw conclusions about importance and publication frequency of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
<BLANKLINE>
| Author Keywords    |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| COMPLIANCE         |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| FINANCIAL_SERVICES |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| FINTECH            |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGTECH            |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| REGULATION         |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
<BLANKLINE>
<BLANKLINE>



**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__time_line-3.html"
>>> r = scientopy.time_line(
...     field="author_keywords",
...     top_n=5,
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-3.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
   Year        Author Keywords  OCC
0  2018  ANTI_MONEY_LAUNDERING    0
1  2019  ANTI_MONEY_LAUNDERING    0
2  2020  ANTI_MONEY_LAUNDERING    1
3  2021  ANTI_MONEY_LAUNDERING    3
4  2018             COMPLIANCE    0



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__time_line-4.html"
>>> r = scientopy.time_line(
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

    <iframe src="../_static/scientopy__time_line-4.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/scientopy__time_line-5.html"
>>> r = scientopy.time_line(
...     field="author_keywords",
...     top_n=5,
...     trend_analysis=True,
...     year_filter=(2018, 2021),
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-5.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 5 'author_keywords' with the highest average growth rate in the dataset. The columns in the table are the publication years. The table contains the number of documents in each year by item in 'author_keywords' .Use the information in the table to draw conclusions about importance and publication frequency of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
<BLANKLINE>
| Author Keywords                 |   2018 |   2019 |   2020 |   2021 |
|:--------------------------------|-------:|-------:|-------:|-------:|
| ACCOUNTABILITY                  |      0 |      0 |      1 |      1 |
| ANTI_MONEY_LAUNDERING           |      0 |      0 |      1 |      3 |
| GDPR                            |      0 |      0 |      1 |      1 |
| REGULATION                      |      2 |      0 |      1 |      1 |
| REGULATORY_TECHNOLOGY (REGTECH) |      0 |      0 |      1 |      2 |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""
## ScientoPy // Time Line
import textwrap
from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.express as px

from ..techminer.indicators.growth_indicators_by_topic import (
    growth_indicators_by_topic,
)
from ..techminer.indicators.indicators_by_item_per_year import (
    indicators_by_item_per_year,
)
from .bar import _filter_indicators_by_custom_topics

TEXTLEN = 40


@dataclass(init=False)
class _Results:
    plot_ = None
    table_ = None
    prompt_ = None


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def time_line(
    field,
    # Specific params:
    time_window=2,
    trend_analysis=False,
    title="Time Line",
    # Item filters:
    top_n=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """ScientoPy Bar Trend."""

    # compute basic growth indicators

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

    ## here, the index of growth_indicators are the topics to plot
    selected_topics = growth_indicators.index.to_list()

    ## data to plot
    indicators = indicators_by_item_per_year(
        root_dir=root_dir,
        field=field,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = indicators[["OCC"]]
    indicators = indicators.reset_index()

    # the magic!
    indicators = indicators[indicators[field].isin(selected_topics)]

    indicators = indicators.sort_values([field, "year"], ascending=True)
    indicators = indicators.pivot(index="year", columns=field, values="OCC")
    indicators = indicators.fillna(0)

    # complete missing years
    year_range = list(
        range(indicators.index.min(), indicators.index.max() + 1)
    )
    missing_years = [
        year for year in year_range if year not in indicators.index
    ]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(indicators.columns))),
        index=missing_years,
        columns=indicators.columns,
    )
    indicators = pd.concat([indicators, pdf], ignore_index=False)
    indicators = indicators.sort_index()

    indicators = indicators.astype(int)

    ## plot data
    indicators.columns = [col for col in indicators.columns]
    indicators = indicators.reset_index()
    indicators = indicators.rename(columns={"index": "year"})
    indicators = indicators.melt(
        id_vars="year",
        value_vars=indicators.columns,
        var_name=field,
        value_name="OCC",
    )
    indicators[field] = indicators[field].apply(_shorten)

    column_ = field.replace("_", " ").title()
    indicators = indicators.rename(columns={"year": "Year", field: column_})

    ###

    results = _Results()
    results.table_ = indicators
    results.plot_ = _make_plot(column_, results.table_, title)
    results.prompt_ = _create_prompt(
        indicators.pivot(index=column_, columns="Year", values="OCC"),
        field,
        trend_analysis,
    )

    return results


def _create_prompt(table, criterion, trend_analysis):
    if trend_analysis is True:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. \
The table below provides data on top {int(table.shape[0])} '{criterion}' \
with the highest average growth rate in the dataset. \
The columns in the table are the publication years. \
The table contains the number of documents in each year by item in '{criterion}' .\
Use the information in the table to draw conclusions about importance and \
publication frequency of the '{criterion}'. \
In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.


{table.to_markdown()}

"""
    else:
        return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. \
The table below provides data on top most frequent {int(table.shape[0])} {criterion} in the dataset. \
The columns in the table are the publication years. \
The table contains the number of documents in each year by item in '{criterion}' .\
Use the information in the table to draw conclusions about importance and \
publication frequency of the '{criterion}'. \
In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.


{table.to_markdown()}

"""


# def _make_table(
#     criterion,
#     directory,
#     topics_length,
#     start_year,
#     end_year,
#     custom_topics,
#     **filters,
# ):

#     indicators = indicators_by_topic_per_year(
#         directory=directory,
#         criterion=criterion,
#         start_year=start_year,
#         end_year=end_year,
#         **filters,
#     )

#     indicators = indicators[["OCC"]]
#     indicators = indicators.reset_index()
#     indicators = indicators.sort_values([criterion, "year"], ascending=True)
#     indicators = indicators.pivot(index="year", columns=criterion, values="OCC")
#     indicators = indicators.fillna(0)

#     # complete missing years
#     year_range = list(range(indicators.index.min(), indicators.index.max() + 1))
#     missing_years = [year for year in year_range if year not in indicators.index]
#     pdf = pd.DataFrame(
#         np.zeros((len(missing_years), len(indicators.columns))),
#         index=missing_years,
#         columns=indicators.columns,
#     )
#     indicators = indicators.append(pdf)
#     indicators = indicators.sort_index()

#     ## Count and sort topics
#     occ = indicators.sum(axis=0)
#     occ = occ.sort_values(ascending=False)

#     ## Custom topics
#     if custom_topics is not None:
#         custom_topics = [topic for topic in custom_topics if topic in occ.index]
#     else:
#         custom_topics = occ.index.copy()
#         custom_topics = custom_topics[:topics_length]

#     ## Create table
#     indicators = indicators[custom_topics]

#     indicators = indicators.astype(int)

#     ## plot data
#     indicators.columns = [col for col in indicators.columns]
#     indicators = indicators.reset_index()
#     indicators = indicators.rename(columns={"index": "year"})
#     indicators = indicators.melt(
#         id_vars="year",
#         value_vars=indicators.columns,
#         var_name=criterion,
#         value_name="OCC",
#     )
#     indicators[criterion] = indicators[criterion].apply(_shorten)

#     column_ = criterion.replace("_", " ").title()
#     indicators = indicators.rename(columns={"year": "Year", criterion: column_})

#     return column_, indicators


def _make_plot(criterion, indicators, title):
    fig = px.line(
        indicators,
        x="Year",
        y="OCC",
        title=title,
        markers=True,
        hover_data=[criterion, "Year", "OCC"],
        color=criterion,
    )
    fig.update_traces(
        marker=dict(size=10, line=dict(color="darkslategray", width=2)),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        # showlegend=False,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        dtick=1,
    )
    return fig


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
