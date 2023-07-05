# flake8: noqa
# pylint: disable=line-too-long
"""
.. _sankey_plot:

Sankey Plot
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> file_name = "sphinx/_static/sankey_plot_0.html"
>>> (
...     tm2p.records(root_dir=root_dir)
...     .sankey_plot(
...         fields=["authors", "countries", "author_keywords"],
...         top_n=10,
...         max_n=20,
...     )
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/sankey_plot_0.html" height="800px" width="100%" frameBorder="0"></iframe>



* Functional interface

>>> file_name = "sphinx/_static/sankey_plot_1.html"
>>> tm2p.sankey_plot(
...     root_dir=root_dir,
...     fields=["authors", "countries", "author_keywords"],
...     top_n=10,
...     max_n=20,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/sankey_plot_1.html" height="800px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go

from .co_occurrence_matrix import co_occurrence_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def sankey_plot(
    #
    # PARAMS:
    fields,
    max_n=50,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # PARAMS:
    font_size=8,
    title=None,
    color=None,
    #
    # DATABASE PARAMS:
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
                curr_custom_items = matrices[-1].df_.columns.to_list()
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
                node_names.extend(matrix.df_.index.to_list())

            node_names.extend(matrix.df_.columns.to_list())

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
            matrix = coc_matrix.df_

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
                    node={
                        "label": node_names,
                        "color": color,
                    },
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
