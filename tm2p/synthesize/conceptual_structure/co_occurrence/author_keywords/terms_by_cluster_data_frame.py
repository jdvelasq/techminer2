"""
Terms by Cluster Frame
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
    >>> from techminer2.co_occurrence_network.author_keywords import TermsByClusterDataFrame
    >>> df = (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
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
                                    0  ...                                3
    0                 FINTECH 31:5168  ...  ARTIFICIAL_INTELLIGENCE 02:0327
    1          BUSINESS_MODEL 03:0896  ...                  FINANCE 02:0309
    2     FINANCIAL_INCLUSION 03:0590  ...                   ROBOTS 02:0289
    3  FINANCIAL_TECHNOLOGIES 03:0461  ...
    4              BLOCKCHAIN 03:0369  ...
    5            CROWDFUNDING 03:0335  ...
    6          CYBER_SECURITY 02:0342  ...
    7            CASE_STUDIES 02:0340  ...
    8                 REGTECH 02:0266  ...
    <BLANKLINE>
    [9 rows x 4 columns]


    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.co_occurrence_network.author_keywords import TermsByClusterDataFrame
    >>> df = (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
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
                            0  ...                        3
    0                 FINTECH  ...  ARTIFICIAL_INTELLIGENCE
    1          BUSINESS_MODEL  ...                  FINANCE
    2     FINANCIAL_INCLUSION  ...                   ROBOTS
    3  FINANCIAL_TECHNOLOGIES  ...
    4              BLOCKCHAIN  ...
    5            CROWDFUNDING  ...
    6          CYBER_SECURITY  ...
    7            CASE_STUDIES  ...
    8                 REGTECH  ...
    <BLANKLINE>
    [9 rows x 4 columns]



"""

from tm2p._internals import ParamsMixin
from tm2p.synthesize.conceptual_structure.co_occurrence.usr.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as UserTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .with_source_field("author_keywords")
            .run()
        )
