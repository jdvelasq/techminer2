# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================

Example:
    >>> from techminer2.packages.networks.co_authorship.authors import TermsByClusterDataFrame

    >>> df = (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
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
from techminer2._internals.mixins import ParamsMixin
from techminer2.co_occurrence.usr.terms_by_cluster_data_frame import (
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
