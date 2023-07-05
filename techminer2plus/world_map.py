# flake8: noqa
# pylint: disable=line-too-long
"""
.. _world_map:

World map
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .list_items(
...         field='countries',
...     )
...     .world_map(
...         title="Country scientific production",
...     )
...     .write_html("sphinx/_static/world_map_0.html")
... )

.. raw:: html

    <iframe src="../_static/world_map_0.html" height="400px" width="100%" frameBorder="0"></iframe>


* Functional interface

>>> itemslist = tm2p.list_items(
...     field='countries',
...     root_dir=root_dir,
... )
>>> tm2p.world_map(
...     itemslist, 
...     title="Country scientific production",
... ).write_html("sphinx/_static/world_map_1.html")

.. raw:: html

    <iframe src="../_static/world_map_1.html" height="400px" width="100%" frameBorder="0"></iframe>

"""
import pandas as pd
import plotly.express as px


def world_map(
    list_items=None,
    colormap="Blues",
    title=None,
):
    """Creates a world map.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        colormap (str, optional): Color map. Defaults to "Blues".

    Returns:
        BasicChart: A basic chart object.


    """

    def create_plot():
        """Creates a plotly figure."""

        worldmap_data = load_worldmap_data()

        dataframe = list_items.df_.copy()
        dataframe.index = dataframe.index.rename("country")
        dataframe = dataframe.sort_index()

        worldmap_data = worldmap_data.join(dataframe, how="left")
        worldmap_data = worldmap_data.fillna(0)

        fig = px.choropleth(
            worldmap_data,
            locations="iso_alpha",
            color=list_items.metric,
            hover_name="country",
            hover_data=[
                col
                for col in dataframe.columns
                if col not in ["country", "iso_alpha"]
            ],
            range_color=(1, list_items.df_[list_items.metric].max()),
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
    return create_plot()
