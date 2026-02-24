"""
Terms by Cluster Frame
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.co_citation.cited_authors import TermsByClusterDataFrame

    >>> df = (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_items_in_top(30)
    ...     .using_citation_threshold(0)
    ...     .having_items_in(None)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()

    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                       0              1                       2
    0  Zavolokina L. 1:3  Gomber P. 1:7         Jagtiani J. 1:2
    1       Gabor D. 1:2     Lee I. 1:2  Anagnostopoulos I. 1:1
    2      Ryu H.-S. 1:2   Leong C. 1:2
    3         Alt R. 1:1    Chen L. 1:1
    4         Gai K. 1:1  Gozman D. 1:1



"""

from techminer2._internals import ParamsMixin
from techminer2.synthesize.intellectual_structure.co_citation._internals.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as InternalTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_authors")
            .run()
        )
