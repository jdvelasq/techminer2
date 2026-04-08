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
    >>> from tm2p.enum import AssociationIndex, Field, GraphClusteringAlgorithm, ItemOrderBy, RecordOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import ClusterToDocuments
    >>> mapping = (
    ...     ClusterToDocuments()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(len(mapping))
    4
    >>> print(mapping[0][0])
    UT 54
    AR Al-Sartawi A, 2024, J FINANC REP ACC, DOI 10.1108/JFRA-01-2024-0010
    TI The diffusion of financial technology-enabled innovation in GCC-listed banks
       and its relationship with profitability and market value
    AU Al-Sartawi A
    TC 125
    SO J FINANC REP ACC
    PY 2024
    AB purpose : this_study_aims_to_examine_the_relationship_between the
       DIFFUSION_OF_TECHNOLOGY-enabled INNOVATION_IN_FINANCIAL_SERVICES ( i . e .
       FINANCIAL_TECHNOLOGY [ FINTECH ] ) and THE_FINANCIAL_PERFORMANCE , i . e .
       PROFITABILITY and MARKET_VALUE of THE_BANKS listed in the
       GULF_COOPERATION_COUNCIL ( gcc ) COUNTRIES . design / methodology / approach
       : AN_EXTENSIVE_REVIEW of THE_LITERATURE was carried out , and
       A_DIFFUSION_INDEX of 73 items including was adopted to measure THE_LEVEL of
       FINTECH_USAGE or DIFFUSION for THE_BANKS that are listed on
       THE_GCC_STOCK_EXCHANGES . the_study used RETURN_ON_ASSETS ( ROA ) and
       TOBIN_Q ( tq ) as PROXIES to measure PROFITABILITY and MARKET_VALUE ,
       respectively . findings : the_findings of the empirical
       results_indicate_that_there_is_a POSITIVE_RELATIONSHIP between
       FINTECH_IMPLEMENTATION and MARKET_PERFORMANCE ( tq ) in THE_GCC_BANKS .
       the_results also showed that THE_HIGHEST_LEVEL of FINTECH_IMPLEMENTATION was
       79.7 % by UNITED_ARAB_EMIRATES_BANKS followed by BAHRAINI_BANKS at 76.7 %
       based on THE_INDEX developed for this_study . practical implications :
       this_study , hence , recommends that POLICYMAKERS and GOVERNMENTS implement
       SUPPORTIVE_POLICIES and INITIATIVES , allowing CONSUMERS to
       EMBRACE_TECHNOLOGY as part of THEIR_WAY of LIFE . this ENCOURAGES_BANKS and
       OTHER_ORGANIZATIONS to FORMULATE_STRATEGIES that integrate TECHNOLOGY into
       OPERATIONS . originality / value : this_paper_offers NEW_CONTRIBUTIONS to
       THE_GCC_LITERATURE regarding FINANCIAL_TECHNOLOGY and provides
       RECOMMENDATIONS to THE_GCC_FINANCIAL_INSTITUTIONS , FINANCIAL_MARKETS ,
       POLICYMAKERS and GOVERNMENTS . 2024 , emerald publishing limited .
    DE digital transformation; financial sector; fintech; fintech governance;
       fintech strategies; firm market value; gcc countries; profitability
    <BLANKLINE>


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.ingest.records import RecordViewer

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
