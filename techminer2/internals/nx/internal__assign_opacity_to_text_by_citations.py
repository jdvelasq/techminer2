# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

#
# In networkx, the size of the node is specified by the 'node_size' parameter.
# Example: nx.draw_networkx_nodes(G, pos, node_size=node_sizes)
import numpy as np


def internal__assign_opacity_to_text_by_citations(
    nx_graph,
    textfont_opacity_range,
):
    #
    # Extracs occurrences from node names. Example: 'regtech 10:100' -> 10
    citations = list(nx_graph.nodes())
    citations = [node.split(" ")[-1] for node in citations]
    citations = [node.split(":")[0] for node in citations]
    citations = np.array([int(node) for node in citations])

    #
    # Set the lower value of the node size to node_size_min
    min_citations = min(citations)
    textfont_opacities = citations - min_citations + textfont_opacity_range[0]

    #
    # Checks if node_sizes.max() > node_size_max and, if so, rescales
    if textfont_opacities.max() > textfont_opacity_range[1]:
        #
        # Scales the node size to the range [node_size_min, node_size_max]
        textfont_opacities -= textfont_opacity_range[0]
        textfont_opacities /= textfont_opacities.max()
        textfont_opacities *= textfont_opacity_range[1] - textfont_opacity_range[0]
        textfont_opacities += textfont_opacity_range[0]

    #
    # Sets the value of node_size
    for opacity, node in zip(textfont_opacities, nx_graph.nodes()):
        nx_graph.nodes[node]["textfont_opacity"] = np.sqrt(opacity)

    return nx_graph
