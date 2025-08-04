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
    >>> from techminer2.database.metrics.collaboration import WorldMap

    >>> # Creates, configure, and plots a world map.
    >>> plotter = (
    ...     WorldMap()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ... )
    >>> plot = plotter.run()
    >>> plot.write_html("docs_source/_generated/px.database.metrics.collaboration.world_map.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.collaboration.world_map.html"
    height="600px" width="100%" frameBorder="0"></iframe>



"""
import plotly.express as px  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....packages.co_occurrence_matrix import DataFrame as CoOccurrenceDataFrame


class WorldMap(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__build_collaboration_data_frame(self):

        # Builds a collaboration data frame with columns "rows", "columns", and "OCC"
        collaboration = (
            CoOccurrenceDataFrame()
            .update(**self.params.__dict__)
            .with_field("countries")
            .update(terms_order_by="OCC")
            .run()
        )

        collaboration = collaboration[collaboration["rows"] != collaboration["columns"]]
        collaboration["row"] = collaboration["rows"].map(
            lambda x: " ".join(x.split()[:-1])
        )
        collaboration["column"] = collaboration["columns"].map(
            lambda x: " ".join(x.split()[:-1])
        )

        collaboration["pair"] = list(zip(collaboration.row, collaboration.column))
        collaboration["line"] = list(range(len(collaboration)))
        collaboration = collaboration[["pair", "line"]]
        collaboration = collaboration.explode("pair")

        self.collaboration = collaboration

    # -------------------------------------------------------------------------
    def internal__plot_world_map(self):

        fig = px.line_geo(
            self.collaboration,
            locations="pair",
            locationmode="country names",
            color="line",
            color_discrete_sequence=["darkslategray"],
        )

        fig.update_layout(
            showlegend=False,
            margin=dict(l=1, r=1, t=1, b=1),
        )

        fig.update_geos(
            showcountries=True,
            landcolor="lightgray",
            countrycolor="Black",
            lataxis_showgrid=False,
            lonaxis_showgrid=False,
        )

        self.fig = fig

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__build_collaboration_data_frame()
        self.internal__plot_world_map()

        return self.fig
