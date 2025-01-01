# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrences Chart
===============================================================================


>>> from techminer2.tools.associations import co_occurrences_chart
>>> plot = co_occurrences_chart(
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
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
>>> # plot.write_html("sphinx/_static/tools/associations/co_occurrences.html")

.. raw:: html

    <iframe src="../../_static/tools/associations/co_occurrences.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""
import plotly.express as px  # type: ignore

from .dataframe import DataFrame

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def co_occurrences_chart(
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
    y_label=None,
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

    associations = term_associations_frame(
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

    associations = associations.copy()
    associations["occ"] = associations.index.copy()
    associations["occ"] = associations["occ"].str.split(" ")
    associations["occ"] = associations["occ"].str[-1]
    associations["occ"] = associations["occ"].str.split(":")
    associations["gc"] = associations["occ"].str[1]
    associations["occ"] = associations["occ"].str[0]

    associations["percentage"] = (
        associations.iloc[:, 0] / associations["occ"].astype(float) * 100
    )
    associations["percentage"] = associations["percentage"].round(2)
    associations["name"] = associations.index.copy()

    associations = associations.sort_values(
        by=["percentage", "occ", "gc", "name"], ascending=[False, False, False, True]
    )

    #
    # Graph
    associations["Rank"] = list(range(1, len(associations) + 1))

    y_label = r"% of Co-occurrence with " + item if y_label is None else y_label

    title = f"(%) Co-occurrences with '{item}'"

    if field_label is None:
        field_label = columns.replace("_", " ").upper() + " RANKING"

    data_frame = associations.copy()

    fig = px.line(
        data_frame,
        x="Rank",
        y=data_frame.percentage,
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
        title=y_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=field_label,
    )

    for name, row in data_frame.iterrows():
        fig.add_annotation(
            x=row["Rank"],
            y=row.percentage,
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return fig
