"""
ClusterActivity
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import RecordOrderBy  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import ClusterActivity
    >>> df = (
    ...     ClusterActivity()
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
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
            0   1   2   3   4  5
    YEAR
    2020    7   2   3   1   0  0
    2021   38   7   8   1   1  0
    2022  106  15  32  15   2  1
    2023  199  26  30   7   3  2
    2024  324  42  43  11   6  4
    2025  368  64  38  18  30  9


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.portfolio.perform_metr.annu import Metrics

from .cluster_to_documents_hard import ClusterToDocumentsHard

REC_ID = Field.REC_ID.value
OCC = "OCC"
YEAR = "YEAR"


class ClusterActivity(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        df = None

        c2d = ClusterToDocumentsHard().update(**self.params.__dict__).run()

        for cluster, rec_ids in c2d.items():

            annual_metrics = (
                Metrics()
                .update(**self.params.__dict__)
                .where_records_match({Field.REC_ID: rec_ids})
                .run()
            )

            if df is None:
                df = annual_metrics[[OCC]].copy()
                df.columns = [cluster]
            else:
                df_cluster = annual_metrics[[OCC]].copy()
                df_cluster.columns = [cluster]
                df = df.join(df_cluster, how="outer")

        # check if there are missing years in the index and add them with 0 values
        df = df.reset_index()  #  type: ignore
        df[YEAR] = df[YEAR].astype(int)
        df = df.set_index(YEAR)
        df = df.reindex(range(df.index.min(), df.index.max() + 1), fill_value=0)

        df = df.fillna(0).astype(int)  #  type: ignore
        df = df[sorted(df.columns)]

        return df
