from abc import ABC, abstractmethod

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.plots.nx import compute_node_metrics


class BaseNodeMetrics(
    ABC,
    ParamsMixin,
):
    """:meta private:"""

    @abstractmethod
    def create_nx_graph(self):
        pass

    def run(self):

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = self.create_nx_graph()
        df = compute_node_metrics(nx_graph=nx_graph)

        if use_counters is False:
            self.params.counters = False
            names = df.index.tolist()
            names = [remove_counters(name) for name in names]
            df.index = names

        df.columns.name = "METRIC"
        df.index.name = "NODE"  # type: ignore

        return df
