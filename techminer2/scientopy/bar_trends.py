"""
Bar Trends
===============================================================================

ScientoPy Bar Trends


**Basic Usage.**

>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/scientpy__bar_trends-1.html"

>>> from techminer2 import scientopy
>>> trends = scientopy.bar_trends(
...     criterion="author_keywords",
...     directory=directory,
... )
>>> trends.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-1.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> trends.table_.head()
                       Before 2022  Between 2022-2023
author_keywords                                      
regtech                         20                  8
fintech                         10                  2
regulatory technology            5                  2
compliance                       5                  2
regulation                       4                  1

**Time Filter.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-3.html"
>>> from techminer2 import scientopy
>>> trends = scientopy.bar_trends(
...     criterion="author_keywords",
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> trends.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-3.html" height="800px" width="100%" frameBorder="0"></iframe>



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-4.html"
>>> from techminer2 import scientopy
>>> trends = scientopy.bar_trends(
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
>>> trends.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-4.html" height="800px" width="100%" frameBorder="0"></iframe>




>>> file_name = "sphinx/_static/scientpy__bar_trends-5.html"
>>> from techminer2 import scientopy
>>> trends = scientopy.bar_trends(
...     criterion="author_keywords",
...     trend_analysis=True,
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... )
>>> trends.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-5.html" height="800px" width="100%" frameBorder="0"></iframe>


"""

import plotly.express as px

from ..techminer.indicators.growth_indicators_by_topic import growth_indicators_by_topic
from .bar import _filter_indicators_by_custom_topics


class _Results:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


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
    return results


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
