# flake8: noqa
"""
Cleveland Chart (*)
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__cleveland_chart.html"


>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_view(
...    field='author_keywords',
...    root_dir=root_dir,
... )

>>> chart = vantagepoint.report.cleveland_dot_chart(obj, title="Most Frequent Author Keywords")
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
Analyze the table below, which provides bibliometric indicators for the field 'author_keywords' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
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
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""


import plotly.express as px

from ...classes import BasicChart


def cleveland_dot_chart(
    obj,
    title=None,
    metric_label=None,
    item_label=None,
):
    """Creates a cleveland doc chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        x_label (str, optional): X label. Defaults to None.
        y_label (str, optional): Y label. Defaults to None.


    """

    def create_plot():
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
            title_text=metric_label
            if metric_label is not None
            else obj.metric_.replace("_", " ").upper(),
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            autorange="reversed",
            gridcolor="lightgray",
            griddash="dot",
            title_text=item_label
            if item_label is not None
            else obj.criterion_.replace("_", " ").upper(),
        )
        return fig

    #
    # Main code
    #

    chart = BasicChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart
