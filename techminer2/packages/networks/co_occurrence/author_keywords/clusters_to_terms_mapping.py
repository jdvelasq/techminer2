# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Clusters to Terms Mapping
===============================================================================


Example:
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, InitializeThesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="example/", quiet=True).run()

    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.packages.networks.co_occurrence.author_keywords import ClustersToTermsMapping
    >>> mapping = (
    ...     ClustersToTermsMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(10)
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {0: ['FINTECH 31:5168',
         'INNOVATION 07:0911',
         'FINANCIAL_INCLUSION 03:0590',
         'BLOCKCHAIN 03:0369',
         'CROWDFUNDING 03:0335',
         'MARKETPLACE_LENDING 03:0317',
         'FINANCIAL_INSTITUTION 02:0484'],
     1: ['FINANCIAL_SERVICE 04:0667',
         'BUSINESS_MODEL 03:0896',
         'FINANCIAL_TECHNOLOGIES 03:0461']}


    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.packages.networks.co_occurrence.author_keywords import ClustersToTermsMapping
    >>> mapping = (
    ...     ClustersToTermsMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(10)
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {0: ['FINTECH',
         'INNOVATION',
         'FINANCIAL_INCLUSION',
         'BLOCKCHAIN',
         'CROWDFUNDING',
         'MARKETPLACE_LENDING',
         'FINANCIAL_INSTITUTION'],
     1: ['FINANCIAL_SERVICE', 'BUSINESS_MODEL', 'FINANCIAL_TECHNOLOGIES']}



"""
from ....._internals.mixins import ParamsMixin
from ..user.clusters_to_terms_mapping import (
    ClustersToTermsMapping as UserClustersToTermsMapping,
)


class ClustersToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserClustersToTermsMapping()
            .update(**self.params.__dict__)
            .with_field("author_keywords")
            .run()
        )
