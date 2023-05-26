"""
Cleveland Chart (*)
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__cleveland_chart.html"

>>> from techminer2 import vantagepoint
>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.extract_topics(
...    criterion='author_keywords',
...    directory=directory,
... )

>>> chart = vantagepoint.report.cleveland_chart(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__cleveland_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head()
author_keywords
regtech                  28
fintech                  12
regulatory technology     7
compliance                7
regulation                5
Name: OCC, dtype: int64


>>> print(chart.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |
|:------------------------|------:|
| regtech                 |    28 |
| fintech                 |    12 |
| regulatory technology   |     7 |
| compliance              |     7 |
| regulation              |     5 |
| financial services      |     4 |
| financial regulation    |     4 |
| artificial intelligence |     4 |
| anti-money laundering   |     3 |
| risk management         |     3 |
| innovation              |     3 |
| blockchain              |     3 |
| suptech                 |     3 |
| semantic technologies   |     2 |
| data protection         |     2 |
| smart contracts         |     2 |
| charitytech             |     2 |
| english law             |     2 |
| gdpr                    |     2 |
| data protection officer |     2 |
<BLANKLINE>
<BLANKLINE>




"""
from dataclasses import dataclass

import plotly.express as px

from ... import chatgpt


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def cleveland_chart(
    obj,
    title=None,
    x_label=None,
    y_label=None,
):
    """Bar chart.

    Parameters
    ----------
    obj : techminer2.vantagepoint.analyze.Analyze
        An object of type Analyze.
    title : str, optional
        Title of the chart, by default None
    x_label : str, optional
        Label of the x-axis, by default None
    y_label : str, optional
        Label of the y-axis, by default None

    """

    result = _Chart()
    result.plot_ = _create_plot(
        obj,
        title=title,
        x_label=x_label,
        y_label=y_label,
    )

    result.table_ = obj.table_[obj.metric_]
    result.prompt_ = chatgpt.generate_prompt_bibliographic_indicators(
        result.table_
    )

    return result


def _create_plot(
    obj,
    title=None,
    x_label=None,
    y_label=None,
):
    fig = px.scatter(
        obj.table_,
        x=obj.metric_,
        y=None,
        hover_data=obj.table_.columns.to_list(),
        size=obj.metric_,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker=dict(
            size=12,
            line=dict(color="black", width=2),
        ),
        marker_color="slategray",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text=x_label
        if x_label is not None
        else obj.metric_.replace("_", " ").upper(),
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
        title_text=y_label
        if y_label is not None
        else obj.criterion_.replace("_", " ").upper(),
    )
    return fig
