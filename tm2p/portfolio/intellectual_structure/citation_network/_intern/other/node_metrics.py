from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.plots.nx import compute_node_metrics

from .create_nx_graph import other_create_nx_graph


class OtherNodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = other_create_nx_graph(self.params)
        df = compute_node_metrics(nx_graph=nx_graph)

        if use_counters is False:
            self.params.counters = False
            names = df.index.tolist()
            names = [remove_counters(name) for name in names]
            df.index = names

        return df
