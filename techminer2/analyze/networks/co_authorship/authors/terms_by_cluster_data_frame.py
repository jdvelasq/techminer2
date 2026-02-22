"""
Terms by Cluster Frame
===============================================================================

Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.authors import TermsByClusterDataFrame

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
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )

    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                        0              1  ...                 5                 6
    0      Gomber P. 2:1065  Gai K. 2:0323  ...     Lee I. 1:0557  Hornuf L. 2:0358
    1  Kauffman R.J. 1:0576  Qiu M. 2:0323  ...  Shin Y.J. 1:0557
    2      Parker C. 1:0576  Sun X. 2:0323  ...
    3     Weber B.W. 1:0576                 ...
    4     Koch J.-A. 1:0489                 ...
    5     Siering M. 1:0489                 ...
    <BLANKLINE>
    [6 rows x 7 columns]


"""

from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.terms_by_cluster_data_frame import (
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
            .with_field("authors")
            .run()
        )
