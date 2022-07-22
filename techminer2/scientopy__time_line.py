"""
Time Line
===============================================================================

ScientoPy Time Line Plot.


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/scientopy__time_line.html"

>>> from techminer2 import scientopy__time_line
>>> time_line = scientopy__time_line(
...     column="author_keywords",
...     top_n=5,
...     directory=directory,
... )
>>> time_line.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> time_line.table_.head()
   year author_keywords  OCC
0  2016         regtech    1
1  2017         regtech    3
2  2018         regtech   14
3  2019         regtech   13
4  2020         regtech   19

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
    top_n=5,
    directory="./",
    title=None,
):
    """ScientoPy Bar Trend."""

    results = _Results()
    results.table_ = _make_table(column, directory, top_n)
    results.plot_ = _make_plot(column, results.table_, title)
    return results


def _make_plot(column, indicators, title):

    fig = px.line(
        indicators,
        x="year",
        y="OCC",
        title=title,
        markers=True,
        hover_data=[column, "year", "OCC"],
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


def _make_table(column, directory, top_n):

    indicators = column_indicators_by_year(directory=directory, column=column)
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

    # top items
    occ = indicators.sum(axis=0)
    occ = occ.sort_values(ascending=False)

    indicators = indicators[occ.index[:top_n]]
    indicators = indicators.astype(int)

    # plot data
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

    return indicators


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
