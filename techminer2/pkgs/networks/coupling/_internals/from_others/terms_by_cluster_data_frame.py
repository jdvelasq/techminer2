# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.others.terms_by_cluster_frame import _terms_by_cluster_frame
## >>> _terms_by_cluster_frame(
## ...     unit_of_analysis='authors', # authors, countries, organizations, sources
## ...     #
## ...     # COLUMN PARAMS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
##                     0                     1                2
## 0    Gomber P. 2:1065      Dolata M. 2:0181    Gai K. 2:0323
## 1    Hornuf L. 2:0358     Schwabe G. 2:0181    Qiu M. 2:0323
## 2  Jagtiani J. 3:0317  Zavolokina L. 2:0181  Sun X./3 2:0323
## 3   Lemieux C. 2:0253                                       



"""
from ......_internals.mixins import ParamsMixin
from ......_internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from .create_nx_graph import internal__create_nx_graph


class InternalTermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)
