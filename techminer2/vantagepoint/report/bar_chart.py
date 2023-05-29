"""
Bar Chart
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__bar_chart.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.extract_topics(
...     criterion='author_keywords',
...     directory=directory,
... )
>>> chart = vantagepoint.report.bar_chart(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__bar_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


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
import plotly.express as px

from ...classes import Chart, ListView


def bar_chart(
    obj,
    title=None,
    criterion_label=None,
    metric_label=None,
):
    """Bar chart.

    Args:
        obj: a data instance.
        title (str): the title of the chart.
        criterion_label (str): the label of the criterion.
        values_label (str): the label of the values.

    Returns:
        A :class:`Chart` instance.

    """

    def chatgpt_default_prompt():
        return (
            "Analyze the table below which contains values for the metric "
            f"{obj.metric_} for {obj.criterion_} "
            f"Identify any notable patterns, "
            "trends, or outliers in the data, and discuss their implications "
            "for the research field. Be sure to provide a concise summary of "
            "your findings in no more than 150 words."
            f"\n\n{obj.table_.to_markdown()}\n\n"
        )

    def create_fig(obj):
        figure = px.bar(
            obj.table_,
            x=obj.metric_,
            y=None,
            hover_data=obj.table_.columns.to_list(),
            orientation="h",
        )

        figure.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title if title is not None else "",
        )
        figure.update_traces(
            marker_color="rgb(171,171,171)",
            marker_line={"color": "darkslategray"},
        )
        figure.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title_text=metric_label
            if metric_label is not None
            else obj.metric_.replace("_", " ").upper(),
        )
        figure.update_yaxes(
            linecolor="gray",
            linewidth=2,
            autorange="reversed",
            gridcolor="lightgray",
            griddash="dot",
            title_text=criterion_label
            if criterion_label is not None
            else obj.criterion_.replace("_", " ").upper(),
        )
        return figure

    #
    #
    # Main:
    #
    #
    if not isinstance(obj, ListView):
        raise TypeError("`obj` must be a ListView instance")

    chart = Chart()
    chart.plot_ = create_fig(obj)
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = chatgpt_default_prompt()

    return chart
