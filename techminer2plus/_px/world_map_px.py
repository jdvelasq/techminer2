"""Primitive to make a world map."""

import plotly.express as px


def world_map_px(
    dataframe,
    metric,
    title,
    colormap,
):
    """Primitive to make a world map."""

    worldmap_data = px.data.gapminder()[["country", "continent", "iso_alpha"]]
    worldmap_data = worldmap_data.drop_duplicates()
    worldmap_data = worldmap_data.reset_index(drop=True)
    worldmap_data.index = worldmap_data.country

    dataframe = dataframe.rename(columns={"Countries": "country"})
    dataframe = dataframe.set_index("country")
    dataframe = dataframe.sort_index()

    worldmap_data = worldmap_data.join(dataframe, how="left")
    worldmap_data = worldmap_data.fillna(0)

    fig = px.choropleth(
        worldmap_data,
        locations="iso_alpha",
        color=metric,
        hover_name="country",
        hover_data=[
            col for col in dataframe.columns if col not in ["country", "iso_alpha"]
        ],
        color_continuous_scale=colormap,
        scope="world",
    )
    fig.update_layout(title=title)

    return fig
