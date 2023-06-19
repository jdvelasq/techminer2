# flake8: noqa
"""
World map
===============================================================================





>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/visualize/world_map.html"

>>> import techminer2plus
>>> itemslist = techminer2plus.analyze.list_items(
...     field='countries',
...     root_dir=root_dir,
... )
>>> chart = techminer2plus.visualize.world_map(
...     itemslist, 
...     title="Country scientific production",
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/visualize/world_map.html" height="400px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head()
countries
United Kingdom    7
Australia         7
United States     6
Ireland           5
China             5
Name: OCC, dtype: int64

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
| countries      |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:---------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| United Kingdom |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33.17 |         4 |         3 |      0.67 |
| Australia      |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                   0         |                     2017 |     7 |                       28.43 |         4 |         3 |      0.57 |
| United States  |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                   0.166667  |                     2016 |     8 |                        7.38 |         3 |         2 |      0.38 |
| Ireland        |     5 |             4 |                   1 |                 55 |                22 |                           11    |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                        9.17 |         3 |         2 |      0.5  |
| China          |     5 |             1 |                   4 |                 27 |                 5 |                            5.4  |                           1    |                   0.5 |                     2   |                   0.4       |                     2017 |     7 |                        3.86 |         3 |         2 |      0.43 |
| Italy          |     5 |             3 |                   2 |                  5 |                 2 |                            1    |                           0.4  |                   0   |                     1   |                   0.2       |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| Germany        |     4 |             3 |                   1 |                 51 |                17 |                           12.75 |                           4.25 |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        8.5  |         3 |         2 |      0.5  |
| Switzerland    |     4 |             3 |                   1 |                 45 |                13 |                           11.25 |                           3.25 |                   0.5 |                     0.5 |                   0.125     |                     2017 |     7 |                        6.43 |         2 |         2 |      0.29 |
| Bahrain        |     4 |             3 |                   1 |                 19 |                 5 |                            4.75 |                           1.25 |                  -1   |                     0.5 |                   0.125     |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Hong Kong      |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                   0         |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
import pandas as pd
import plotly.express as px

from ..check_params import check_listview
from ..classes import BasicChart


def world_map(
    obj,
    title=None,
    colormap="Blues",
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

        dataframe = obj.table_.copy()
        dataframe.index = dataframe.index.rename("country")
        dataframe = dataframe.sort_index()

        worldmap_data = worldmap_data.join(dataframe, how="left")
        worldmap_data = worldmap_data.fillna(0)

        fig = px.choropleth(
            worldmap_data,
            locations="iso_alpha",
            color=obj.metric_,
            hover_name="country",
            hover_data=[
                col
                for col in dataframe.columns
                if col not in ["country", "iso_alpha"]
            ],
            range_color=(1, obj.table_[obj.metric_].max()),
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

    check_listview(obj)

    chart = BasicChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart
