# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Treemap
===============================================================================

>>> from techminer2.pkgs.networks.co_occurrence.user import Treemap
>>> plot = (
...     Treemap()
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # NETWORK:
...     .using_association_index("association")
...     #
...     # PLOT:
...     .using_title_text(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> plot.write_html("sphinx/_generated/pkgs/networks/co_occurrence/user/treemap.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/co_occurrence/user/treemap.html" 
    height="800px" width="100%" frameBorder="0"></iframe>


"""
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__assign_node_colors_based_on_group_attribute,
    internal__cluster_nx_graph,
    internal__plot_node_treemap,
)
from .._internals.create_nx_graph import internal__create_nx_graph


class Treemap(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__assign_node_colors_based_on_group_attribute(nx_graph)
        return internal__plot_node_treemap(self.params, nx_graph)
