# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.others.network_metrics import _network_metrics
## >>> _network_metrics(
## ...     unit_of_analysis='authors', # authors, countries, organizations, sources
## ...     #
## ...     # COLUMN PARAMS:
## ...     top_n=20,
## ...     citations_threshold=0,
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # DATABASE:
## ...     .where_root_directory("examples/fintech/")
## ...     .where_database("main")
## ...     .where_record_years_range(None, None)
## ...     .where_record_citations_range(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .run()
## ... ).head()
                    Degree  Betweenness  Closeness  PageRank
Gomber P. 2:1065         3          0.0   0.333333  0.085695
Hornuf L. 2:0358         3          0.0   0.333333  0.073543
Jagtiani J. 3:0317       3          0.0   0.333333  0.120381
Lemieux C. 2:0253        3          0.0   0.333333  0.120381
Dolata M. 2:0181         2          0.0   0.222222  0.100000


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.nx import internal__compute_network_metrics
from techminer2.networks.coupling._internals.from_others.create_nx_graph import (
    internal__create_nx_graph,
)


class InternalNetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = internal__create_nx_graph(params=self.params)
        return internal__compute_network_metrics(params=self.params, nx_graph=nx_graph)
