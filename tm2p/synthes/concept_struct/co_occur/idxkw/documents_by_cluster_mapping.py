"""
Terms to Cluster Mapping
===============================================================================


Smoke tests:
    >>> # where_records_ordered_by: date_newest, date_oldest, global_cited_by_highest,
    >>> #                           global_cited_by_lowest, local_cited_by_highest,
    >>> #                           local_cited_by_lowest, first_author_a_to_z,
    >>> #                           first_author_z_to_a, source_title_a_to_z,
    >>> #                           source_title_z_to_a
    >>> from tm2p.co_occurrence_network.index_keywords import DocumentsByClusterMapping
    >>> documents_by_cluster = (
    ...     DocumentsByClusterMapping()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("date_newest")
    ...     #
    ...     .run()
    ... )
    >>> print(len(documents_by_cluster)) # doctest: +SKIP
    3
    >>> print(documents_by_cluster[0][0]) # doctest: +SKIP
    UT 26
    AR Haddad C., 2019, SMALL BUS ECON, V53, P81
    TI The emergence of the global fintech market: economic and technological
       determinants
    AU Haddad C.; Hornuf L.
    TC 258
    SO Small Business Economics
    PY 2019
    AB we investigate THE_ECONOMIC_AND_TECHNOLOGICAL_DETERMINANTS inducing
       ENTREPRENEURS to establish VENTURES with THE_PURPOSE of reinventing
       FINANCIAL_TECHNOLOGY ( FINTECH ) . we find that COUNTRIES witness
       MORE_FINTECH_STARTUP_FORMATIONS when THE_ECONOMY is well developed and
       VENTURE_CAPITAL is readily available . furthermore , THE_NUMBER of
       SECURE_INTERNET_SERVERS , MOBILE_TELEPHONE_SUBSCRIPTIONS , and
       THE_AVAILABLE_LABOR_FORCE has A_POSITIVE_IMPACT on THE_DEVELOPMENT of
       THIS_NEW_MARKET_SEGMENT . finally , the more difficult it is for COMPANIES
       to ACCESS_LOANS , the higher is THE_NUMBER of FINTECH_STARTUPS in A_COUNTRY
       . overall , THE_EVIDENCE suggests that FINTECH_STARTUP_FORMATION_NEED not be
       left to chance , but ACTIVE_POLICIES can influence THE_EMERGENCE of
       THIS_NEW_SECTOR . 2018 , the author ( s ) .
    DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
    <BLANKLINE>





"""

from tm2p._internals import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.documents_by_cluster_mapping import (
    DocumentsByClusterMapping as UserDocumentsByClusterMapping,
)


class DocumentsByClusterMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserDocumentsByClusterMapping()
            .update(**self.params.__dict__)
            .with_source_field("keywords")
            .run()
        )
