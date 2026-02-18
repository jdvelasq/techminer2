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


Smoke tests:
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> from techminer2.refine.thesaurus_old.descriptors import ApplyThesaurus, InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()


    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.co_occurrence_network.author_keywords import TermsToClustersMapping
    >>> mapping = (
    ...     TermsToClustersMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +SKIP
    {'ARTIFICIAL_INTELLIGENCE 02:0327': 3,
     'BANKING 02:0291': 1,
     'BLOCKCHAIN 03:0369': 0,
     'BUSINESS_MODEL 03:0896': 0,
     'CASE_STUDIES 02:0340': 0,
     'CROWDFUNDING 03:0335': 0,
     'CYBER_SECURITY 02:0342': 0,
     'FINANCE 02:0309': 3,
     'FINANCIAL_INCLUSION 03:0590': 0,
     'FINANCIAL_INSTITUTION 02:0484': 1,
     'FINANCIAL_SERVICE 04:0667': 1,
     'FINANCIAL_TECHNOLOGIES 03:0461': 0,
     'FINTECH 31:5168': 0,
     'INNOVATION 07:0911': 1,
     'LENDINGCLUB 02:0253': 2,
     'MARKETPLACE_LENDING 03:0317': 2,
     'PEER_TO_PEER_LENDING 02:0253': 2,
     'REGTECH 02:0266': 0,
     'ROBOTS 02:0289': 3,
     'TECHNOLOGIES 02:0310': 1}





    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.co_occurrence_network.author_keywords import TermsToClustersMapping
    >>> mapping = (
    ...     TermsToClustersMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +SKIP
    {'ARTIFICIAL_INTELLIGENCE': 3,
     'BANKING': 1,
     'BLOCKCHAIN': 0,
     'BUSINESS_MODEL': 0,
     'CASE_STUDIES': 0,
     'CROWDFUNDING': 0,
     'CYBER_SECURITY': 0,
     'FINANCE': 3,
     'FINANCIAL_INCLUSION': 0,
     'FINANCIAL_INSTITUTION': 1,
     'FINANCIAL_SERVICE': 1,
     'FINANCIAL_TECHNOLOGIES': 0,
     'FINTECH': 0,
     'INNOVATION': 1,
     'LENDINGCLUB': 2,
     'MARKETPLACE_LENDING': 2,
     'PEER_TO_PEER_LENDING': 2,
     'REGTECH': 0,
     'ROBOTS': 3,
     'TECHNOLOGIES': 1}



"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.terms_to_clusters_mapping import (
    TermsToClustersMapping as UserTermsToClusterMapping,
)


class TermsToClustersMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsToClusterMapping()
            .update(**self.params.__dict__)
            .with_field("author_keywords")
            .run()
        )
