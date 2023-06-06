# flake8: noqa
"""
Cleveland Dot Chart (*)
===============================================================================


Example
-------------------------------------------------------------------------------

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
REGTECH               28
FINTECH               12
COMPLIANCE             7
REGULATION             5
FINANCIAL_SERVICES     4
Name: OCC, dtype: int64


>>> print(chart.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'author_keywords' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                 |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:--------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| REGTECH                         |    28 |                329 |                74 |                           11.75 |                           2.64 |
| FINTECH                         |    12 |                249 |                49 |                           20.75 |                           4.08 |
| COMPLIANCE                      |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| REGULATION                      |     5 |                164 |                22 |                           32.8  |                           4.4  |
| FINANCIAL_SERVICES              |     4 |                168 |                20 |                           42    |                           5    |
| FINANCIAL_REGULATION            |     4 |                 35 |                 8 |                            8.75 |                           2    |
| REGULATORY_TECHNOLOGY (REGTECH) |     4 |                 30 |                10 |                            7.5  |                           2.5  |
| ARTIFICIAL_INTELLIGENCE         |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| ANTI-MONEY_LAUNDERING           |     3 |                 21 |                 4 |                            7    |                           1.33 |
| RISK_MANAGEMENT                 |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
import plotly.express as px

from ...check_params import check_listview
from ...classes import BasicChart


def cleveland_dot_chart(
    obj,
    title=None,
    metric_label=None,
    field_label=None,
):
    """Creates a cleveland doc chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        metric_label (str, optional): Metric label. Defaults to None.
        field_label (str, optional): Field label. Defaults to None.

    Returns:
        BasicChart: A basic chart object.

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
            title_text=metric_label,
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            autorange="reversed",
            gridcolor="gray",
            griddash="solid",
            title_text=field_label,
        )
        return fig

    #
    # Main code
    #

    check_listview(obj)

    if metric_label is None:
        metric_label = obj.metric_.replace("_", " ").upper()

    if field_label is None:
        field_label = obj.field_.replace("_", " ").upper()

    chart = BasicChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart
