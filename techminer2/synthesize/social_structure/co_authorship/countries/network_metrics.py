"""
Metrics
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.countries import NetworkMetrics
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
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                            Degree  Betweenness  Closeness  PageRank
    United States 16:3189        8     0.253411   0.494152  0.187008
    Australia 05:0783            6     0.147173   0.423559  0.126959
    Germany 07:1814              5     0.115010   0.386728  0.098902
    China 08:1085                4     0.012671   0.386728  0.115357
    Denmark 02:0330              4     0.050682   0.355789  0.074453
    Sweden 01:0160               3     0.000000   0.355789  0.053942
    South Korea 06:1192          2     0.000000   0.306715  0.056150
    Netherlands 03:0300          2     0.000000   0.296491  0.042702
    Singapore 01:0576            2     0.000000   0.342105  0.041331
    Kazakhstan 01:0121           2     0.000000   0.306715  0.040427
    United Kingdom 03:0636       1     0.000000   0.269537  0.025484
    France 01:0258               1     0.000000   0.254135  0.026881
    Hong Kong 01:0178            1     0.000000   0.269537  0.025484
    Belgium 01:0101              1     0.000000   0.296491  0.024518
    Switzerland 04:0660          0     0.000000   0.000000  0.010067



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
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                    Degree  Betweenness  Closeness  PageRank
    United States        8     0.253411   0.494152  0.187008
    Australia            6     0.147173   0.423559  0.126959
    Germany              5     0.115010   0.386728  0.098902
    China                4     0.012671   0.386728  0.115357
    Denmark              4     0.050682   0.355789  0.074453
    Sweden               3     0.000000   0.355789  0.053942
    South Korea          2     0.000000   0.306715  0.056150
    Netherlands          2     0.000000   0.296491  0.042702
    Singapore            2     0.000000   0.342105  0.041331
    Kazakhstan           2     0.000000   0.306715  0.040427
    United Kingdom       1     0.000000   0.269537  0.025484
    France               1     0.000000   0.254135  0.026881
    Hong Kong            1     0.000000   0.269537  0.025484
    Belgium              1     0.000000   0.296491  0.024518
    Switzerland          0     0.000000   0.000000  0.010067





"""

from techminer2._internals import ParamsMixin
from techminer2.synthesize.conceptual_structure.co_occurrence.usr.network_metrics import (
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
            .with_source_field("countries")
            .run()
        )
