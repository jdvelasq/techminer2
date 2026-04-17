from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx import (
    assign_textfont_sizes_based_on_occurrences,
    cluster_nx_graph,
    compute_spring_layout_positions,
    create_network_density_plot,
)
from tm2p.portfolio.intellectual_structure.coupling_network._intern.others_borrar._create_nx_graph import (
    other_create_nx_graph,
)


class xOtherKernelDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        use_counters = self.params.use_counters
        self.params.use_counters = True

        nx_graph = other_create_nx_graph(params=self.params)
        nx_graph = cluster_nx_graph(self.params, nx_graph)
        nx_graph = compute_spring_layout_positions(self.params, nx_graph)
        nx_graph = assign_textfont_sizes_based_on_occurrences(self.params, nx_graph)

        if use_counters is False:
            self.params.use_counters = False
            for node, data in nx_graph.nodes(data=True):
                text = data["text"]
                nx_graph.nodes[node]["text"] = remove_counters(text)

        return create_network_density_plot(self.params, nx_graph)
