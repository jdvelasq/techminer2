# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Density Plot
===============================================================================


>>> from techminer2.pkgs.networks.co_occurrence.author_keywords import NodeDensityPlot
>>> plot = (
...     NodeDensityPlot()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # NETWORK:
...     .using_association_index("association")
...     #
...     #
...     .using_spring_layout_k(None)
...     .using_spring_layout_iterations(30)
...     .using_spring_layout_seed(0)
...     #
...     .using_textfont_size_range(10, 20)
...         bandwidth=0.1,
...     .using_colormap("Aggrnyl")
...         opacity=0.6,
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
>>> # plot.write_html("sphinx/_static/co_occurrence_network/node_density_plot.html")

.. raw:: html

    <iframe src="../_static/co_occurrence_network/node_density_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""

from .....internals.mixins import InputFunctionsMixin
from ..internals.node_density_plot import InternalNodeDensityPlot


class NodeDensityPlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            InternalNodeDensityPlot()
            .update_params(**self.params.__dict__)
            .with_field("author_keywords")
            .build()
        )
