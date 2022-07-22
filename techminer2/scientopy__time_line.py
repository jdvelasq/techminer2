"""
Time Line
===============================================================================

ScientoPy Time Line Plot.


>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/scientopy__time_line-1.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     column="author_keywords",
...     topics_length=5,
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-1.html" height="800px" width="100%" frameBorder="0"></iframe>


**'skip_first' argument.**

>>> time_line.table_.head()
   Year Author Keywords  OCC
0  2016         regtech    1
1  2017         regtech    3
2  2018         regtech   14
3  2019         regtech   13
4  2020         regtech   18


>>> file_name = "sphinx/_static/scientopy__time_line-2.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     column="author_keywords",
...     topics_length=5,
...     skip_first=2,
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-2.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> time_line.table_.head()
   Year Author Keywords  OCC
0  2016      blockchain    0
1  2017      blockchain    2
2  2018      blockchain    2
3  2019      blockchain    5
4  2020      blockchain    4



**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__time_line-3.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     column="author_keywords",
...     topics_length=5,
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-3.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> time_line.table_.head()
   Year Author Keywords  OCC
0  2018         regtech   14
1  2019         regtech   13
2  2020         regtech   18
3  2021         regtech   14
4  2018         fintech   10



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__time_line-4.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     column="author_keywords",
...     custom_topics=["fintech", "blockchain", "financial regulation", "machine learning"],
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-4.html" height="800px" width="100%" frameBorder="0"></iframe>


"""
## ScientoPy // Time Line
import textwrap

import numpy as np
import pandas as pd
import plotly.express as px

from ._indicators.column_indicators_by_year import column_indicators_by_year

TEXTLEN = 40


class _Results:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def scientopy__time_line(
    column,
    topics_length=5,
    directory="./",
    start_year=None,
    end_year=None,
    skip_first=0,
    custom_topics=None,
    title=None,
):
    """ScientoPy Bar Trend."""

    results = _Results()
    column_, results.table_ = _make_table(
        column=column,
        directory=directory,
        topics_length=topics_length,
        start_year=start_year,
        end_year=end_year,
        skip_first=skip_first,
        custom_topics=custom_topics,
    )
    results.plot_ = _make_plot(column_, results.table_, title)
    return results


def _make_plot(column, indicators, title):

    fig = px.line(
        indicators,
        x="Year",
        y="OCC",
        title=title,
        markers=True,
        hover_data=[column, "Year", "OCC"],
        color=column,
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


def _make_table(
    column,
    directory,
    topics_length,
    start_year,
    end_year,
    skip_first,
    custom_topics,
):

    indicators = column_indicators_by_year(
        directory=directory, column=column, use_filter=False
    )
    indicators = indicators[["OCC"]]
    indicators = indicators.reset_index()
    indicators = indicators.sort_values([column, "year"], ascending=True)
    indicators = indicators.pivot(index="year", columns=column, values="OCC")
    indicators = indicators.fillna(0)

    # complete missing years
    year_range = list(range(indicators.index.min(), indicators.index.max() + 1))
    missing_years = [year for year in year_range if year not in indicators.index]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(indicators.columns))),
        index=missing_years,
        columns=indicators.columns,
    )
    indicators = indicators.append(pdf)
    indicators = indicators.sort_index()

    ## Apply year filters. The number of occurrences is affected
    ## by the number of years in the time line.
    if start_year is not None:
        indicators = indicators[indicators.index >= start_year]
    if end_year is not None:
        indicators = indicators[indicators.index <= end_year]

    ## Count and sort topics
    occ = indicators.sum(axis=0)
    occ = occ.sort_values(ascending=False)

    ## Custom topics
    if custom_topics is not None:
        custom_topics = [topic for topic in custom_topics if topic in occ.index]
    else:
        custom_topics = occ.index.copy()
        if skip_first > 0:
            custom_topics = custom_topics[skip_first:]
        custom_topics = custom_topics[:topics_length]

    ## Create table
    indicators = indicators[custom_topics]

    indicators = indicators.astype(int)

    ## plot data
    indicators.columns = [col for col in indicators.columns]
    indicators = indicators.reset_index()
    indicators = indicators.rename(columns={"index": "year"})
    indicators = indicators.melt(
        id_vars="year",
        value_vars=indicators.columns,
        var_name=column,
        value_name="OCC",
    )
    indicators[column] = indicators[column].apply(_shorten)

    column_ = column.replace("_", " ").title()
    indicators = indicators.rename(columns={"year": "Year", column: column_})

    return column_, indicators


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
