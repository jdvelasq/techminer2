"""
Sankey Plot
===============================================================================



Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/techminer2plus__sankey_plot_0.html"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.sankey_plot(
...     root_dir=root_dir,
...     fields=["authors", "countries", "author_keywords"],
...     top_n=10,
...     max_n=20,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/techminer2plus__sankey_plot_0.html"
    height="800px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go

# from ...vantagepoint.analyze.co_occurrence_matrix import co_occurrence_matrix


def sankey_plot(
    # Specific params:
    fields,
    max_n=50,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Plot params:
    font_size=8,
    title=None,
    color=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Sankey plot"""

    def build_matrices():
        matrices = []

        for row, col in zip(fields[:-1], fields[1:]):
            #

            if row == fields[0]:
                # it is the first matrix

                coc_matrix = co_occurrence_matrix(
                    columns=col,
                    rows=row,
                    # Column item filters:
                    col_top_n=max_n,
                    # Row item filters:
                    row_top_n=top_n,
                    row_occ_range=occ_range,
                    row_gc_range=gc_range,
                    row_custom_items=custom_items,
                    # Database params:
                    root_dir=root_dir,
                    database=database,
                    year_filter=year_filter,
                    cited_by_filter=cited_by_filter,
                    **filters,
                )

                matrices.append(coc_matrix)

            else:
                curr_custom_items = matrices[-1].matrix_.columns.to_list()
                curr_custom_items = [
                    " ".join(item.split(" ")[:-1])
                    for item in curr_custom_items
                ]

                coc_matrix = co_occurrence_matrix(
                    columns=col,
                    rows=row,
                    # Columns item filters:
                    col_top_n=max_n,
                    # Rows item filters:
                    row_custom_items=curr_custom_items,
                    # Database params:
                    root_dir=root_dir,
                    database=database,
                    year_filter=year_filter,
                    cited_by_filter=cited_by_filter,
                    **filters,
                )

                matrices.append(coc_matrix)

        return matrices

    def build_node_names(matrices):
        """Builds the node indices"""

        node_names = []
        for i_matrix, matrix in enumerate(matrices):
            if i_matrix == 0:
                node_names.extend(matrix.matrix_.index.to_list())

            node_names.extend(matrix.matrix_.columns.to_list())

        return node_names

    def build_node_indexes(node_names):
        """Builds the node indices"""
        return {key: pos for pos, key in enumerate(node_names)}

    def build_links(matrices, node_indexes):
        """Links are a node dictionary with source, target and value"""

        source = []
        target = []
        value = []

        for coc_matrix in matrices:
            matrix = coc_matrix.matrix_

            for row in matrix.index:
                for col in matrix.columns:
                    source.append(node_indexes[row])
                    target.append(node_indexes[col])
                    value.append(matrix.loc[row, col])
        return {"source": source, "target": target, "value": value}

    def build_diagram(node_names, links, color, title, font_size):
        fig = go.Figure(
            data=[
                go.Sankey(
                    node={"label": node_names, "color": color},
                    link=links,
                )
            ]
        )
        fig.update_layout(title_text=title, font_size=font_size)

        return fig

    matrices = build_matrices()
    node_names = build_node_names(matrices)
    node_indexes = build_node_indexes(node_names)
    links = build_links(matrices, node_indexes)
    fig = build_diagram(node_names, links, color, title, font_size)

    return fig


#     matrix_left = co_occurrence_matrix(
#         columns=middle_criterion,
#         rows=left_criterion,
#         col_top_n=topics_length_left,
#         col_gc_range=topic_min_citations,
#         root_dir=directory,
#         database=database,
#         year_filter=start_year,
#         cited_by_filter=end_year,
#         **filters,
#     ).rows_

#     matrix_right = co_occ_matrix(
#         columns=right_criterion,
#         rows=middle_criterion,
#         col_top_n=topics_length_right,
#         col_gc_range=topic_min_citations,
#         root_dir=directory,
#         database=database,
#         year_filter=start_year,
#         cited_by_filter=end_year,
#     ).rows_

#     return _make_sankey_plot(matrix_left, matrix_right)


# def _make_sankey_plot(matrix_left, matrix_right):
#     left_labels = matrix_left.index.to_list()
#     middle_labels = list(
#         set(matrix_left.columns.to_list() + matrix_right.index.to_list())
#     )
#     right_labels = matrix_right.columns.to_list()

#     labels = left_labels + middle_labels + right_labels
#     labels = {key: pos for pos, key in enumerate(labels)}

#     connections_left = {
#         (labels[row], labels[col]): matrix_left.loc[row, col]
#         for row in matrix_left.index
#         for col in matrix_left.columns
#         if matrix_left.loc[row, col] != 0
#     }

#     connections_right = {
#         (labels[row], labels[col]): matrix_right.loc[row, col]
#         for row in matrix_right.index
#         for col in matrix_right.columns
#         if matrix_right.loc[row, col] != 0
#     }

#     connections = {**connections_left, **connections_right}

#     fig = go.Figure(
#         go.Sankey(
#             arrangement="snap",
#             node={
#                 "label": [key for key in labels.keys()],
#                 "x": [0] * len(left_labels)
#                 + [0.5] * len(middle_labels)
#                 + [1] * len(right_labels),
#                 "y": [0] * len(left_labels)
#                 + [0.01] * len(middle_labels)
#                 + [0.02] * len(right_labels),
#                 "pad": 10,
#                 "color": "#333",
#             },
#             link={
#                 "source": [key[0] for key in connections.keys()],
#                 "target": [key[1] for key in connections.keys()],
#                 "value": list(connections.values()),
#             },
#         )
#     )

#     fig.update_layout(
#         hovermode="x",
#         font={"size": 10, "color": "black"},
#     )

#     return fig
