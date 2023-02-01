"""
Time Line
===============================================================================

ScientoPy Time Line Plot.


>>> directory = "data/regtech/"


>>> file_name = "sphinx/_static/scientopy__time_line-1.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     criterion="author_keywords",
...     topics_length=5,
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-1.html" height="800px" width="100%" frameBorder="0"></iframe>




**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__time_line-3.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     criterion="author_keywords",
...     topics_length=5,
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-3.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> time_line.table_.head()
   Year          Author Keywords  OCC
0  2018  artificial intelligence    2
1  2019  artificial intelligence    1
2  2020  artificial intelligence    5
3  2021  artificial intelligence    3
4  2018               blockchain    2



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__time_line-4.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     criterion="author_keywords",
...     custom_topics=["fintech", "blockchain", "financial regulation", "machine learning"],
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-4.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/scientopy__time_line-5.html"
>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     criterion="author_keywords",
...     topics_length=5,
...     trend_analysis=True,
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-5.html" height="800px" width="100%" frameBorder="0"></iframe>





"""
## ScientoPy // Time Line
import textwrap

import numpy as np
import pandas as pd
import plotly.express as px

from .scientopy__bar import _filter_indicators_by_custom_topics
from .tm2__growth_indicators_by_topic import tm2__growth_indicators_by_topic
from .tm2__indicators_by_topic_per_year import \
    tm2__indicators_by_topic_per_year

TEXTLEN = 40


class _Results:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def scientopy__time_line(
    criterion,
    time_window=2,
    topics_length=5,
    custom_topics=None,
    trend_analysis=False,
    title="Time Line",
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """ScientoPy Bar Trend."""

    # compute basic growth indicators

    growth_indicators = tm2__growth_indicators_by_topic(
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

    ## here, the index of growth_indicators are the topics to plot
    selected_topics = growth_indicators.index.to_list()

    ## data to plot
    indicators = tm2__indicators_by_topic_per_year(
        directory=directory,
        criterion=criterion,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = indicators[["OCC"]]
    indicators = indicators.reset_index()

    # the magic!
    indicators = indicators[indicators[criterion].isin(selected_topics)]

    indicators = indicators.sort_values([criterion, "year"], ascending=True)
    indicators = indicators.pivot(index="year", columns=criterion, values="OCC")
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

    indicators = indicators.astype(int)

    ## plot data
    indicators.columns = [col for col in indicators.columns]
    indicators = indicators.reset_index()
    indicators = indicators.rename(columns={"index": "year"})
    indicators = indicators.melt(
        id_vars="year",
        value_vars=indicators.columns,
        var_name=criterion,
        value_name="OCC",
    )
    indicators[criterion] = indicators[criterion].apply(_shorten)

    column_ = criterion.replace("_", " ").title()
    indicators = indicators.rename(columns={"year": "Year", criterion: column_})

    ###

    results = _Results()
    results.table_ = indicators

    results.plot_ = _make_plot(column_, results.table_, title)
    return results


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
