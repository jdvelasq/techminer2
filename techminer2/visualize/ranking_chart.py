# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Ranking Chart
===============================================================================

>>> from techminer2.visualize import ranking_chart
>>> chart = ranking_chart(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Author Keywords",
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/visualize/ranking_chart.html")

.. raw:: html

    <iframe src="../../../../_static/visualize/ranking_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> chart.df_.head()
                       rank_occ  OCC
author_keywords                     
REGTECH                       1   28
FINTECH                       2   12
REGULATORY_TECHNOLOGY         3    7
COMPLIANCE                    4    7
REGULATION                    5    5


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
| author_keywords         |   rank_occ |   OCC |
|:------------------------|-----------:|------:|
| REGTECH                 |          1 |    28 |
| FINTECH                 |          2 |    12 |
| REGULATORY_TECHNOLOGY   |          3 |     7 |
| COMPLIANCE              |          4 |     7 |
| REGULATION              |          5 |     5 |
| ANTI_MONEY_LAUNDERING   |          6 |     5 |
| FINANCIAL_SERVICES      |          7 |     4 |
| FINANCIAL_REGULATION    |          8 |     4 |
| ARTIFICIAL_INTELLIGENCE |          9 |     4 |
| RISK_MANAGEMENT         |         10 |     3 |
| INNOVATION              |         11 |     3 |
| BLOCKCHAIN              |         12 |     3 |
| SUPTECH                 |         13 |     3 |
| SEMANTIC_TECHNOLOGIES   |         14 |     2 |
| DATA_PROTECTION         |         15 |     2 |
| SMART_CONTRACTS         |         16 |     2 |
| CHARITYTECH             |         17 |     2 |
| ENGLISH_LAW             |         18 |     2 |
| ACCOUNTABILITY          |         19 |     2 |
| DATA_PROTECTION_OFFICER |         20 |     2 |
```
<BLANKLINE>
    

"""
import plotly.express as px

from ..performance_analysis.list_items import list_items

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def ranking_chart(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a rank chart.

    :meta private:
    """

    items = list_items(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    metric_label = metric.replace("_", " ").upper() if metric_label is None else metric_label

    field_label = (
        field.replace("_", " ").upper() + " RANKING" if field_label is None else field_label
    )

    data_frame = items.df_.copy()
    table = data_frame.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y=metric,
        hover_data=data_frame.columns.to_list(),
        markers=True,
    )

    fig.update_traces(
        marker={
            "size": marker_size,
            "line": {"color": MARKER_LINE_COLOR, "width": 1},
        },
        marker_color=MARKER_COLOR,
        line={"color": MARKER_LINE_COLOR, "width": line_width},
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=metric_label,
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
            y=row[metric],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    items.fig_ = fig

    return items
