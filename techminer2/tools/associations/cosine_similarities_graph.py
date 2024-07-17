# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Cosine Similarities Graph
===============================================================================


"""
import pandas as pd
import plotly.express as px
from sklearn.metrics.pairwise import cosine_similarity

from ...co_occurrence_matrix.compute_co_occurrence_matrix import compute_co_occurrence_matrix

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def cosine_similarities_graph(
    #
    # FUNCTION PARAMS:
    item,
    columns,
    rows=None,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    y_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Makes a butterfly chart.

    :meta private:
    """

    def extract_item_position_and_name(candidate_items, item):
        """Obtains the positions of topics in a list."""

        item = item[0]
        org_candidate_items = candidate_items[:]
        candidate_items = [col.split(" ")[:-1] for col in candidate_items]
        candidate_items = [" ".join(col) for col in candidate_items]
        pos = candidate_items.index(item)
        name = org_candidate_items[pos]
        return pos, name

    #
    # MAIN CODE:
    #
    cooc_matrix = compute_co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    similarities = pd.DataFrame(
        cosine_similarity(cooc_matrix),
        index=cooc_matrix.index,
        columns=cooc_matrix.columns,
    )

    item = [item]

    position, name = extract_item_position_and_name(similarities.columns.tolist(), item)

    similarities = similarities.iloc[:, [position]]
    similarities = similarities.sort_values(by=similarities.columns[0], ascending=False)

    #
    # Delete names from matrix.index if exists
    similarities = similarities.drop([name])

    #
    # Graph
    similarities["Rank"] = list(range(1, len(similarities) + 1))
    y_label = "Cosine similarity with " + item[0] if y_label is None else y_label

    field_label = columns.replace("_", " ").upper() + " RANKING" if field_label is None else field_label

    fig = px.line(
        similarities,
        x="Rank",
        y=similarities.columns[0],
        hover_data=similarities.columns.to_list(),
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

    for name, row in similarities.iterrows():
        fig.add_annotation(
            x=row["Rank"],
            y=row[similarities.columns[0]],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return fig
