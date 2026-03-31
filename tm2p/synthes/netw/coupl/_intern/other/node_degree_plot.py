from tm2p._intern import ParamsMixin
from tm2p._intern.nx import create_node_degree_plot

from .node_degree_dataframe import OtherNodeDegreeDataFrame


class OtherNodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = OtherNodeDegreeDataFrame().update(**self.params.__dict__).run()
        plot = create_node_degree_plot(self.params, df)

        return plot
