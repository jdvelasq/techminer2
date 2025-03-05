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


>>> from techminer2.pkgs.networks.co_occurrence.descriptors import ClustersToTermsMapping
>>> mapping = (
...     ClustersToTermsMapping()
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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... )
>>> from pprint import pprint
>>> pprint(mapping)
{0: ['THIS_PAPER 14:2240',
     'FINANCIAL_SERVICE 12:2100',
     'SERVICES 09:1527',
     'BANKS 09:1133',
     'THE_DEVELOPMENT 08:1173',
     'REGULATORS 08:0974',
     'DATA 07:1086',
     'BANKING 07:0851',
     'THE_AUTHOR 07:0828',
     'INVESTMENT 06:1294',
     'THE_FINANCIAL_SERVICES_INDUSTRY 06:1237',
     'THE_PURPOSE 06:1046'],
 1: ['FINTECH 46:7183',
     'FINANCE 21:3481',
     'FINANCIAL_TECHNOLOGIES 18:2455',
     'INNOVATION 16:2845',
     'TECHNOLOGIES 15:1810',
     'THIS_STUDY 14:1737',
     'THE_FINANCIAL_INDUSTRY 09:2006',
     'THIS_ARTICLE 06:1360']}



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
            .with_field("descriptors")
            .run()
        )
