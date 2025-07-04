# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Metrics
===============================================================================


Example:
    >>> from techminer2.packages.networks.coupling.authors import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                          Degree  Betweenness  Closeness  PageRank
    Gomber P. 2:1065           3          0.0        0.6  0.166667
    Kauffman R.J. 1:0576       3          0.0        0.6  0.166667
    Parker C. 1:0576           3          0.0        0.6  0.166667
    Weber B.W. 1:0576          3          0.0        0.6  0.166667
    Jagtiani J. 3:0317         1          0.0        0.2  0.166667
    Lemieux C. 2:0253          1          0.0        0.2  0.166667




    >>> from techminer2.packages.networks.coupling.authors import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                   Degree  Betweenness  Closeness  PageRank
    Gomber P.           3          0.0        0.6  0.166667
    Kauffman R.J.       3          0.0        0.6  0.166667
    Parker C.           3          0.0        0.6  0.166667
    Weber B.W.          3          0.0        0.6  0.166667
    Jagtiani J.         1          0.0        0.2  0.166667
    Lemieux C.          1          0.0        0.2  0.166667





"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.network_metrics import InternalNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNetworkMetrics()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .unit_of_analysis("authors")
            .run()
        )
