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


>>> from techminer2.pkgs.networks.co_occurrence.author_keywords import ClustersToTermsMapping
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> from pprint import pprint
>>> pprint(mapping)
{0: ['FINTECH 31:5168',
     'FINANCIAL_INCLUSION 03:0590',
     'CROWDFUNDING 03:0335',
     'MARKETPLACE_LENDING 03:0317',
     'BUSINESS_MODELS 02:0759',
     'CYBER_SECURITY 02:0342',
     'CASE_STUDY 02:0340'],
 1: ['INNOVATION 07:0911',
     'FINANCIAL_SERVICES 04:0667',
     'FINANCIAL_TECHNOLOGY 03:0461']}


"""
from ....._internals.mixins import ParamsMixin
from ..user.clusters_to_terms_mapping import (
    ClustersToTermsMapping as UserClustersToTermsMapping,
)


class ClustersToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserClustersToTermsMapping()
            .update(**self.params.__dict__)
            .with_field("author_keywords")
            .build()
        )
