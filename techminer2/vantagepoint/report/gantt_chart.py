"""
Gantt Chart (GPT)
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__gantt_chart.html"

>>> from techminer2 import vantagepoint
>>> data = vantagepoint.analyze.terms_by_year(
...    criterion='author_keywords',
...    topics_length=20,
...    directory=directory,
... )
>>> chart = vantagepoint.report.gantt_chart(data)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__gantt_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head(10)
               author_keywords  Year  OCC
0               regtech 28:329  2017    2
1    financial services 04:168  2017    1
2  financial regulation 04:035  2017    1
3            blockchain 03:005  2017    1
4       smart contracts 02:022  2017    1
5               regtech 28:329  2018    3
6               fintech 12:249  2018    2
7            regulation 05:164  2018    2
8    financial services 04:168  2018    1
9       risk management 03:014  2018    1

>>> print(chart.prompt_)
Analyze the table below which contains the  occurrences by year for the author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| regtech 28:329                 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| fintech 12:249                 |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| regulatory technology 07:037   |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| compliance 07:030              |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| regulation 05:164              |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| financial services 04:168      |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| financial regulation 04:035    |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| artificial intelligence 04:023 |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| anti-money laundering 03:021   |      0 |      0 |      0 |      1 |      2 |      0 |      0 |
| risk management 03:014         |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
| innovation 03:012              |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| blockchain 03:005              |      1 |      0 |      1 |      0 |      1 |      0 |      0 |
| suptech 03:004                 |      0 |      0 |      1 |      0 |      0 |      2 |      0 |
| semantic technologies 02:041   |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
| data protection 02:027         |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| smart contracts 02:022         |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
| charitytech 02:017             |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| english law 02:017             |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| gdpr 02:014                    |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| data protection officer 02:014 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
<BLANKLINE>
<BLANKLINE>

"""
import textwrap
from dataclasses import dataclass

import plotly.express as px

COLOR = "#556f81"
TEXTLEN = 40


@dataclass(init=False)
class _Chart:
    plot_ = None
    table_ = None


def gantt_chart(
    obj,
    title="",
):
    """Creates a Gantt Chart from a terms by year table."""

    table = obj.table_.melt(
        value_name="OCC", var_name="column", ignore_index=False
    )
    table = table[table.OCC > 0]
    table = table.rename(columns={"column": "Year"})
    table = table.reset_index()

    fig = _create_fig(
        table,
        obj.criterion_for_rows_,
        obj.metric_,
        title,
    )

    chart = _Chart()
    chart.plot_ = fig
    chart.table_ = table
    chart.prompt_ = obj.prompt_

    return chart


def _create_fig(table, criterion, metric, title):
    """Creates a figure."""

    fig = px.scatter(
        table,
        x="Year",
        y=criterion,
        size=metric,
        hover_data=table.columns.to_list(),
        title=title,
        color=criterion,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis_title=None,
        yaxis_title=criterion.replace("_", " ").upper(),
    )
    fig.update_traces(
        marker={
            "line": {"color": COLOR, "width": 1},
            "opacity": 1.0,
        },
        marker_color=COLOR,
        mode="lines+markers",
        line={"width": 2, "color": COLOR},
    )
    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
        tickangle=270,
        dtick=1.0,
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
    )

    return fig


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
