# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================

>>> from techminer2.pkgs.networks.coupling.documents import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
...     .having_citation_threshold(0)
...     #
...     # CLUSTERING:
...     .using_clustering_algorithm_or_dict("louvain")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
                                          0  ...                                             2
0  Gomber P., 2018, J MANAGE INF SYST 1:576  ...  Gracia D.B., 2019, IND MANAGE DATA SYS 1:225
1       Jagtiani J., 2018, J ECON BUS 1:156  ...                   Hu Z., 2019, SYMMETRY 1:176
2         Gomber P., 2017, J BUS ECON 1:489  ...     Gai K., 2018, J NETWORK COMPUT APPL 1:238
3     Haddad C., 2019, SMALL BUS ECON 1:258  ...    Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161
4             Lee I., 2018, BUS HORIZ 1:557  ...                                              
5    Leong C., 2017, INT J INF MANAGE 1:180  ...                                              
<BLANKLINE>
[6 rows x 3 columns]



"""
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from .._internals.from_documents.create_nx_graph import internal__create_nx_graph


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(params=self.params, nx_graph=nx_graph)
        return internal__extract_communities_to_frame(
            params=self.params, nx_graph=nx_graph
        )
