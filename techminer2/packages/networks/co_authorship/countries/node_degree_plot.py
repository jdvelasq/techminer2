# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Plot
===============================================================================


Example:
    >>> from techminer2.packages.networks.co_authorship.countries import NodeDegreePlot
    >>> plot = (
    ...     NodeDegreePlot()
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
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.networks.co_authorship.countries.node_degree_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.co_authorship.countries.node_degree_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>



"""
"""Node Degree Plot"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.co_occurrence.user.node_degree_plot import (
    NodeDegreePlot as UserNodeDegreePlot,
)


class NodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNodeDegreePlot()
            .update(**self.params.__dict__)
            .with_field("countries")
            .run()
        )
