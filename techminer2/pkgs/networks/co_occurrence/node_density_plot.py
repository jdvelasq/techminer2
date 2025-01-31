# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Density Plot
===============================================================================


## >>> from techminer2.analyze.co_occurrence_network import NodeDensityPlot
## >>> plot = (
## ...     NodeDensityPlot()
## ...     .set_analysis_params(
## ...         association_index="association",
## ...     #
## ...     ).set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     #
## ...     ).set_plot_params(
## ...         textfont_size_range=(10, 20),
## ...         bandwidth=0.1,
## ...         colorscale="Aggrnyl",
## ...         opacity=0.6,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> # plot.write_html("sphinx/_static/co_occurrence_network/node_density_plot.html")

.. raw:: html

    <iframe src="../_static/co_occurrence_network/node_density_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from ....internals.nx.internal__assign_textfont_sizes_to_nodes_by_occurrences import (
    nx_assign_textfont_sizes_to_nodes_by_occurrences,
)
from ....internals.nx.internal__cluster_graph import internal__cluster_graph
from ....internals.nx.internal__compute_spring_layout_positions import (
    internal__compute_spring_layout_positions,
)
from ....internals.nx.internal__create_network_density_plot import (
    internal__create_network_density_plot,
)
from ...co_occurrence_matrix.internals.create_co_occurrence_nx_graph import (
    _create_co_occurrence_nx_graph,
)


def node_density_plot(
    #
    # PARAMS:
    field,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    association_index="association",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # DENSITY VISUALIZATION:
    bandwidth="silverman",
    colorscale="Aggrnyl",
    opacity=0.6,
    textfont_size_range=(10, 20),
    #
    # AXES:
    # xaxes_range=None,
    # yaxes_range=None,
    # show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = _create_co_occurrence_nx_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # NETWORK PARAMS:
        association_index=association_index,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = internal__cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    nx_graph = internal__compute_spring_layout_positions(
        nx_graph=nx_graph,
        k=nx_k,
        iterations=nx_iterations,
        seed=nx_random_state,
    )

    nx_graph = nx_assign_textfont_sizes_to_nodes_by_occurrences(
        nx_graph, textfont_size_range
    )

    return internal__create_network_density_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        bandwidth=bandwidth,
        colorscale=colorscale,
        opacity=opacity,
        # xaxes_range=xaxes_range,
        # yaxes_range=yaxes_range,
        # show_axes=show_axes,
    )
