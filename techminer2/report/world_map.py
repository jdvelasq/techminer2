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

>>> from techminer2.report import world_map
>>> chart = world_map(
...     #
...     # ITEMS PARAMS:
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Countries' Scientific Production",
...     colormap="Blues",
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/report/world_map.html")

.. raw:: html

    <iframe src="../../../_static/report/world_map.html" 
    height="400px" width="100%" frameBorder="0"></iframe>

>>> chart.df_.head()
               rank_occ  OCC  before_2018  between_2018_2019  growth_percentage
countries                                                                      
United States         1   16            1                 15              93.75
China                 2    8            3                  5              62.50
Germany               3    7            2                  5              71.43
South Korea           4    6            2                  4              66.67
Australia             5    5            2                  3              60.00


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
import pandas as pd
import plotly.express as px

from ..metrics.performance_metrics import performance_metrics


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
    """Creates a world map.

    :meta private:
    """

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
                col for col in dataframe.columns if col not in ["country", "iso_alpha"]
            ],
            range_color=(1, data_frame[metric].max()),
            color_continuous_scale=colormap,
            color_discrete_map={0: "gray"},
            scope="world",
        )
        # fig.update_layout(coloraxis_showscale=False)
        fig.update_layout(
            coloraxis_colorbar=dict(
                title=dict(text=""),
                orientation="h",
                thickness=10,
                tickfont=dict(size=8),
                len=0.9,
                x=0.5,
                y=-0.2,
            )
        )
        fig.update_layout(title=title)

        return fig

    def load_worldmap_data():
        worldmap_data = px.data.gapminder()[["country", "continent", "iso_alpha"]]
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
    items = performance_metrics(
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

    data_frame = items.df_.copy()
    items.fig_ = create_plot()

    return items
