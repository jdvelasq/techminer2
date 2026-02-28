"""
Clusters to Terms Mapping
===============================================================================


Smoke tests:
    >>> from tm2p.packages.networks.co_authorship.authors import ClustersToTermsMapping
    >>> mapping = (
    ...     ClustersToTermsMapping()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
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
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {0: ['Gomber P. 2:1065',
         'Kauffman R.J. 1:0576',
         'Parker C. 1:0576',
         'Weber B.W. 1:0576',
         'Koch J.-A. 1:0489',
         'Siering M. 1:0489'],
     1: ['Gai K. 2:0323', 'Qiu M. 2:0323', 'Sun X. 2:0323'],
     2: ['Dolata M. 2:0181', 'Schwabe G. 2:0181', 'Zavolokina L. 2:0181'],
     3: ['Buchak G. 1:0390', 'Matvos G. 1:0390', 'Piskorski T. 1:0390'],
     4: ['Jagtiani J. 3:0317', 'Lemieux C. 2:0253'],
     5: ['Lee I. 1:0557', 'Shin Y.J. 1:0557'],
     6: ['Hornuf L. 2:0358']}



"""

from tm2p._intern import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.clusters_to_terms_mapping import (
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
            .with_source_field("authors")
            .run()
        )
