"""
ClusterToDocumentsHard
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import RecordOrderBy  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import ClusterToDocumentsHard
    >>> mapping = (
    ...     ClusterToDocumentsHard()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
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
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping[0][:5])  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    ['Aanjankumar S, 2025, IEEE ACCESS, V13, P97428, DOI '
     '10.1109/ACCESS.2025.3573076',
     'Abadade Y, 2023, IEEE ACCESS, V11, P96892, DOI 10.1109/ACCESS.2023.3294111',
     'Abadade Y, 2024, FUTUR INTERNET, V16, DOI 10.3390/fi16110391',
     'Abbas NA, 2023, J TEKNOL, V85, P175, DOI 10.11113/jurnalteknologi.v85.18744',
     'Abdulghafoor YS, 2025, AL-NAHRAIN J ENG SCI, V28, P97, DOI '
     '10.29194/NJES.2801097']

"""

import sys

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.portfolio.thematic_struct.tfidf import Matrix as TfIdf

from .cluster_to_units import ClusterToUnits

REC_ID = Field.REC_ID.value


class ClusterToDocumentsHard(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        tf_matrix = (
            TfIdf()
            .update(**self.params.__dict__)
            #
            .using_counters(True)
            #
            .using_tfidf_binary_frequencies(True)
            .using_tfidf_norm(None)
            .using_tfidf_smooth_idf(False)
            .using_tfidf_sublinear_tf(False)
            .using_tfidf_use_idf(False)
            #
            .run()
        )

        c2u = ClusterToUnits().update(**self.params.__dict__).using_counters(True).run()

        clusters = sorted(c2u.keys())
        cluster_scores = pd.DataFrame(index=tf_matrix.index)

        for cluster in clusters:
            cluster_terms = c2u[cluster]
            #
            #
            for unit in cluster_terms:
                if unit not in tf_matrix.columns.to_list():
                    tf_matrix[unit] = 0

                    sys.stderr.write(f"Warning: Unit '{unit}' from cluster {cluster}\n")
                    for c in tf_matrix.columns:
                        unit_f = unit[:6]
                        if c.startswith(unit_f):
                            sys.stderr.write(f"   '{c}'\n")
            #
            #
            cluster_scores[cluster] = tf_matrix[cluster_terms].sum(axis=1)

        dominant_cluster = cluster_scores.idxmax(axis=1)

        mapping = {}

        for idx, cluster in dominant_cluster.items():  # type: ignore
            if cluster not in mapping:
                mapping[cluster] = []
            mapping[cluster].append(idx)

        return mapping
