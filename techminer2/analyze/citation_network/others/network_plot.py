# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network plot from others (fields)


"""
from ....internals.nx.nx_assign_colors_to_nodes_by_group_attribute import (
    nx_assign_colors_to_nodes_by_group_attribute,
)
from ....internals.nx.nx_assign_opacity_to_text_by_frequency import (
    nx_assign_opacity_to_text_by_frequency,
)
from ....internals.nx.nx_assign_sizes_to_nodes_by_occurrences import (
    _nx_assign_sizes_to_nodes_by_occurrences,
)
from ....internals.nx.nx_assign_text_positions_to_nodes_by_quadrants import (
    nx_assign_text_positions_to_nodes_by_quadrants,
)
from ....internals.nx.nx_assign_textfont_sizes_to_nodes_by_occurrences import (
    _nx_assign_textfont_sizes_to_nodes_by_occurrences,
)
from ....internals.nx.nx_assign_uniform_color_to_edges import (
    nx_assign_uniform_color_to_edges,
)
from ....internals.nx.nx_assign_widths_to_edges_by_weight import (
    _nx_assign_widths_to_edges_by_weight,
)
from ....internals.nx.nx_cluster_graph import nx_cluster_graph
from ....internals.nx.nx_compute_spring_layout_positions import (
    nx_compute_spring_layout_positions,
)
from ....internals.nx.nx_network_plot import nx_network_plot
from .internals.create_citation_nx_graph import _create_citation_nx_graph

UNIT_OF_ANALYSIS = "abbr_source_title"


def _network_plot(
    #
    # FIELD PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    occurrence_threshold=None,
    custom_terms=None,
    #
    # NETWORK CLUSTERING:
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(20, 70),
    textfont_size_range=(9, 12),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
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
    """:meta private:"""

    nx_graph = _create_citation_nx_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = nx_cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    nx_graph = nx_compute_spring_layout_positions(
        nx_graph=nx_graph,
        k=nx_k,
        iterations=nx_iterations,
        seed=nx_random_state,
    )

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout_positions(
        nx_graph, nx_k, nx_iterations, nx_random_state
    )

    #
    # Sets the node attributes
    nx_graph = nx_assign_colors_to_nodes_by_group_attribute(nx_graph)
    #
    nx_graph = _nx_assign_sizes_to_nodes_by_occurrences(nx_graph, node_size_range)
    nx_graph = _nx_assign_textfont_sizes_to_nodes_by_occurrences(
        nx_graph, textfont_size_range
    )
    nx_graph = nx_assign_opacity_to_text_by_frequency(nx_graph, textfont_opacity_range)

    #
    # Sets the edge attributes
    nx_graph = _nx_assign_widths_to_edges_by_weight(nx_graph, edge_width_range)
    nx_graph = nx_assign_text_positions_to_nodes_by_quadrants(nx_graph)
    nx_graph = nx_assign_uniform_color_to_edges(nx_graph, edge_color)

    return nx_network_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )
