from abc import ABC, abstractmethod

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.nx import build_node_degree_plot


class BaseStrengthPlot(
    ABC,
    ParamsMixin,
):

    @abstractmethod
    def get_node_metrics(self):
        pass

    def run(self):

        use_counters = self.params.counters

        metrics = self.get_node_metrics().update(**self.params.__dict__).using_counters(True).run()  # type: ignore
        metrics = metrics.reset_index().rename(columns={"index": "NODE"})
        if use_counters is False:
            self.params.counters = False
            metrics["NODE"] = metrics["NODE"].str.split(" ").str[:-1].str.join(" ")
        plot = build_node_degree_plot(self.params, metrics)

        return plot
