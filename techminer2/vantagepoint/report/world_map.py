"""
World Map (GPT)
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__world_map.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.extract_topics(
...     criterion='countries',
...     directory=directory,
...     topics_length=None,
... )
>>> chart = vantagepoint.report.world_map(
...     obj, 
...     title="Country scientific production",
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint__world_map.html" height="450px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head()
countries
United Kingdom    7
Australia         7
United States     6
Ireland           5
China             5
Name: OCC, dtype: int64

>>> print(chart.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   OCC |
|:---------------------|------:|
| United Kingdom       |     7 |
| Australia            |     7 |
| United States        |     6 |
| Ireland              |     5 |
| China                |     5 |
| Italy                |     5 |
| Germany              |     4 |
| Switzerland          |     4 |
| Bahrain              |     4 |
| Hong Kong            |     3 |
| Luxembourg           |     2 |
| United Arab Emirates |     2 |
| Spain                |     2 |
| Indonesia            |     2 |
| Greece               |     1 |
| Japan                |     1 |
| Jordan               |     1 |
| South Africa         |     1 |
| Ukraine              |     1 |
| Malaysia             |     1 |
| Palestine            |     1 |
| India                |     1 |
| Taiwan               |     1 |
| France               |     1 |
| Poland               |     1 |
| Romania              |     1 |
| Singapore            |     1 |
| Belgium              |     1 |
| Netherlands          |     1 |
<BLANKLINE>
<BLANKLINE>

"""
from dataclasses import dataclass

import plotly.express as px

from ... import chatgpt


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def world_map(
    obj,
    title=None,
):
    colormap = "Blues"

    result = _Chart()
    result.plot_ = _create_plot(
        obj,
        title=title,
        colormap=colormap,
    )

    result.table_ = obj.table_[obj.metric_]
    result.prompt_ = chatgpt.generate_prompt(result.table_)

    return result


def _create_plot(
    obj,
    title,
    colormap,
):
    worldmap_data = _load_worldmap_data()

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
            col for col in dataframe.columns if col not in ["country", "iso_alpha"]
        ],
        range_color=(1, obj.table_[obj.metric_].max()),
        color_continuous_scale=colormap,
        color_discrete_map={0: "gray"},
        scope="world",
    )
    fig.update_layout(coloraxis_showscale=False)
    fig.update_layout(title=title)

    return fig


def _load_worldmap_data():
    worldmap_data = px.data.gapminder()[["country", "continent", "iso_alpha"]]
    worldmap_data = worldmap_data.drop_duplicates()

    # adds to worldmap_data the Russia, Greenland, and Antarctica
    worldmap_data = worldmap_data.append(
        {
            "country": "Russia",
            "continent": "Asia",
            "iso_alpha": "RUS",
        },
        ignore_index=True,
    )
    worldmap_data = worldmap_data.append(
        {
            "country": "Greenland",
            "continent": "North America",
            "iso_alpha": "GRL",
        },
        ignore_index=True,
    )
    worldmap_data = worldmap_data.append(
        {
            "country": "Antarctica",
            "continent": "Antarctica",
            "iso_alpha": "ATA",
        },
        ignore_index=True,
    )

    worldmap_data = worldmap_data.reset_index(drop=True)
    worldmap_data.index = worldmap_data.country
    return worldmap_data
