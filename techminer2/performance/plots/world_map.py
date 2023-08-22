# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
.. _tm2.performance.plots.world_map:

World Map
===============================================================================

>>> from techminer2.performance.plots import world_map
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/performance/plots/world_map.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/plots/world_map.html" 
    height="400px" width="100%" frameBorder="0"></iframe>

>>> chart.df_.head()
                rank_occ  OCC  ...  between_2022_2023  growth_percentage
countries                      ...                                      
United Kingdom         1    7  ...                  1              14.29
Australia              2    7  ...                  0               0.00
United States          3    6  ...                  2              33.33
Ireland                4    5  ...                  1              20.00
China                  5    5  ...                  4              80.00
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries            |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:---------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| United Kingdom       |          1 |     7 |             6 |                   1 |               14.29 |
| Australia            |          2 |     7 |             7 |                   0 |                0    |
| United States        |          3 |     6 |             4 |                   2 |               33.33 |
| Ireland              |          4 |     5 |             4 |                   1 |               20    |
| China                |          5 |     5 |             1 |                   4 |               80    |
| Italy                |          6 |     5 |             3 |                   2 |               40    |
| Germany              |          7 |     4 |             3 |                   1 |               25    |
| Switzerland          |          8 |     4 |             3 |                   1 |               25    |
| Bahrain              |          9 |     4 |             3 |                   1 |               25    |
| Hong Kong            |         10 |     3 |             3 |                   0 |                0    |
| Luxembourg           |         11 |     2 |             2 |                   0 |                0    |
| United Arab Emirates |         12 |     2 |             2 |                   0 |                0    |
| Spain                |         13 |     2 |             1 |                   1 |               50    |
| Indonesia            |         14 |     2 |             0 |                   2 |              100    |
| Greece               |         15 |     1 |             1 |                   0 |                0    |
| Japan                |         16 |     1 |             0 |                   1 |              100    |
| South Africa         |         17 |     1 |             1 |                   0 |                0    |
| Jordan               |         18 |     1 |             1 |                   0 |                0    |
| Ukraine              |         19 |     1 |             1 |                   0 |                0    |
| Malaysia             |         20 |     1 |             1 |                   0 |                0    |
```
<BLANKLINE>



"""
import pandas as pd
import plotly.express as px

from ..performance_metrics import performance_metrics


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
            hover_data=[col for col in dataframe.columns if col not in ["country", "iso_alpha"]],
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
