"""
Network metrics
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=2,
...    directory=directory,
... )
>>> obj = vantagepoint.analyze.network_metrics(co_occ_matrix)
>>> obj.table_.head()
                              Degree  Betweenness  Closeness  PageRank
regtech 28:329                    24     0.462865   0.961538  0.120570
fintech 12:249                    15     0.063865   0.714286  0.072220
compliance 07:030                 13     0.070556   0.675676  0.066519
regulatory technology 07:037      11     0.096056   0.641026  0.057893
regulation 05:164                 13     0.039944   0.675676  0.062773

>>> print(obj.prompt_)
Analyze the table below, which provides the degree centrality, betweeness \
centrality, closeness centrality, and pagerank of nodes in a networkx graph of \
a co-ocurrence matrix. Identify any notable patterns, trends, or outliers in \
the data, and discuss their implications in the network.
<BLANKLINE>
|                                    |   Degree |   Betweenness |   Closeness |   PageRank |
|:-----------------------------------|---------:|--------------:|------------:|-----------:|
| regtech 28:329                     |       24 |    0.462865   |    0.961538 |  0.12057   |
| fintech 12:249                     |       15 |    0.0638651  |    0.714286 |  0.0722198 |
| compliance 07:030                  |       13 |    0.0705556  |    0.675676 |  0.0665193 |
| regulatory technology 07:037       |       11 |    0.0960556  |    0.641026 |  0.0578929 |
| regulation 05:164                  |       13 |    0.0399444  |    0.675676 |  0.0627735 |
| artificial intelligence 04:023     |        9 |    0.0247778  |    0.609756 |  0.0473497 |
| financial regulation 04:035        |        8 |    0.0107778  |    0.581395 |  0.0412898 |
| financial services 04:168          |        7 |    0.00280952 |    0.568182 |  0.0357439 |
| anti-money laundering 03:021       |        5 |    0.00444444 |    0.555556 |  0.0295263 |
| blockchain 03:005                  |        7 |    0.0123333  |    0.568182 |  0.0379545 |
| innovation 03:012                  |        6 |    0.00347619 |    0.568182 |  0.0314127 |
| risk management 03:014             |        9 |    0.00716667 |    0.609756 |  0.0447381 |
| suptech 03:004                     |        7 |    0          |    0.581395 |  0.0354176 |
| accountability 02:014              |        4 |    0          |    0.531915 |  0.025025  |
| anti money laundering (aml) 02:013 |        1 |    0          |    0.396825 |  0.0102428 |
| charitytech 02:017                 |        4 |    0          |    0.531915 |  0.0248019 |
| data protection 02:027             |        3 |    0          |    0.520833 |  0.0185186 |
| data protection officer 02:014     |        4 |    0          |    0.531915 |  0.025025  |
| english law 02:017                 |        4 |    0          |    0.531915 |  0.0248019 |
| finance 02:001                     |        7 |    0.00169841 |    0.568182 |  0.0355464 |
| gdpr 02:014                        |        4 |    0          |    0.531915 |  0.025025  |
| reporting 02:001                   |       10 |    0.0134762  |    0.625    |  0.0486282 |
| sandbox 02:012                     |        5 |    0.00242063 |    0.543478 |  0.0274795 |
| semantic technologies 02:041       |        4 |    0          |    0.531915 |  0.0224613 |
| smart contracts 02:022             |        2 |    0          |    0.510204 |  0.0146482 |
| technology 02:010                  |        2 |    0          |    0.510204 |  0.0143888 |
<BLANKLINE>
<BLANKLINE>
# noqa: E501


"""

from ... import network_utils
from ...classes import NetworkStatistics
from .list_cells_in_matrix import list_cells_in_matrix


def network_metrics(
    matrix,
):
    """Compute network metrics a co-occurrence matrix."""

    def generate_chatgpt_prompt(table):
        """Generates a chatgpt prompt."""

        prompt = (
            "Analyze the table below, which provides the degree centrality, "
            "betweeness centrality, closeness centrality, and pagerank of "
            "nodes in a networkx graph of a co-ocurrence matrix. Identify "
            "any notable patterns, trends, or outliers in the data, and "
            "discuss their implications in the network."
            f"\n\n{table.to_markdown()}\n\n"
        )

        return prompt

    #
    #
    # Main:
    #
    #

    matrix_list = list_cells_in_matrix(matrix)
    graph = network_utils.create_graph(matrix_list)
    graph = network_utils.compute_node_degree(graph)
    table = network_utils.compute_newtork_statistics(graph)

    obj = NetworkStatistics()

    obj.table_ = table
    obj.prompt_ = generate_chatgpt_prompt(table)

    return obj
