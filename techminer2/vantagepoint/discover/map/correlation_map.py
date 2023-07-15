# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx
import numpy as np
import plotly.express as px

from ....vosviewer.nx_utils import (
    nx_compute_spring_layout,
    nx_compute_textposition,
    nx_scale_node_size_prop_to_occ_property,
    nx_scale_textfont_opacity_prop_to_occ_property,
    nx_scale_textfont_size_prop_to_occ_property,
)
from ....vosviewer.px_utils import px_create_network_chart


def correlation_map(
    similarity,
    #
    # FUNCTION PARAMS:
    n_labels=None,
    color="#7793a5",
    nx_k=None,
    nx_iterations=10,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    #
    # Create a empty networkx graph
    #
    nx_graph = nx.Graph()

    #
    # Creates the nodes of the graph
    #
    nodes = similarity.index.tolist()

    for node in nodes:
        nx_graph.add_nodes_from(
            #
            # NODE NAME:
            [node],
            #
            # NODE ATTR:
            text=" ".join(node.split(" ")[:-1]),
            OCC=int(node.split(" ")[-1].split(":")[0]),
            global_citations=int(node.split(" ")[-1].split(":")[0]),
            #
            # OTHER ATTR:
            group=0,
            color=color,
            # node_size=node_size,
            # textfont_color=textfont_color,
            # textfont_size=textfont_size,
        )

    #
    # Scales the node size
    nx_graph = nx_scale_node_size_prop_to_occ_property(
        nx_graph, node_size_min, node_size_max
    )

    #
    # Scales the font size
    nx_graph = nx_scale_textfont_size_prop_to_occ_property(
        nx_graph, textfont_size_min, textfont_size_max
    )

    #
    # Scales the font color
    nx_graph = nx_scale_textfont_opacity_prop_to_occ_property(
        nx_graph,
        textfont_opacity_min=0.35,
        textfont_opacity_max=1.00,
    )

    #
    #
    # Adds edges to the graph
    #
    #
    for i_row in range(similarity.shape[0]):
        for i_col in range(i_row + 1, similarity.shape[1]):
            if similarity.iloc[i_row, i_col] > 0:
                #
                source_node = similarity.index[i_row]
                target_node = similarity.columns[i_col]
                weight = similarity.iloc[i_row, i_col]

                #
                # Sets the properties for correlation maps
                #
                if weight < 0.25:
                    width, dash = 2, "dot"

                elif weight < 0.5:
                    width, dash = 2, "dash"

                elif weight < 0.75:
                    width, dash = 4, "solid"

                else:
                    width, dash = 6, "solid"

                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(source_node, target_node, weight)],
                    width=width,
                    dash=dash,
                    color="#b8c6d0",
                )

    nx_graph = nx_compute_spring_layout(
        graph=nx_graph, k=nx_k, iterations=nx_iterations, seed=nx_random_state
    )

    nx_graph = nx_compute_textposition(nx_graph)

    fig = px_create_network_chart(
        nx_graph=nx_graph,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
        n_labels=n_labels,
    )

    return fig
