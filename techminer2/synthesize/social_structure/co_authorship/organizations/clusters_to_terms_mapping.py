"""
Clusters to Terms Mapping
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.organizations import ClustersToTermsMapping
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
    {0: ['Goethe Univ Frankfurt (DEU) 2:1065',
         'Pennsylvania State Univ (USA) 1:0576',
         'Singapore Manag Univ (SMU) (SGP) 1:0576',
         'Univ of Delaware (USA) 1:0576'],
     1: ['Columbia Grad Sch of Bus (USA) 1:0390',
         'Univ of Chicago (USA) 1:0390',
         'Univ of Texas at Austin (USA) 1:0390',
         '[UKN] Stanford GSB and the Hoover Inst, United States (USA) 1:0390'],
     2: ['Baylor Univ (USA) 2:0395',
         'Univ of New South Wales (AUS) 2:0340',
         'Univ of Sydney (AUS) 2:0300'],
     3: ['Fed Reserv Bank of Philadelphia (USA) 3:0317',
         'Fed Reserv Bank of Chicago (USA) 2:0253'],
     4: ['Hankyong Nac Univ (KOR) 1:0557', 'Western Illinois Univ (USA) 1:0557'],
     5: ['Univ of Zurich (CHE) 3:0434'],
     6: ['Max Planck Inst for Innovation and Competition (DEU) 2:0358'],
     7: ['Pace Univ (USA) 2:0323'],
     8: ['Sungkyunkwan Univ (KOR) 2:0307'],
     9: ['Univ of Latvia (LVA) 2:0163']}




"""

from techminer2._internals import ParamsMixin
from techminer2.synthesize.conceptual_structure.co_occurrence.usr.clusters_to_terms_mapping import (
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
            .with_field("organizations")
            .run()
        )
