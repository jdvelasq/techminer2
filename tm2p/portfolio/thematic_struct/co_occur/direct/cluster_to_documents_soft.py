"""
ClusterToDocumentsSoft
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import RecordOrderBy  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import ClusterToDocumentsSoft
    >>> mapping = (
    ...     ClusterToDocumentsSoft()
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
    >>> print(mapping[0])  # doctest: +NORMALIZE_WHITESPACE
    291     Heydari S, 2025, SENSORS, V25, DOI 10.3390/s25...
    331     Lamaakal I, 2025, IEEE INTERNET THINGS J, V12,...
    340     Zeynali M, 2025, SCI REP, V15, DOI 10.1038/s41...
    402     Katib I, 2025, AIN SHAMS ENG J, V16, DOI 10.10...
    96      Zhou H, 2025, SCI REP, V15, DOI 10.1038/s41598...
    ...


"""

from tm2p._intern import Params, ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field

from .cluster_to_units import ClusterToUnits

REC_ID = Field.REC_ID.value


class ClusterToDocumentsSoft(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        c2u = (
            ClusterToUnits().update(**self.params.__dict__).using_counters(False).run()
        )

        mapping = {}
        analysis_unit = self.params.analysis_unit

        for key, values in c2u.items():

            params = {analysis_unit: values}

            records_match = self.params.records_match
            if records_match is not None:
                records_match = {**records_match, **params}
            else:
                records_match = params

            params = Params(**self.params.__dict__)
            params.records_match = records_match  # type: ignore

            records = load_filtered_main_csv_zip(params=params)

            mapping[key] = records[REC_ID]

        return mapping
