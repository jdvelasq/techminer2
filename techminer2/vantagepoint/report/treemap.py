# flake8: noqa
"""
Treemap
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__treemap.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_view(
...    criterion='author_keywords',
...    root_dir=root_dir,
... )
>>> chart = vantagepoint.report.treemap(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

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
| accountability          |     2 |
| data protection officer |     2 |
<BLANKLINE>
<BLANKLINE>




"""
from dataclasses import dataclass

import plotly.express as px
import plotly.graph_objects as go

from ... import chatgpt


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def treemap(
    obj,
    title=None,
):
    """Bar chart.

    Parameters
    ----------
    obj : techminer2.vantagepoint.analyze.Analyze
        An object of type Analyze.
    title : str, optional
        Title of the chart, by default None

    """

    result = _Chart()
    result.plot_ = _create_plot(
        obj,
        title=title,
    )

    result.table_ = obj.table_[obj.metric_]
    result.prompt_ = chatgpt.generate_prompt_bibliographic_indicators(
        result.table_
    )

    return result


def _create_plot(
    obj,
    title=None,
):
    fig = go.Figure()
    fig.add_trace(
        go.Treemap(
            labels=obj.table_.index,
            parents=[""] * len(obj.table_),
            values=obj.table_[obj.metric_],
            textinfo="label+value",
        )
    )
    fig.update_traces(marker={"cornerradius": 5})
    fig.update_layout(
        showlegend=False,
        margin={"t": 30, "l": 0, "r": 0, "b": 0},
        title=title if title is not None else "",
    )

    # Change the colors of the treemap white
    fig.update_traces(
        marker={"line": {"color": "darkslategray", "width": 1}},
        marker_colors=["white"] * len(obj.table_),
    )

    # Change the font size of the labels
    fig.update_traces(textfont_size=12)

    return fig
