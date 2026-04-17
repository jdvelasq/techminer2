from abc import ABC, abstractmethod

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.plots.nx import (
    build_network_density_plot,
    compute_clustered_spring_layout_positions,
    detect_communities,
)


class BaseKernelDensityPlot(
    ABC,
    ParamsMixin,
):
    """:meta private:"""

    @abstractmethod
    def create_nx_graph(self):
        pass

    @abstractmethod
    def assign_textfont_size(self, nx_graph):
        pass

    def run(self):

        use_counters = self.params.use_counters
        self.params.use_counters = True
        nx_graph = self.create_nx_graph()
        nx_graph = detect_communities(self.params, nx_graph)
        nx_graph = compute_clustered_spring_layout_positions(self.params, nx_graph)
        nx_graph = self.assign_textfont_size(nx_graph)  # type: ignore

        if use_counters is False:
            self.params.use_counters = False
            for node, data in nx_graph.nodes(data=True):  # type: ignore
                text = data["text"]
                nx_graph.nodes[node]["text"] = remove_counters(text)  # type: ignore

        return build_network_density_plot(self.params, nx_graph)
