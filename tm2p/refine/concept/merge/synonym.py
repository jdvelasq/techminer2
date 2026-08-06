"""
Synonym
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.merge import Synonym
    >>> (
    ...     Synonym()
    ...     #
    ...     # ANALYSIS UNIT:    
    ...     .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
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
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # DATABASE:    
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, ThFile
from tm2p.refine._intern.merge import BaseSynonym


class Synonym(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> int:
        """:meta private:"""

        return (
            BaseSynonym()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_analysis_unit(AnalysisUnit.CONCEPT)
            .run()
        )


# if __name__ == "__main__":

#     Synonym().where_root_directory(".").run()
