# flake8: noqa
"""
Gantt Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__gantt_chart.html"

>>> from techminer2 import vantagepoint
>>> data = vantagepoint.analyze.terms_by_year(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... )
>>> chart = vantagepoint.report.gantt_chart(data)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__gantt_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head(10)
               author_keywords  Year  OCC
0               REGTECH 28:329  2017    2
1    FINANCIAL_SERVICES 04:168  2017    1
2  FINANCIAL_REGULATION 04:035  2017    1
3            BLOCKCHAIN 03:005  2017    1
4        SMART_CONTRACT 02:022  2017    1
5               REGTECH 28:329  2018    3
6               FINTECH 12:249  2018    2
7            REGULATION 05:164  2018    2
8    FINANCIAL_SERVICES 04:168  2018    1
9       RISK_MANAGEMENT 03:014  2018    1



>>> print(chart.prompt_)
Analyze the table below which contains the  occurrences by year for the years. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                        |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                         |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249                         |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| COMPLIANCE 07:030                      |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164                      |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| FINANCIAL_SERVICES 04:168              |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| FINANCIAL_REGULATION 04:035            |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |      0 |      0 |      0 |      1 |      2 |      1 |      0 |
| ARTIFICIAL_INTELLIGENCE 04:023         |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| ANTI-MONEY_LAUNDERING 03:021           |      0 |      0 |      0 |      1 |      2 |      0 |      0 |
| RISK_MANAGEMENT 03:014                 |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
| INNOVATION 03:012                      |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| REGULATORY_TECHNOLOGY 03:007           |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| BLOCKCHAIN 03:005                      |      1 |      0 |      1 |      0 |      1 |      0 |      0 |
| SUPTECH 03:004                         |      0 |      0 |      1 |      0 |      0 |      2 |      0 |
| DATA_PROTECTION 02:027                 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| SMART_CONTRACT 02:022                  |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
| CHARITYTECH 02:017                     |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| ENGLISH_LAW 02:017                     |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| ACCOUNTABILITY 02:014                  |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| DATA_PROTECTION_OFFICER 02:014         |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long    
"""
import textwrap

import plotly.express as px

from ...classes import BasicChart

COLOR = "#556f81"
TEXTLEN = 40


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
        obj.other_criterion_,
        obj.metric_,
        title,
    )

    chart = BasicChart()
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
