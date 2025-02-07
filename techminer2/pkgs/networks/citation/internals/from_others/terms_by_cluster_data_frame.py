# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Builds a terms by cluster frame from other fields.



"""
from ......internals.mixins import InputFunctionsMixin
from ......internals.nx.cluster_nx_graph import internal__cluster_nx_graph
from ......internals.nx.extract_communities_to_frame import (
    internal__extract_communities_to_frame,
)
from .create_nx_graph import internal__create_nx_graph


class TermsByClusterDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)
