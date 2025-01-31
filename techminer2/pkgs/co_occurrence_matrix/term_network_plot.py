# flake8: noqa
# pylint: disable = invalid - name
# pylint: disable = line - too - long
# pylint: disable = missing - docstring
# pylint: disable = too - many - arguments
# pylint: disable = too - many - locals
# pylint: disable = too - many - statements
"""
Chart
===============================================================================


## >>> from techminer2.visualize.specialized_plots.word_network import chart
## >>> plot = chart(
## ...     #
## ...     # FUNCTION PARAMS:
## ...     item='INNOVATION',
## ...     #
## ...     # COLUMNS:
## ...     .with_field("author_keywords")
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(2, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # ROWS:
## ...     .wiht_other_field("authors")
## ...     .having_other_terms_in_top(10)
## ...     .having_other_terms_ordered_by(None)
## ...     .having_other_term_occurrences_between(None, None)
## ...     .having_other_term_citations_between(None, None)
## ...     .having_other_terms_in(None)
## ...     #
## ...     # NETWORK:
## ...     .using_spring_layout_k(None)
## ...     .using_spring_layout_iterations(30)
## ...     .using_spring_layout_seed(0)
## 
## ...     #
## ...     # NODES:
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_size_range(10, 20)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...     #
## ...     # EDGES
## ...     edge_color="#b8c6d0",
## ...     edge_width_range=(0.8, 4.0),
## ...     .using_xaxes_range=(None, None)
## ...     .using_yaxes_range=(None, None)
## ...     .using_axes_visible(False)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> # plot.write_html("sphinx/_generated/visualize/specialized_charts/word_network/chart_0.html")

.. raw:: html

    <iframe src="../../../_generated/visualize/specialized_charts/word_network/chart_0.html"
    height="600px" width="100%" frameBorder="0"></iframe>


## >>> from techminer2.visualize.specialized_plots.word_network import chart
## >>> plot = chart(
## ...     #
## ...     # FUNCTION PARAMS:
## ...     item='FINANCIAL_SERVICES',
## ...     columns='author_keywords',
## ...     rows=None,
## ...     #
## ...     # COLUMN PARAMS:
## ...     col_top_n=10,
## ...     col_occ_range=(None, None),
## ...     col_gc_range=(None, None),
## ...     col_custom_terms=None,
## ...     #
## ...     # ROW PARAMS:
## ...     row_top_n=None,
## ...     row_occ_range=(None, None),
## ...     row_gc_range=(None, None),
## ...     row_custom_terms=None,
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     #
## ...     # NODES:
## ...     node_size_range=(30, 70),
## ...     textfont_size_range=(10, 20),
## ...     textfont_opacity_range=(0.35, 1.00),
## ...     #
## ...     # EDGES
## ...     edge_color="#b8c6d0",
## ...     edge_width_range=(0.8, 4.0),
## ...     ).set_axes_params(
## ...         xaxes_range=None,
## ...         yaxes_range=None,
## ...         show_axes=False,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/",
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_generated/visualize/specialized_charts/word_network/chart_1.html")

.. raw:: html
    <iframe src="../../../_generated/visualize/specialized_charts/word_network/chart_1.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
# from ....analyze.associations.term_associations.dataframe import DataFrame
# from ....analyze.co_occurrence_matrix.co_occurrence_matrix_network import (
#     co_occurrence_matrix_network,
# )


# def chart(
#     #
#     # FUNCTION PARAMS:
#     item,
#     columns,
#     rows=None,
#     #
#     # COLUMN PARAMS:
#     col_top_n=None,
#     col_occ_range=(None, None),
#     col_gc_range=(None, None),
#     col_custom_terms=None,
#     #
#     # ROW PARAMS:
#     row_top_n=None,
#     row_occ_range=(None, None),
#     row_gc_range=(None, None),
#     row_custom_terms=None,
#     #
#     # LAYOUT:
#     nx_k=None,
#     nx_iterations=30,
#     nx_random_state=0,
#     #
#     # NODES:
#     node_size_range=(30, 70),
#     textfont_size_range=(10, 20),
#     textfont_opacity_range=(0.35, 1.00),
#     #
#     # EDGES
#     edge_color="#b8c6d0",
#     edge_width_range=(0.8, 4.0),
#     #
#     # AXES:
#     xaxes_range=None,
#     yaxes_range=None,
#     show_axes=False,
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
#     database="main",
#     year_filter=(None, None),
#     cited_by_filter=(None, None),
#     **filters,
# ):
#     """:meta private:"""

#     associations = term_associations_frame(
#         #
#         # FUNCTION PARAMS:
#         item=item,
#         #
#         # CO-OCC PARAMS:
#         columns=columns,
#         rows=rows,
#         #
#         # COLUMN PARAMS:
#         col_top_n=col_top_n,
#         col_occ_range=col_occ_range,
#         col_gc_range=col_gc_range,
#         col_custom_terms=col_custom_terms,
#         #
#         # ROW PARAMS:
#         row_top_n=row_top_n,
#         row_occ_range=row_occ_range,
#         row_gc_range=row_gc_range,
#         row_custom_terms=row_custom_terms,
#         #
#         # DATABASE PARAMS:
#         root_dir=root_dir,
#         database=database,
#         year_filter=(None, None),
#         cited_by_filter=(None, None),
#         **filters,
#     )

#     #
#     # Build a list of associated terms
#     terms = associations[associations.iloc[:, 0] > 0].index.tolist()
#     terms = terms + associations.columns.tolist()
#     terms = list(set(terms))
#     terms = [" ".join(item.split(" ")[:-1]) for item in terms]

#     #
#     # Returb the network
#     return co_occurrence_matrix_network(
#         #
#         # FUNCTION PARAMS:
#         columns=columns,
#         rows=rows,
#         #
#         # COLUMN PARAMS:
#         col_top_n=None,
#         col_occ_range=(None, None),
#         col_gc_range=(None, None),
#         col_custom_terms=terms,
#         #
#         # ROW PARAMS:
#         row_top_n=None,
#         row_occ_range=(None, None),
#         row_gc_range=(None, None),
#         row_custom_terms=terms,
#         #
#         # LAYOUT:
#         nx_k=nx_k,
#         nx_iterations=nx_iterations,
#         nx_random_state=nx_random_state,
#         #
#         # NODES:
#         node_size_range=node_size_range,
#         textfont_size_range=textfont_size_range,
#         textfont_opacity_range=textfont_opacity_range,
#         #
#         # EDGES
#         edge_color=edge_color,
#         edge_width_range=edge_width_range,
#         #
#         # AXES:
#         xaxes_range=xaxes_range,
#         yaxes_range=yaxes_range,
#         show_axes=show_axes,
#         #
#         # DATABASE PARAMS:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
