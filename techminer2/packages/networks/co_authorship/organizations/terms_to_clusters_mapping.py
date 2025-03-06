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


>>> from techminer2.packages.networks.co_authorship.organizations import TermsToClustersMapping
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
{'Baylor Univ (USA) 2:0395': 2,
 'Columbia Grad Sch of Bus (USA) 1:0390': 1,
 'Fed Reserv Bank of Chicago (USA) 2:0253': 3,
 'Fed Reserv Bank of Philadelphia (USA) 3:0317': 3,
 'Goethe Univ Frankfurt (DEU) 2:1065': 0,
 'Hankyong Nac Univ (KOR) 1:0557': 4,
 'Max Planck Inst for Innovation and Competition (DEU) 2:0358': 6,
 'Pace Univ (USA) 2:0323': 7,
 'Pennsylvania State Univ (USA) 1:0576': 0,
 'Singapore Manag Univ (SMU) (SGP) 1:0576': 0,
 'Stanford GSB and the Hoover Institution, United States (USA) 1:0390': 1,
 'Sungkyunkwan Univ (KOR) 2:0307': 8,
 'Univ of Chicago (USA) 1:0390': 1,
 'Univ of Delaware (USA) 1:0576': 0,
 'Univ of Latvia (LVA) 2:0163': 9,
 'Univ of New South Wales (AUS) 2:0340': 2,
 'Univ of Sydney (AUS) 2:0300': 2,
 'Univ of Texas at Austin (USA) 1:0390': 1,
 'Univ of Zurich (CHE) 3:0434': 5,
 'Western Illinois Univ (USA) 1:0557': 4}

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
{'Baylor Univ (USA)': 2,
 'Columbia Grad Sch of Bus (USA)': 1,
 'Fed Reserv Bank of Chicago (USA)': 3,
 'Fed Reserv Bank of Philadelphia (USA)': 3,
 'Goethe Univ Frankfurt (DEU)': 0,
 'Hankyong Nac Univ (KOR)': 4,
 'Max Planck Inst for Innovation and Competition (DEU)': 6,
 'Pace Univ (USA)': 7,
 'Pennsylvania State Univ (USA)': 0,
 'Singapore Manag Univ (SMU) (SGP)': 0,
 'Stanford GSB and the Hoover Institution, United States (USA)': 1,
 'Sungkyunkwan Univ (KOR)': 8,
 'Univ of Chicago (USA)': 1,
 'Univ of Delaware (USA)': 0,
 'Univ of Latvia (LVA)': 9,
 'Univ of New South Wales (AUS)': 2,
 'Univ of Sydney (AUS)': 2,
 'Univ of Texas at Austin (USA)': 1,
 'Univ of Zurich (CHE)': 5,
 'Western Illinois Univ (USA)': 4}

"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.terms_to_clusters_mapping import (
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
            .with_field("organizations")
            .run()
        )
