from tm2p._intern import Params
from tm2p._intern.plots.nx import create_nx_graph_from_matrix

from ..latent_matrix import LatentMatrix


def create_nx_graph(params: Params):

    matrix = LatentMatrix().update(**params.__dict__).using_counters(True).run()
    nx_graph = create_nx_graph_from_matrix(matrix)

    return nx_graph
