"""
Metrics
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.authors import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
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
    ... ).head(15)
                          Degree  Betweenness  Closeness  PageRank
    Gomber P. 2:1065           5     0.035088   0.263158  0.083753
    Kauffman R.J. 1:0576       3     0.000000   0.187970  0.050930
    Parker C. 1:0576           3     0.000000   0.187970  0.050930
    Weber B.W. 1:0576          3     0.000000   0.187970  0.050930
    Gai K. 2:0323              2     0.000000   0.105263  0.052219
    Qiu M. 2:0323              2     0.000000   0.105263  0.052219
    Sun X. 2:0323              2     0.000000   0.105263  0.052219
    Dolata M. 2:0181           2     0.000000   0.105263  0.052219
    Schwabe G. 2:0181          2     0.000000   0.105263  0.052219
    Zavolokina L. 2:0181       2     0.000000   0.105263  0.052219
    Koch J.-A. 1:0489          2     0.000000   0.164474  0.038386
    Siering M. 1:0489          2     0.000000   0.164474  0.038386
    Buchak G. 1:0390           2     0.000000   0.105263  0.052219
    Matvos G. 1:0390           2     0.000000   0.105263  0.052219
    Piskorski T. 1:0390        2     0.000000   0.105263  0.052219




>>> (
...     NetworkMetrics()
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
... ).head(15)
               Degree  Betweenness  Closeness  PageRank
Gomber P.           5     0.035088   0.263158  0.083753
Kauffman R.J.       3     0.000000   0.187970  0.050930
Parker C.           3     0.000000   0.187970  0.050930
Weber B.W.          3     0.000000   0.187970  0.050930
Gai K.              2     0.000000   0.105263  0.052219
Qiu M.              2     0.000000   0.105263  0.052219
Sun X.              2     0.000000   0.105263  0.052219
Dolata M.           2     0.000000   0.105263  0.052219
Schwabe G.          2     0.000000   0.105263  0.052219
Zavolokina L.       2     0.000000   0.105263  0.052219
Koch J.-A.          2     0.000000   0.164474  0.038386
Siering M.          2     0.000000   0.164474  0.038386
Buchak G.           2     0.000000   0.105263  0.052219
Matvos G.           2     0.000000   0.105263  0.052219
Piskorski T.        2     0.000000   0.105263  0.052219


"""

from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.network_metrics import (
    NetworkMetrics as UserNetworkMetrics,
)


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNetworkMetrics()
            .update(**self.params.__dict__)
            .with_field("authors")
            .run()
        )
