"""
Create concept grid
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=3,
...    directory=directory,
... )
>>> concept_grid = vantagepoint.analyze.create_concept_grid(co_occ_matrix)
>>> concept_grid
                          CL_00  ...                        CL_02
0  regulatory technology 07:037  ...               fintech 12:249
1             compliance 07:030  ...    financial services 04:168
2             regulation 05:164  ...  financial regulation 04:035
3        risk management 03:014  ...            innovation 03:012
4                suptech 03:004  ...                             
<BLANKLINE>
[5 rows x 3 columns]


"""


from ... import network_utils
from .list_cells_in_matrix import list_cells_in_matrix


def create_concept_grid(
    matrix,
    method="louvain",
):
    """Create a concept grid (communities) of a networkx graph."""

    matrix_list = list_cells_in_matrix(matrix)
    graph = network_utils.create_graph(matrix_list)
    graph = network_utils.apply_community_detection_method(graph, method)
    grid_concepts = network_utils.get_communities(graph)

    return grid_concepts