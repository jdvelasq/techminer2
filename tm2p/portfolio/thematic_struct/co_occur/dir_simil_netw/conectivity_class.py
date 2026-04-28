"""
ConectivityClass
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.direct_similarity_network import ConectivityClass
    >>> df = (
    ...     ConectivityClass()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                       LINKS  TLS  TLS_TO_OCC_RATIO STRUCTURAL_ROLE
    sustainability 013:02308              16   47             3.615     Specialized
    economic growth 009:01654             10   31             3.444     Specialized
    sustainable development 015:02158     15   51             3.400     Specialized
    innovation 020:03916                  18   65             3.250     Specialized
    green finance 011:02844               12   34             3.091     Specialized


"""

import networkx as nx  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.nx import remove_selfloop_edges, set_node_size_properties

from .dir_matrix import DirectMatrix
from .matrix import Matrix as CoOccurrenceMatrix

LINKS = "LINKS"
TLS = "TLS"
TLS_TO_OCC_RATIO = "TLS_TO_OCC_RATIO"
STRUCTURAL_ROLE = "STRUCTURAL_ROLE"


class ConectivityClass(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        similarity_matrix = (
            DirectMatrix().update(**self.params.__dict__).using_counters(True).run()
        )
        co_occurrence_matrix = (
            CoOccurrenceMatrix()
            .update(**self.params.__dict__)
            .using_counters(True)
            .run()
        )

        nx_graph = nx.from_pandas_adjacency(similarity_matrix)
        nx_graph = remove_selfloop_edges(nx_graph)
        nx_graph = set_node_size_properties(self.params, nx_graph, co_occurrence_matrix)

        nodes = list(nx_graph.nodes())

        links = {node: nx_graph.nodes[node]["LINKS"] for node in nx_graph.nodes()}
        tls = {node: nx_graph.nodes[node]["TLS"] for node in nx_graph.nodes()}
        ratio = {
            node: (
                nx_graph.nodes[node]["TLS"] / nx_graph.nodes[node]["OCC"]
                if nx_graph.nodes[node]["OCC"] > 0
                else 0
            )
            for node in nx_graph.nodes()
        }
        values = list(ratio.values())
        p25, p50, p75 = np.percentile(values, [25, 50, 75])  # type: ignore
        structural_role = {}
        for node in nodes:
            if ratio[node] <= p25:
                structural_role[node] = "Generic"
            elif ratio[node] <= p50:
                structural_role[node] = "Common"
            elif ratio[node] <= p75:
                structural_role[node] = "Core"
            else:
                structural_role[node] = "Specialized"

        data_frame = pd.DataFrame(
            {
                LINKS: links,
                TLS: tls,
                TLS_TO_OCC_RATIO: ratio,
                STRUCTURAL_ROLE: structural_role,
            },
            index=nodes,
        )

        data_frame = data_frame.sort_values(
            by=[TLS_TO_OCC_RATIO, LINKS],
            ascending=[False, False],
        )

        return data_frame
