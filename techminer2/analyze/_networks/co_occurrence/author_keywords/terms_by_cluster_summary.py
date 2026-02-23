"""
Terms by Cluster Summary
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
    >>> from techminer2.co_occurrence_network.author_keywords import TermsByClusterSummary
    >>> df = (
    ...     TermsByClusterSummary()
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
    >>> df  # doctest: +SKIP
       Cluster  ...                                              Terms
    0        0  ...  FINTECH 31:5168; BUSINESS_MODEL 03:0896; FINAN...
    1        1  ...  INNOVATION 07:0911; FINANCIAL_SERVICE 04:0667;...
    2        2  ...  MARKETPLACE_LENDING 03:0317; LENDINGCLUB 02:02...
    3        3  ...  ARTIFICIAL_INTELLIGENCE 02:0327; FINANCE 02:03...
    <BLANKLINE>
    [4 rows x 4 columns]


    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.co_occurrence_network.author_keywords import TermsByClusterSummary
    >>> df = (
    ...     TermsByClusterSummary()
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
    >>> df  # doctest: +SKIP
       Cluster  ...                                              Terms
    0        0  ...  FINTECH; BUSINESS_MODEL; FINANCIAL_INCLUSION; ...
    1        1  ...  INNOVATION; FINANCIAL_SERVICE; FINANCIAL_INSTI...
    2        2  ...  MARKETPLACE_LENDING; LENDINGCLUB; PEER_TO_PEER...
    3        3  ...           ARTIFICIAL_INTELLIGENCE; FINANCE; ROBOTS
    <BLANKLINE>
    [4 rows x 4 columns]



"""

from techminer2._internals import ParamsMixin
from techminer2.analyze._networks.co_occurrence.usr.terms_by_cluster_summary import (
    TermsByClusterSummary as UserTermsByClusterSummary,
)


class TermsByClusterSummary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsByClusterSummary()
            .update(**self.params.__dict__)
            .with_field("author_keywords")
            .run()
        )
