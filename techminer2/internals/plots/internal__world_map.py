# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods
"World Map Plot Mixin."

import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore


def internal__world_map(params, data_frame):

    #
    # Variables
    colormap = params.colormap
    hover_data = [
        col for col in data_frame.columns if col not in ["country", "iso_alpha"]
    ]
    metric = params.terms_order_by
    title_text = params.title_text

    #
    # Load worl map data
    world_map_data = px.data.gapminder()[["country", "continent", "iso_alpha"]]
    world_map_data = world_map_data.drop_duplicates()

    #
    # Adds to world_map_data the Russia, Greenland, and Antarctica
    world_map_data = pd.concat(
        [
            world_map_data,
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

    world_map_data = world_map_data.reset_index(drop=True)
    world_map_data.index = pd.Index(world_map_data.country.to_list())

    #
    # Plots the world map

    data_frame.index = data_frame.index.rename("country")
    data_frame = data_frame.sort_index()

    world_map_data = world_map_data.join(data_frame, how="left")
    world_map_data = world_map_data.fillna(0)

    fig = px.choropleth(
        world_map_data,
        locations="iso_alpha",
        color=metric,
        hover_name="country",
        hover_data=hover_data,
        range_color=(1, data_frame[metric].max()),
        color_continuous_scale=colormap,
        color_discrete_map={0: "gray"},
        scope="world",
    )

    # fig.update_layout(coloraxis_showscale=False)

    fig.update_layout(
        coloraxis_colorbar={
            "title": {"text": ""},
            "orientation": "h",
            "thickness": 10,
            "tickfont": {"size": 8},
            "len": 0.9,
            "x": 0.5,
            "y": -0.2,
        }
    )

    fig.update_layout(title=title_text)

    return fig
