"""
Terms to Cluster Mapping
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.authors import TermsToClustersMapping
    >>> mapping = (
    ...     TermsToClustersMapping()
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
    {'Buchak G. 1:0390': 3,
     'Dolata M. 2:0181': 2,
     'Gai K. 2:0323': 1,
     'Gomber P. 2:1065': 0,
     'Hornuf L. 2:0358': 6,
     'Jagtiani J. 3:0317': 4,
     'Kauffman R.J. 1:0576': 0,
     'Koch J.-A. 1:0489': 0,
     'Lee I. 1:0557': 5,
     'Lemieux C. 2:0253': 4,
     'Matvos G. 1:0390': 3,
     'Parker C. 1:0576': 0,
     'Piskorski T. 1:0390': 3,
     'Qiu M. 2:0323': 1,
     'Schwabe G. 2:0181': 2,
     'Shin Y.J. 1:0557': 5,
     'Siering M. 1:0489': 0,
     'Sun X. 2:0323': 1,
     'Weber B.W. 1:0576': 0,
     'Zavolokina L. 2:0181': 2}

    >>> mapping = (
    ...     TermsToClustersMapping()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
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
    >>> pprint(mapping)
    {'Buchak G.': 3,
     'Dolata M.': 2,
     'Gai K.': 1,
     'Gomber P.': 0,
     'Hornuf L.': 6,
     'Jagtiani J.': 4,
     'Kauffman R.J.': 0,
     'Koch J.-A.': 0,
     'Lee I.': 5,
     'Lemieux C.': 4,
     'Matvos G.': 3,
     'Parker C.': 0,
     'Piskorski T.': 3,
     'Qiu M.': 1,
     'Schwabe G.': 2,
     'Shin Y.J.': 5,
     'Siering M.': 0,
     'Sun X.': 1,
     'Weber B.W.': 0,
     'Zavolokina L.': 2}


"""

from techminer2._internals import ParamsMixin
from techminer2.synthesize.conceptual_structure.co_occurrence.usr.terms_to_clusters_mapping import (
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
            .with_field("authors")
            .run()
        )
