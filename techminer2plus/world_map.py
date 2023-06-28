# flake8: noqa
"""
.. _world_map:

World map
===============================================================================





>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/world_map.html"

>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...     field='countries',
...     top_n=20,
...     root_dir=root_dir,
... )
>>> chart = techminer2plus.world_map(
...     itemslist, 
...     title="Country scientific production",
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/world_map.html" height="400px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head()
countries
United Kingdom    7
Australia         7
United States     6
Ireland           5
China             5
Name: OCC, dtype: int64



# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


@dataclass
class WorldMap:
    """World Map.

    :meta private:
    """

    plot_: go.Figure
    table_: pd.DataFrame


def world_map(
    data=None,
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

        dataframe = data.df_.copy()
        dataframe.index = dataframe.index.rename("country")
        dataframe = dataframe.sort_index()

        worldmap_data = worldmap_data.join(dataframe, how="left")
        worldmap_data = worldmap_data.fillna(0)

        fig = px.choropleth(
            worldmap_data,
            locations="iso_alpha",
            color=data.metric_,
            hover_name="country",
            hover_data=[
                col
                for col in dataframe.columns
                if col not in ["country", "iso_alpha"]
            ],
            range_color=(1, data.df_[data.metric_].max()),
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

    return WorldMap(
        plot_=create_plot(),
        table_=data.df_[data.metric_],
    )
