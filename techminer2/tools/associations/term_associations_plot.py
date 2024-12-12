# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Term Associations Plot
===============================================================================


>>> from techminer2.tools.associations import term_associations_plot
>>> plot = term_associations_plot(
...     #
...     # FUNCTION PARAMS:
...     item='FINTECH',
...     #
...     # CO-OCC PARAMS:
...     columns='author_keywords',
...     rows=None,
...     #
...     # COLUMN PARAMS:
...     col_top_n=20,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_terms=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_terms=None,
...     #
...     # CHART PARAMS:
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> plot.write_html("sphinx/_static/tools/associations/term_associations_plot.html")

.. raw:: html

    <iframe src="../../_static/tools/associations/term_associations_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from dataclasses import dataclass

import plotly.express as px  # type: ignore

from ...analyze.co_occurrence_matrix.co_occurrence_matrix import co_occurrence_matrix
from ...helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes
from .term_associations_frame import term_associations_frame

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def term_associations_plot(
    #
    # FUNCTION PARAMS:
    item,
    #
    # CO-OCC PARAMS:
    columns,
    rows=None,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_terms=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_terms=None,
    #
    # CHART PARAMS:
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    data_frame = term_associations_frame(
        #
        # FUNCTION PARAMS:
        item=item,
        #
        # CO-OCC PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_terms=col_custom_terms,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_terms=row_custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = _make_fig(
        data_frame,
        #
        # CO-OCC PARAMS:
        columns=columns,
        rows=rows,
        #
        # CHART PARAMS:
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
    )

    return fig


def _make_fig(
    data_frame,
    #
    # CO-OCC PARAMS:
    columns,
    rows=None,
    #
    # CHART PARAMS:
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
):
    """association plot"""

    item_name = data_frame.iloc[:, 0].name
    item_name = " ".join(item_name.split(" ")[:-1])
    series_name = data_frame.iloc[:, 0].index.name
    title = f"Co-occurrence of '{item_name}' with '{series_name}'"

    data_frame = data_frame.copy()
    data_frame.columns = ["OCC"]

    if rows is None:
        rows = columns

    metric_label = "OCC" if metric_label is None else metric_label

    field_label = rows.replace("_", " ").upper() + " RANKING" if field_label is None else field_label

    table = data_frame.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y="OCC",
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
            y=row["OCC"],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return fig
