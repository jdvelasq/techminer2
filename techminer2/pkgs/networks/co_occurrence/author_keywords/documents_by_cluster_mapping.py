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

>>> # where_records_ordered_by: date_newest, date_oldest, global_cited_by_highest, 
>>> #                           global_cited_by_lowest, local_cited_by_highest, 
>>> #                           local_cited_by_lowest, first_author_a_to_z, 
>>> #                           first_author_z_to_a, source_title_a_to_z, 
>>> #                           source_title_z_to_a
>>> from techminer2.pkgs.networks.co_occurrence.author_keywords DocumentsByClusterMapping
>>> documents_by_cluster = (
...     DocumentsByClusterMapping()
...     #
...     # FIELD:
...     .having_terms_in_top(10)
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     .where_records_ordered_by("date_newest")
...     #
...     .build()
... )
>>> print(len(documents_by_cluster))
4
>>> print(documents_by_cluster[0][0])
Record-No: 6
AR Haddad C., 2019, SMALL BUS ECON, V53, P81
TI The emergence of the global fintech market: economic and technological
   determinants
AU Haddad C.; Hornuf L.
TC 258
SO Small Business Economics
PY 2019
AB we investigate the economic and TECHNOLOGICAL_DETERMINANTS inducing
   ENTREPRENEURS to establish ventures with the purpose of reinventing
   FINANCIAL_TECHNOLOGY ( FINTECH ) . we find that countries witness more
   FINTECH_STARTUP_FORMATIONS when the economy is well_developed and
   VENTURE_CAPITAL is readily available . furthermore , the number of secure
   INTERNET_SERVERS , MOBILE_TELEPHONE_SUBSCRIPTIONS , and the
   AVAILABLE_LABOR_FORCE has a POSITIVE_IMPACT on the DEVELOPMENT of this
   NEW_MARKET_SEGMENT . finally , the more difficult IT is for companies to
   ACCESS_LOANS , the higher is the number of FINTECH_STARTUPS in a country .
   overall , the EVIDENCE_SUGGESTS that FINTECH_STARTUP_FORMATION_NEED not be
   left to chance , but ACTIVE_POLICIES can INFLUENCE the emergence of this
   NEW_SECTOR . 2018 , the author ( s ) .
DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
** ACCESS_LOANS; ACTIVE_POLICIES; AVAILABLE_LABOR_FORCE; EVIDENCE_SUGGESTS;
   FINANCIAL_TECHNOLOGY; FINTECH_STARTUPS; FINTECH_STARTUP_FORMATIONS;
   FINTECH_STARTUP_FORMATION_NEED; GLOBAL_FINTECH_MARKET; INTERNET_SERVERS;
   MOBILE_TELEPHONE_SUBSCRIPTIONS; NEW_MARKET_SEGMENT; NEW_SECTOR;
   POSITIVE_IMPACT; TECHNOLOGICAL_DETERMINANTS; VENTURE_CAPITAL
<BLANKLINE>



"""
from .....internals.mixins import InputFunctionsMixin
from ..user.documents_by_cluster_mapping import (
    DocumentsByClusterMapping as UserDocumentsByClusterMapping,
)


class DocumentsByClusterMapping(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserDocumentsByClusterMapping()
            .update_params(**self.params.__dict__)
            .with_field("author_keywords")
            .build()
        )
