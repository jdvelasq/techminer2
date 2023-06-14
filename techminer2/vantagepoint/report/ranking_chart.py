# flake8: noqa
"""
Ranking Chart (*)
===============================================================================

Default visualization chart for Bibliometrix.

Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__ranking_chart.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_items(
...    field='author_keywords',
...    root_dir=root_dir,
... )
>>> chart = vantagepoint.report.ranking_chart(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__ranking_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


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
| ANTI_MONEY_LAUNDERING           |     4 |                 23 |                 4 |                            5.75 |                           1    |
| RISK_MANAGEMENT                 |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
import plotly.express as px

from ...check_params import check_listview
from ...classes import BasicChart


# pylint: disable=too-many-arguments
def ranking_chart(
    obj,
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
):
    """Creates a rank chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        metric_label (str, optional): Metric label. Defaults to None.
        field_label (str, optional): Field label. Defaults to None.
        textfont_size (int, optional): Font size. Defaults to 10.
        marker_size (int, optional): Marker size. Defaults to 6.
        line_color (str, optional): Line color. Defaults to "black".
        line_width (int, optional): Line width. Defaults to 1.
        yshift (int, optional): Y shift. Defaults to 4.

    Returns:
        BasicChart: A basic chart object.

    """

    def create_plot():
        """Plots the degree of a co-occurrence matrix."""

        table = obj.table_.copy()
        table["Rank"] = list(range(1, len(table) + 1))

        fig = px.line(
            table,
            x="Rank",
            y=obj.metric_,
            hover_data=obj.table_.columns.to_list(),
            markers=True,
        )

        fig.update_traces(
            marker={
                "size": marker_size,
                "line": {"color": line_color, "width": 0},
            },
            marker_color=line_color,
            line={"color": line_color, "width": line_width},
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=obj.metric_.replace("_", " ").upper(),
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=field_label,
        )

        for name, row in table.iterrows():
            fig.add_annotation(
                x=row["Rank"],
                y=row[obj.metric_],
                text=name,
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": textfont_size},
                yshift=yshift,
            )

        return fig

    #
    # Main code
    #

    check_listview(obj)

    if title is None:
        title = ""

    if metric_label is None:
        metric_label = obj.metric_.replace("_", " ").upper()

    if field_label is None:
        field_label = obj.field_.replace("_", " ").upper() + " RANKING"

    chart = BasicChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart
