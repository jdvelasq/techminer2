"""
Network Map (Deprecated)
===============================================================================



# >>> directory = "data/regtech/"
# >>> file_name = "sphinx/images/co_occurrence_network_map.png"

# >>> from techminer2 import vantagepoint__co_occ_matrix_list
# >>> from techminer2._matrix_list_2_network_graph import matrix_list_2_network_graph
# >>> from techminer2._get_network_graph_indicators import get_network_graph_indicators
# >>> from techminer2._network_community_detection import network_community_detection
# >>> from techminer2._network_map import network_map

# >>> matrix_list = vantagepoint__co_occ_matrix_list(
# ...    criterion='author_keywords',
# ...    topics_length=3,
# ...    directory=directory,
# ... )
# >>> graph = matrix_list_2_network_graph(matrix_list) 
# >>> graph = network_community_detection(graph, method='louvain')
# >>> network_map(graph).savefig(file_name)



# .. image:: images/co_occurrence_network_map.png
#     :width: 700px
#     :align: center

"""
from ._bubble_map import bubble_map


def network_map(
    network,
    color_scheme="clusters",
):

    manifold = network["manifold_data"]

    return bubble_map(
        node_x=manifold["Dim-0"],
        node_y=manifold["Dim-1"],
        node_clusters=manifold["cluster"],
        node_text=manifold["node"],
        node_sizes=manifold["degree"],
        x_axis_at=0,
        y_axis_at=0,
        color_scheme=color_scheme,
        xlabel="X-Axis",
        ylabel="Y-Axis",
        figsize=figsize,
        fontsize=7,
    )
