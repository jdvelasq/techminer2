"""
Bar Trends
===============================================================================

ScientoPy Bar Trends




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/scientpy__bar_trends.html"

>>> from techminer2 import scientpy__bar_trends
>>> trends = scientpy__bar_trends(
...     column="author_keywords",
...     directory=directory,
... )
>>> trends.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> trends.table_.head()
                         Before 2021  Between 2021-2022
author_keywords                                        
regtech                           50                 20
fintech                           32                 10
blockchain                        13                  5
artificial intelligence            8                  5
compliance                        10                  2

"""
## ScientoPy // Bar Trends
import plotly.express as px

from .growth_indicators import growth_indicators


class _Results:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def scientopy__bar_trends(
    column,
    top_n=20,
    time_window=2,
    directory="./",
):
    """ScientoPy Bar Trend."""

    results = _Results()
    results.table_ = _make_table(column, time_window, directory)
    results.plot_ = _make_plot(column, results.table_, top_n)
    return results


def _make_plot(column, indicators, top_n):

    col0 = indicators.columns[0]
    col1 = indicators.columns[1]
    indicators = indicators.copy()
    indicators = indicators.iloc[:, :2]
    indicators = indicators.head(top_n)
    indicators = indicators.reset_index()

    indicators = indicators.melt(id_vars=column, value_vars=[col0, col1])
    indicators = indicators.rename(
        columns={
            column: column.replace("_", " ").title(),
            "variable": "Period",
            "value": "Num Documents",
        }
    )

    fig = px.bar(
        indicators,
        x="Num Documents",
        y=column.replace("_", " ").title(),
        color="Period",
        title="Trend",
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


def _make_table(column, time_window, directory):
    indicators = growth_indicators(column, time_window=time_window, directory=directory)
    indicators = indicators[indicators.columns[:2]]
    indicators = indicators.assign(
        num_documents=indicators[indicators.columns[0]]
        + indicators[indicators.columns[1]]
    )
    indicators = indicators.sort_values(by="num_documents", ascending=False)
    indicators.pop("num_documents")
    return indicators
