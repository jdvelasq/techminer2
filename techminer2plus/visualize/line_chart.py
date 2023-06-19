# flake8: noqa
"""
Line Chart
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/visualize/line_chart.html"

>>> import techminer2plus
>>> itemslist = techminer2plus.analyze.list_items(
...    field='author_keywords',
...    root_dir=root_dir,
... )
>>> chart = techminer2plus.visualize.line_chart(itemslist, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/visualize/line_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.table_.head()
author_keywords
REGTECH                  28
FINTECH                  12
REGULATORY_TECHNOLOGY     7
COMPLIANCE                7
REGULATION                5
Name: OCC, dtype: int64

>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords         |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY   |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE              |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| REGULATION              |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING   |     5 |             5 |                   0 |                 34 |                 8 |                            6.8  |                           1.6  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES      |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| FINANCIAL_REGULATION    |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                   0.25      |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| ARTIFICIAL_INTELLIGENCE |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                   0.125     |                     2019 |     5 |                        4.6  |         3 |         2 |      0.6  |
| RISK_MANAGEMENT         |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        2.33 |         2 |         2 |      0.33 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
import plotly.express as px

from ..check_params import check_listview
from ..classes import BasicChart


def line_chart(
    obj,
    title=None,
    field_label=None,
    metric_label=None,
):
    """Creates a line chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        metric_label (str, optional): Metric label. Defaults to None.
        field_label (str, optional): Field label. Defaults to None.

    Returns:
        BasicChart: A basic chart object.

    """

    def create_plot():
        figure = px.line(
            obj.table_,
            x=None,
            y=obj.metric_,
            hover_data=obj.table_.columns.to_list(),
            markers=True,
        )

        figure.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title,
        )
        figure.update_traces(
            marker=dict(size=9, line=dict(color="darkslategray", width=2)),
            marker_color="rgb(171,171,171)",
            line=dict(color="darkslategray"),
        )
        figure.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=270,
            title_text=field_label,
        )
        figure.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title_text=metric_label,
        )
        return figure

    #
    # Main code
    #

    check_listview(obj)

    if title is None:
        title = ""

    if metric_label is None:
        metric_label = obj.metric_.replace("_", " ").upper()

    if field_label is None:
        field_label = obj.field_.replace("_", " ").upper()

    chart = BasicChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart
