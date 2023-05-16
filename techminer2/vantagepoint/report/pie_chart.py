"""
Pie Chart (GPT)
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__pie_chart.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.extract_topics(
...    criterion='author_keywords',
...    directory=directory,
...    topics_length=10,
... )
>>> chart = vantagepoint.report.pie_chart(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__pie_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

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


def pie_chart(
    obj,
    title=None,
    hole=0.4,
):
    result = _Chart()
    result.plot_ = _create_plot(
        obj,
        title=title,
        hole=hole,
    )

    result.table_ = obj.table_[obj.metric_]
    result.prompt_ = chatgpt.generate_prompt(result.table_)

    return result


def _create_plot(
    obj,
    title,
    hole,
):
    fig = px.pie(
        obj.table_,
        values=obj.metric_,
        names=obj.table_.index.to_list(),
        hole=hole,
        hover_data=obj.table_.columns.to_list(),
        title=title if title is not None else "",
    )
    fig.update_traces(textinfo="percent+value")
    fig.update_layout(legend={"y": 0.5})
    return fig
