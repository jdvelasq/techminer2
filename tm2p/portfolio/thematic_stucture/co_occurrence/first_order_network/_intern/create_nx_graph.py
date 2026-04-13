from tm2p._intern import Params
from tm2p._intern.plots.nx import create_nx_graph_from_matrix

from ..matrix import Matrix


def create_nx_graph(params: Params):

    matrix = Matrix().update(**params.__dict__).using_counters(True).run()
    nx_graph = create_nx_graph_from_matrix(matrix)

    return nx_graph
