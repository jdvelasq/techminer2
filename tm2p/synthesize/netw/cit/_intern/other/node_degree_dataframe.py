from tm2p._intern import ParamsMixin
from tm2p._intern.nx import (
    assign_degree_to_nodes,
    collect_node_degrees,
    create_node_degree_dataframe,
)
from tm2p.enum.column import NAME
from tm2p.synthesize.netw.cit._intern.other.create_nx_graph import other_create_nx_graph


class OtherNodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = other_create_nx_graph(self.params)
        nx_graph = assign_degree_to_nodes(nx_graph)
        node_degrees = collect_node_degrees(nx_graph)
        df = create_node_degree_dataframe(node_degrees)
        if use_counters is False:
            self.params.counters = False
            df[NAME] = df[NAME].str.split(" ").str[:-1].str.join(" ")
        return df
