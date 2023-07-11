# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _world_map:

World map
===============================================================================


>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p
>>> tm2p.world_map(
...    title="Countries' Scientific Production",
...    top_n=20,
...    root_dir=root_dir,
... ).write_html("sphinx/_static/world_map.html")

.. raw:: html

    <iframe src="../../_static/world_map.html" height="400px" width="100%" frameBorder="0"></iframe>

"""
import pandas as pd
import plotly.express as px

from .list_items_table import list_items_table


def world_map(
    #
    # ITEMS PARAMS:
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    colormap="Blues",
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a world map."""

    def create_plot():
        """Creates a plotly figure."""

        worldmap_data = load_worldmap_data()

        dataframe = data_frame.copy()
        dataframe.index = dataframe.index.rename("country")
        dataframe = dataframe.sort_index()

        worldmap_data = worldmap_data.join(dataframe, how="left")
        worldmap_data = worldmap_data.fillna(0)

        fig = px.choropleth(
            worldmap_data,
            locations="iso_alpha",
            color=metric,
            hover_name="country",
            hover_data=[
                col
                for col in dataframe.columns
                if col not in ["country", "iso_alpha"]
            ],
            range_color=(1, data_frame[metric].max()),
            color_continuous_scale=colormap,
            color_discrete_map={0: "gray"},
            scope="world",
        )
        fig.update_layout(coloraxis_showscale=False)
        fig.update_layout(title=title)

        return fig

    def load_worldmap_data():
        worldmap_data = px.data.gapminder()[
            ["country", "continent", "iso_alpha"]
        ]
        worldmap_data = worldmap_data.drop_duplicates()

        # adds to worldmap_data the Russia, Greenland, and Antarctica
        worldmap_data = pd.concat(
            [
                worldmap_data,
                pd.DataFrame(
                    {
                        "country": ["Russia", "Greenland", "Antarctica"],
                        "continent": ["Asia", "North America", "Antarctica"],
                        "iso_alpha": ["RUS", "GRL", "ATA"],
                    }
                ),
            ],
            ignore_index=True,
        )

        worldmap_data = worldmap_data.reset_index(drop=True)
        worldmap_data.index = pd.Index(worldmap_data.country.to_list())
        return worldmap_data

    #
    # Main code
    #
    data_frame = list_items_table(
        #
        # ITEMS PARAMS:
        field="countries",
        metric=metric,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return create_plot()
