# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms to Cluster Mapping
===============================================================================


Example:
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, CreateThesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="example/", quiet=True).run()


    >>> #
    >>> # CODE TESTED
    >>> #
    >>> # where_records_ordered_by: date_newest, date_oldest, global_cited_by_highest,
    >>> #                           global_cited_by_lowest, local_cited_by_highest,
    >>> #                           local_cited_by_lowest, first_author_a_to_z,
    >>> #                           first_author_z_to_a, source_title_a_to_z,
    >>> #                           source_title_z_to_a
    >>> from techminer2.packages.networks.co_occurrence.author_keywords import DocumentsByClusterMapping
    >>> documents_by_cluster = (
    ...     DocumentsByClusterMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("date_newest")
    ...     #
    ...     .run()
    ... )
    >>> print(len(documents_by_cluster))
    4
    >>> print(documents_by_cluster[0][0])
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
       FINANCIAL_TECHNOLOGY ( FINTECH ) . we find that COUNTRIES witness more
       FINTECH_STARTUP_FORMATIONS when THE_ECONOMY is
       WELL_DEVELOPED_AND_VENTURE_CAPITAL is readily available . furthermore ,
       THE_NUMBER of SECURE_INTERNET_SERVERS , MOBILE_TELEPHONE_SUBSCRIPTIONS , and
       THE_AVAILABLE_LABOR_FORCE has A_POSITIVE_IMPACT on THE_DEVELOPMENT of
       THIS_NEW_MARKET_SEGMENT . finally , the more difficult it is for COMPANIES
       to ACCESS_LOANS , the higher is THE_NUMBER of FINTECH_STARTUPS in A_COUNTRY
       . overall , THE_EVIDENCE suggests that FINTECH_STARTUP_FORMATION_NEED not be
       left to CHANCE , but ACTIVE_POLICIES can influence THE_EMERGENCE of
       THIS_NEW_SECTOR . 2018 , the author ( s ) .
    DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
    <BLANKLINE>





"""
from ....._internals.mixins import ParamsMixin
from ..user.documents_by_cluster_mapping import (
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
            .with_field("author_keywords")
            .run()
        )
