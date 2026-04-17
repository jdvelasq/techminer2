from tm2p._intern import ParamsMixin
from tm2p._intern.nx import (
    assign_degree_to_nodes,
    collect_node_degrees,
    create_node_degree_dataframe,
)
from tm2p.enum.cols import NAME
from tm2p.portfolio.intellectual_structure.coupling_network._intern.doc_borrar._create_nx_graph import (
    doc_create_nx_graph,
)


class xDocNodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        use_counters = self.params.use_counters
        self.params.use_counters = True
        nx_graph = doc_create_nx_graph(self.params)
        nx_graph = assign_degree_to_nodes(nx_graph)
        node_degrees = collect_node_degrees(nx_graph)
        df = create_node_degree_dataframe(node_degrees)

        if use_counters is False:
            self.params.use_counters = False
            df[NAME] = df[NAME].str.split(" ").str[:-1].str.join(" ")
        return df
