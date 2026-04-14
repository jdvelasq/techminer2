from tm2p._intern import ParamsMixin
from tm2p._intern.nx import create_node_degree_plot

from ._node_degree_dataframe import DocNodeDegreeDataFrame


class DocNodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = DocNodeDegreeDataFrame().update(**self.params.__dict__).run()
        plot = create_node_degree_plot(self.params, df)

        return plot
