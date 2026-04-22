"""
ClusterToDocuments
===============================================================================


Smoke tests:
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  #       linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  #  always
    ...     compute_distances=True,  #  always True
    ... )
    >>> from tm2p.enum import AssociationIndex, Field, GraphClusteringAlgorithm, UnitOrderBy, RecordOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.direct_similarity_network import ClusterToDocuments
    >>> mapping = (
    ...     ClusterToDocuments()
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
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(len(mapping))
    4
    >>> print(mapping[0][0])


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.ingest.rec import RecordViewer

from .cluster_to_items import ClusterToItems


class ClusterToDocuments(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        c2t_mapping = (
            ClusterToItems().update(**self.params.__dict__).using_counters(False).run()
        )

        mapping = {}
        field = self.params.source_field

        for key, values in c2t_mapping.items():

            params = {field: values}

            records_match = self.params.records_match
            if records_match is not None:
                records_match = {**records_match, **params}
            else:
                records_match = params

            mapping[key] = (
                RecordViewer()
                .update(**self.params.__dict__)
                .with_source_field(Field.ABSTR_UPPER)
                .where_records_match(records_match)
                .run()
            )

        return mapping
