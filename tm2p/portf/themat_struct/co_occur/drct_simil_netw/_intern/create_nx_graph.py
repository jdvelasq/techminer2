import networkx as nx  # type: ignore

from tm2p._intern import Params
from tm2p._intern.plots.nx import remove_selfloop_edges, set_node_size_properties

from ..direct_matrix import DirectMatrix
from ..mtx import Matrix as CoOccurrenceMatrix


def create_nx_graph(params: Params):

    similarity_matrix = (
        DirectMatrix().update(**params.__dict__).using_counters(True).run()
    )
    co_occurrence_matrix = (
        CoOccurrenceMatrix().update(**params.__dict__).using_counters(True).run()
    )
    nx_graph = nx.from_pandas_adjacency(similarity_matrix)
    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = set_node_size_properties(params, nx_graph, co_occurrence_matrix)

    return nx_graph
