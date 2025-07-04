# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
World Map
===============================================================================


Example:
    >>> from techminer2.database.metrics.performance import WorldMap
    >>> plot = (
    ...     WorldMap()
    ...     #
    ...     # FIELD:
    ...     .with_field("countries")
    ...     #
    ...     # TERMS:
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Countries' Scientific Production")
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.database.metrics.performance.world_map.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.performance.world_map.html"
    height="400px" width="100%" frameBorder="0"></iframe>


"""
from ...._internals.params_mixin import ParamsMixin
from ...._internals.plots.internal__world_map import internal__world_map
from .data_frame import DataFrame


class WorldMap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        if self.params.title_text is None:
            self.using_title_text("World Map")

        fig = internal__world_map(params=self.params, data_frame=data_frame)

        return fig
