# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Word Network
===============================================================================


>>> from techminer2.co_occurrence import word_network
>>> word_network(
...     #
...     # FUNCTION PARAMS:
...     item='FINANCIAL_SERVICES',
...     columns='author_keywords',
...     rows='authors',
...     #
...     # COLUMN PARAMS:
...     col_top_n=10,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=10,    
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_size_min=30,
...     node_size_max=70,
...     textfont_size_min=10,
...     textfont_size_max=20,
...     textfont_opacity_min=0.35,
...     textfont_opacity_max=1.00,
...     #
...     # EDGES
...     edge_color="#b8c6d0",
...     edge_width_min=0.8,
...     edge_width_max=4.0,
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_occurrence/word_network_0.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence/word_network_0.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> word_network(
...     #
...     # FUNCTION PARAMS:
...     item='FINANCIAL_SERVICES',
...     columns='author_keywords',
...     rows=None,
...     #
...     # COLUMN PARAMS:
...     col_top_n=10,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,    
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_size_min=30,
...     node_size_max=70,
...     textfont_size_min=10,
...     textfont_size_max=20,
...     textfont_opacity_min=0.35,
...     textfont_opacity_max=1.00,
...     #
...     # EDGES
...     edge_color="#b8c6d0",
...     edge_width_min=0.8,
...     edge_width_max=4.0,
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_occurrence/word_network_1.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence/word_network_1.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
"""
from .item_associations import item_associations
from .matrix_viewer import matrix_viewer


def word_network(
    #
    # FUNCTION PARAMS:
    item,
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
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
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
    """Makes network map from a co-ocurrence matrix.

    :meta private:
    """

    associations = item_associations(
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
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
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
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=(None, None),
        cited_by_filter=(None, None),
        **filters,
    )

    #
    # Build a list of associated terms
    items = associations.df_[associations.df_.iloc[:, 0] > 0].index.tolist()
    items = items + associations.df_.columns.tolist()
    items = list(set(items))
    items = [" ".join(item.split(" ")[:-1]) for item in items]

    #
    # Returb the network
    return matrix_viewer(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=None,
        col_occ_range=(None, None),
        col_gc_range=(None, None),
        col_custom_items=items,
        #
        # ROW PARAMS:
        row_top_n=None,
        row_occ_range=(None, None),
        row_gc_range=(None, None),
        row_custom_items=items,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        textfont_opacity_min=textfont_opacity_min,
        textfont_opacity_max=textfont_opacity_max,
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
