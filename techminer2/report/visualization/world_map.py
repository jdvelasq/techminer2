"""
World Map
===============================================================================


Smoke tests:
    >>> from techminer2.analyze.metrics.performance import WorldMap
    >>> plot = (
    ...     WorldMap()
    ...     #
    ...     # FIELD:
    ...     .with_field("countries")
    ...     #
    ...     # TERMS:
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Countries' Scientific Production")
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.database.metrics.performance.world_map.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.performance.world_map.html"
    height="400px" width="100%" frameBorder="0"></iframe>


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.world_map import world_map
from techminer2.report.visualization.dataframe import DataFrame


class WorldMap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        if self.params.title_text is None:
            self.using_title_text("World Map")

        fig = world_map(params=self.params, dataframe=data_frame)

        return fig


#
