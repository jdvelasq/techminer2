# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Butterfly Chart
===============================================================================



## >>> from techminer2.report import butterfly_chart
## >>> chart = butterfly_chart(
## ...     #
## ...     # COLUMN PARAMS:
## ...     item_a="FINTECH",
## ...     item_b="INNOVATION",
## ...     #
## ...     columns='author_keywords',
## ...     col_top_n=10,
## ...     col_occ_range=(None, None),
## ...     col_gc_range=(None, None),
## ...     col_custom_terms=None,
## ...     #
## ...     # ROW PARAMS:
## ...     rows=None,
## ...     row_top_n=None,
## ...     row_occ_range=(None, None),
## ...     row_gc_range=(None, None),
## ...     row_custom_terms=None,
## ...     #
## ...     # CHART PARAMS:
## ...     title=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # chart.write_html("sphinx/_static/report/butterfly_chart.html")

.. raw:: html

    <iframe src="../_static/report/butterfly_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go

from ..co_occurrence_matrix.co_occurrence_matrix import co_occurrence_matrix


def butterfly_chart(
    #
    # COLUMN PARAMS:
    item_a,
    item_b,
    #
    columns,
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_terms=None,
    #
    # ROW PARAMS:
    rows=None,
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_terms=None,
    #
    # CHART PARAMS:
    title=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    def extract_item_position_and_name(candidate_items, item):
        """Obtains the positions of topics in a list."""

        org_candidate_items = candidate_items[:]
        candidate_items = [col.split(" ")[:-1] for col in candidate_items]
        candidate_items = [" ".join(col) for col in candidate_items]
        pos = candidate_items.index(item)
        name = org_candidate_items[pos]
        return pos, name

    #
    # MAIN CODE:
    #
    matrix = co_occurrence_matrix(
        #
        # COLUMN PARAMS:
        columns=columns,
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_terms=col_custom_terms,
        #
        # ROW PARAMS:
        rows=rows,
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

    pos_a, name_a = extract_item_position_and_name(matrix.columns.tolist(), item_a)
    pos_b, name_b = extract_item_position_and_name(matrix.columns.tolist(), item_b)

    matrix = matrix.iloc[:, [pos_a, pos_b]]

    # Delete name_a and name_b from matrix.index if exists
    if name_a in matrix.index:
        matrix = matrix.drop([name_a])
    if name_b in matrix.index:
        matrix = matrix.drop([name_b])

    # delete rows with all zeros
    matrix = matrix.loc[(matrix != 0).any(axis=1)]

    x_max_value = matrix.max().max()

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=matrix.index,
            x=matrix[name_a],
            name=name_a,
            orientation="h",
            marker={"color": "#7793a5"},
        )
    )

    fig.add_trace(
        go.Bar(
            y=matrix.index,
            x=matrix[name_b].map(lambda w: -w),
            name=name_b,
            orientation="h",
            marker={"color": "#465c6b"},
        )
    )

    # puts yaxis at x = 0
    # fig.update_layout(
    #     xaxis={
    #         "zeroline": False,
    #         "zerolinecolor": "gray",
    #         "zerolinewidth": 2,
    #     }
    # )

    # draw a vertical line at x=0
    # fig.add_shape(
    #     type="line",
    #     x0=0,
    #     y0=matrix.index[0],
    #     x1=0,
    #     y1=matrix.index[-1],
    #     line=dict(
    #         color="gray",
    #         width=1,
    #     ),
    # )

    fig.update_layout(barmode="overlay")

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.add_vline(
        x=0.0,
        line={
            "color": "lightgray",
            "width": 2,
            "dash": "dot",
        },
    )

    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text="OCC",
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=0,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
        # title_text=field_label,
    )

    # sets xaxis range to (-x_max_value, x_max_value)
    fig.update_layout(
        xaxis_range=[-x_max_value, x_max_value],
    )

    # sets the legend position upper left
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        )
    )

    return fig
