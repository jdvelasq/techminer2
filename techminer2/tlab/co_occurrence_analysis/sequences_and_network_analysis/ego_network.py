# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ego Network
===============================================================================

>>> from techminer2 import tlab
>>> root_dir = "data/regtech/"
>>> tlab.co_occurrence_analysis.sequences_and_network_analysis.ego_network(
...    item='ANTI_MONEY_LAUNDERING',
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... ).write_html("sphinx/_static/tlab/co_occurrence_analysis/sequences_and_network_analysis/ego_network.html")

.. raw:: html

    <iframe src="../../../../../_static/tlab/co_occurrence_analysis/sequences_and_network_analysis/ego_network.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



"""
from ....vantagepoint.discover.matrix.co_occurrence_matrix import co_occurrence_matrix
from ....vantagepoint.explore.matrix_viewer import matrix_viewer


def ego_network(
    item,
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
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
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size=30,
    textfont_size=10,
    #
    # EDGES
    edge_color="#b8c6d0",
    edge_width_min=0.8,
    edge_width_max=4.0,
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    def remove_counters(matrix):
        #
        matrix = matrix.copy()

        index = matrix.index.tolist()
        index = [" ".join(idx.split(" ")[:-1]) for idx in index]

        cols = matrix.columns.tolist()
        cols = [" ".join(col.split(" ")[:-1]) for col in cols]

        matrix.index = index
        matrix.columns = cols

        return matrix

    def extract_custom_items_from_matrix(matrix, name):
        #
        matrix = matrix.copy()

        #
        # Extracts associated terms from rows
        row_custom_items = matrix.loc[:, name]
        row_custom_items = row_custom_items[row_custom_items > 0]
        row_custom_items = row_custom_items.index.tolist()

        #
        # Extracts associated terms from columns
        col_custom_items = [name]
        col_custom_items += [idx for idx in row_custom_items if idx in matrix.columns.tolist()]

        return row_custom_items, col_custom_items

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

    matrix = remove_counters(matrix)
    row_custom_items, col_custom_items = extract_custom_items_from_matrix(matrix, item)

    return matrix_viewer(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        ## col_top_n=None,
        ## col_occ_range=(None, None),
        ## col_gc_range=(None, None),
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        ## row_top_n=None,
        ## row_occ_range=(None, None),
        ## row_gc_range=(None, None),
        row_custom_items=row_custom_items,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size=node_size,
        textfont_size=textfont_size,
        #
        # EDGES
        edge_color=edge_color,
        edge_width_min=edge_width_min,
        edge_width_max=edge_width_max,
        #
        # AXES:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
