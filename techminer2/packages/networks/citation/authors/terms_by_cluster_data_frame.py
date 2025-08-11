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
    >>> from techminer2.packages.networks.citation.authors import TermsByClusterDataFrame

    >>> df = (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()

    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                          0                    1                   2
    0      Gomber P. 2:1065     Hornuf L. 2:0358  Jagtiani J. 3:0317
    1  Kauffman R.J. 1:0576     Haddad C. 1:0258   Lemieux C. 2:0253
    2      Parker C. 1:0576  Puschmann T. 1:0253
    3     Weber B.W. 1:0576
    4     Koch J.-A. 1:0489

    >>> df = (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()

    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                   0             1            2
    0      Gomber P.     Hornuf L.  Jagtiani J.
    1  Kauffman R.J.     Haddad C.   Lemieux C.
    2      Parker C.  Puschmann T.
    3     Weber B.W.
    4     Koch J.-A.



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.citation._internals.from_others.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as OtherTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            OtherTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .unit_of_analysis("authors")
            .run()
        )
