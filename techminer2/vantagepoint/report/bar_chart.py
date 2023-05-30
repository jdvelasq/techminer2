# flake8: noqa
"""
Bar Chart
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__bar_chart.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_view(
...     criterion='author_keywords',
...     root_dir=root_dir,
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
Analyze the table below which contains values for the metric OCC for author_keywords Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| regtech                 |    28 |                329 |                74 |                           11.75 |                           2.64 |
| fintech                 |    12 |                249 |                49 |                           20.75 |                           4.08 |
| regulatory technology   |     7 |                 37 |                14 |                            5.29 |                           2    |
| compliance              |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| regulation              |     5 |                164 |                22 |                           32.8  |                           4.4  |
| financial services      |     4 |                168 |                20 |                           42    |                           5    |
| financial regulation    |     4 |                 35 |                 8 |                            8.75 |                           2    |
| artificial intelligence |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| anti-money laundering   |     3 |                 21 |                 4 |                            7    |                           1.33 |
| risk management         |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
| innovation              |     3 |                 12 |                 4 |                            4    |                           1.33 |
| blockchain              |     3 |                  5 |                 0 |                            1.67 |                           0    |
| suptech                 |     3 |                  4 |                 2 |                            1.33 |                           0.67 |
| semantic technologies   |     2 |                 41 |                19 |                           20.5  |                           9.5  |
| data protection         |     2 |                 27 |                 5 |                           13.5  |                           2.5  |
| smart contracts         |     2 |                 22 |                 8 |                           11    |                           4    |
| charitytech             |     2 |                 17 |                 4 |                            8.5  |                           2    |
| english law             |     2 |                 17 |                 4 |                            8.5  |                           2    |
| accountability          |     2 |                 14 |                 3 |                            7    |                           1.5  |
| data protection officer |     2 |                 14 |                 3 |                            7    |                           1.5  |
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
