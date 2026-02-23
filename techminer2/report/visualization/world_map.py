"""
World Map
===============================================================================


Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.report.visualization import WorldMap
    >>> plot = (
    ...     WorldMap()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.COUNTRY)
    ...     #
    ...     # TERMS:
    ...     .having_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Countries' Scientific Production")
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(plot).__name__
    'Figure'
    >>> plot.write_html("tmp/px.database.metrics.performance.world_map.html")



"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.world_map import world_map
from techminer2.report.visualization.dataframe import DataFrame


class WorldMap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = DataFrame().update(**self.params.__dict__).run()
        fig = world_map(params=self.params, dataframe=df)

        return fig


#
