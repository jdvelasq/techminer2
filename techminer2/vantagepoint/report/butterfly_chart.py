# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _butterfly_chart:

Butterfly Chart
===============================================================================



>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> heat_map = vantagepoint.report.butterfly_chart(
...     columns='author_keywords',
...     col_top_n=10,
...     root_dir=root_dir,
...     item_a="ARTIFICIAL_INTELLIGENCE",
...     item_b="REGTECH",
... ).write_html("sphinx/_static/butterfly_chart.html")

.. raw:: html

    <iframe src="../../../../_static/butterfly_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go

from ..discover.matrix.co_occurrence_matrix import co_occurrence_matrix


def butterfly_chart(
    #
    # FUNCTION PARAMS:
    item_a,
    item_b,
    columns,
    rows=None,
    #
    # CHART PARAMS:
    title=None,
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
    """Makes a butterfly chart."""

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

    pos_a, name_a = extract_item_position_and_name(
        matrix.columns.tolist(), item_a
    )
    pos_b, name_b = extract_item_position_and_name(
        matrix.columns.tolist(), item_b
    )

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
            marker={"color": "#8da4b4"},
        )
    )

    fig.add_trace(
        go.Bar(
            y=matrix.index,
            x=matrix[name_b].map(lambda w: -w),
            name=name_b,
            orientation="h",
            marker={"color": "#556f81"},
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
        # title_text=title if title is not None else "",
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


# import plotly.express as px

# from ...classes import WordComparison
# from ...counters_lib import add_counters_to_column_values
# from ...indicators.indicators_by_field import indicators_by_field
# from ...filtering_lib import generate_custom_items
# from ...load_utils import load_stopwords
# from ...records_lib import read_records
# from ...sorting_lib import sort_indicators_by_metric


# def comparison_between_word_pairs(
#     field,
#     item_a,
#     item_b,
#     # Item filters:
#     top_n=None,
#     occ_range=None,
#     gc_range=None,
#     custom_items=None,
#     # Database params:
#     root_dir="./",
#     database="main",
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """Comparison between topics."""

#     matrix_list = _create_comparison_matrix_list(
#         item_a=item_a,
#         item_b=item_b,
#         field=field,
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     matrix_list = _remove_stopwords(
#         root_dir,
#         matrix_list,
#     )

#     matrix_list = _select_topics(
#         matrix_list=matrix_list,
#         occ_range=occ_range,
#         gc_range=gc_range,
#         top_n=top_n,
#         custom_items=custom_items,
#         field=field,
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     matrix_list = add_counters_to_column_values(
#         criterion=field,
#         name="column",
#         root_dir=root_dir,
#         database=database,
#         table=matrix_list,
#         start_year=year_filter,
#         end_year=cited_by_filter,
#         **filters,
#     )

#     matrix_list = _sort_matrix_list(matrix_list)
#     matrix_list = matrix_list.reset_index(drop=True)

#     wordcomparison = WordComparison()
#     wordcomparison.table_ = matrix_list
#     wordcomparison.plot_ = _create_bart_chart(matrix_list, item_a, item_b)

#     return wordcomparison


# def _create_bart_chart(matrix_list, topic_a, topic_b):
#     matrix_list = matrix_list.copy()

#     fig = px.bar(
#         matrix_list,
#         x="OCC",
#         y="column",
#         color="row",
#         title="Co-occurrences between topics",
#         hover_data=["OCC"],
#         orientation="h",
#         color_discrete_map={
#             topic_a: "#CCD3D9",
#             topic_b: "#99A8B3",
#             " & ".join(sorted([topic_a, topic_b])): "#556f81",
#         },
#     )
#     fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
#     fig.update_yaxes(
#         linecolor="gray",
#         linewidth=2,
#         autorange="reversed",
#     )
#     fig.update_xaxes(
#         linecolor="gray",
#         linewidth=2,
#         gridcolor="gray",
#         griddash="dot",
#     )

#     fig.update_layout(
#         yaxis_title=None,
#     )

#     return fig


# def _select_topics(
#     matrix_list,
#     occ_range,
#     gc_range,
#     top_n,
#     custom_items,
#     field,
#     root_dir,
#     database,
#     year_filter,
#     cited_by_filter,
#     **filters,
# ):
#     indicators = indicators_by_field(
#         field=field,
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     indicators = sort_indicators_by_metric(indicators, metric="OCC")

#     if custom_items is None:
#         custom_items = generate_custom_items(
#             indicators=indicators,
#             top_n=top_n,
#             occ_range=occ_range,
#             gc_range=gc_range,
#         )

#     matrix_list = matrix_list.loc[matrix_list.column.isin(custom_items), :]

#     return matrix_list


# def _remove_stopwords(directory, matrix_list):
#     stopwords = load_stopwords(directory)
#     matrix_list = matrix_list[~matrix_list["column"].isin(stopwords)]
#     return matrix_list


# def _create_comparison_matrix_list(
#     item_a,
#     item_b,
#     field,
#     root_dir,
#     database,
#     year_filter,
#     cited_by_filter,
#     **filters,
# ):
#     records = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     matrix_list = records[[field]].copy()
#     matrix_list = matrix_list.dropna()
#     matrix_list = matrix_list.rename(columns={field: "column"})
#     matrix_list = matrix_list.assign(row=records[[field]])

#     # Explode 'row' for topic_a and topic_b
#     matrix_list["row"] = matrix_list["row"].str.split(";")
#     matrix_list["row"] = matrix_list["row"].map(
#         lambda x: [y.strip() for y in x]
#     )
#     matrix_list = matrix_list[
#         matrix_list["row"].map(
#             lambda x: any([y in [item_a, item_b] for y in x])
#         )
#     ]

#     matrix_list["row"] = matrix_list["row"].map(
#         lambda x: sorted([y for y in x if y in [item_a, item_b]])
#     )
#     matrix_list["row"] = matrix_list["row"].str.join(" & ")
#     matrix_list = matrix_list.explode("row")
#     matrix_list["row"] = matrix_list["row"].str.strip()

#     # Explode 'column' for all topics
#     matrix_list["column"] = matrix_list["column"].str.split(";")
#     matrix_list = matrix_list.explode("column")
#     matrix_list["column"] = matrix_list["column"].str.strip()
#     matrix_list = matrix_list[
#         matrix_list["column"].map(lambda x: x not in [item_a, item_b])
#     ]

#     # count
#     matrix_list["OCC"] = 1
#     matrix_list = matrix_list.groupby(
#         ["row", "column"], as_index=False
#     ).aggregate("sum")

#     matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
#     matrix = matrix.fillna(0)
#     if " & ".join([item_a, item_b]) not in matrix.index.to_list():
#         matrix.loc[" & ".join(sorted([item_a, item_b]))] = 0

#     matrix_list = matrix.melt(
#         value_name="OCC", var_name="column", ignore_index=False
#     )

#     matrix_list = matrix_list.reset_index()
#     matrix_list["OCC"] = matrix_list["OCC"].astype(int)

#     return matrix_list


# def _sort_matrix_list(matrix_list):
#     indicators = matrix_list.copy()
#     indicators = indicators[["column", "OCC"]]
#     indicators = indicators.groupby("column", as_index=False).aggregate("sum")
#     indicators = indicators.sort_values(by=["OCC"], ascending=False)
#     sorted_topics = indicators["column"]
#     topics2rank = {topic: i for i, topic in enumerate(sorted_topics)}

#     matrix_list["rank"] = matrix_list["column"].map(topics2rank)
#     matrix_list = matrix_list.sort_values(by=["rank"], ascending=True)
#     matrix_list = matrix_list.drop(columns=["rank"])

#     return matrix_list
