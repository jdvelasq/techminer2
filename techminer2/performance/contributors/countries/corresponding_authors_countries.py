# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Corresponding Author's Countries
===============================================================================


>>> from techminer2.performance_analysis.fields.countries import corresponding_authors_countries
>>> result = corresponding_authors_countries(
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
>>> result.fig_.write_html("sphinx/_static/performance/countries/corresponding_authors_countries.html")

.. raw:: html

    <iframe src="../../../../_static/performance/countries/corresponding_authors_countries.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(result.df_.head().to_markdown())
| countries      |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:---------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United Kingdom |     7 |                199 |                35 |                    4 |                      3 |       0.43 |
| Australia      |     7 |                199 |                30 |                    4 |                      3 |       0.43 |
| United States  |     6 |                 59 |                19 |                    4 |                      2 |       0.33 |
| Ireland        |     5 |                 55 |                22 |                    4 |                      1 |       0.2  |
| China          |     5 |                 27 |                 5 |                    2 |                      3 |       0.6  |


>>> print(result.prompt_)
Your task is to generate an analysis about the collaboration between \\
countries according to the data in a scientific bibliography database. \\
Summarize the table below, delimited by triple backticks, where the column \\
'single publication' is the number of documents in which all the authors \\
belongs to the same country, and the  column 'multiple publication' is the \\
number of documents in which the authors are from different countries. The \\
column 'mcp ratio' is the ratio between the columns 'multiple publication' \\
and 'single publication'. The higher the ratio, the higher the \\
collaboration between countries. Use the information in the table to draw \\
conclusions about the level of collaboration between countries in the \\
dataset. In your analysis, be sure to describe in a clear and concise way, \\
any findings or any patterns you observe, and identify any outliers or \\
anomalies in the data. Limit your description to one paragraph with no more \\
than 250 words.
<BLANKLINE>
Table:
```
| countries            |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:---------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United Kingdom       |     7 |                199 |                35 |                    4 |                      3 |       0.43 |
| Australia            |     7 |                199 |                30 |                    4 |                      3 |       0.43 |
| United States        |     6 |                 59 |                19 |                    4 |                      2 |       0.33 |
| Ireland              |     5 |                 55 |                22 |                    4 |                      1 |       0.2  |
| China                |     5 |                 27 |                 5 |                    2 |                      3 |       0.6  |
| Italy                |     5 |                  5 |                 2 |                    4 |                      1 |       0.2  |
| Germany              |     4 |                 51 |                14 |                    2 |                      2 |       0.5  |
| Switzerland          |     4 |                 45 |                12 |                    1 |                      3 |       0.75 |
| Bahrain              |     4 |                 19 |                 3 |                    2 |                      2 |       0.5  |
| Hong Kong            |     3 |                185 |                23 |                    0 |                      3 |       1    |
| Luxembourg           |     2 |                 34 |                 7 |                    1 |                      1 |       0.5  |
| United Arab Emirates |     2 |                 13 |                 5 |                    1 |                      1 |       0.5  |
| Spain                |     2 |                  4 |                 0 |                    2 |                      0 |       0    |
| Indonesia            |     2 |                  0 |                 0 |                    2 |                      0 |       0    |
| Greece               |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| Japan                |     1 |                 13 |                 1 |                    0 |                      1 |       1    |
| South Africa         |     1 |                 11 |                 4 |                    1 |                      0 |       0    |
| Jordan               |     1 |                 11 |                 2 |                    0 |                      1 |       1    |
| Ukraine              |     1 |                  4 |                 0 |                    1 |                      0 |       0    |
| Malaysia             |     1 |                  3 |                 0 |                    1 |                      0 |       0    |
```
<BLANKLINE>

"""
from dataclasses import dataclass

import plotly.express as px

from ...._filtering_lib import generate_custom_items
from ...._sorting_lib import sort_indicators_by_metric
from ....format_prompt_for_dataframes import format_prompt_for_dataframes
from ....indicators.collaboration_indicators_by_field import collaboration_indicators_by_field


def corresponding_authors_countries(
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
    """Corresponding Author's Country

    :meta private:
    """

    indicators = __indicators(
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

    prompt = __create_prompt(indicators)

    fig = __plot(indicators)

    @dataclass
    class Results:
        df_ = indicators
        prompt_ = prompt
        fig_ = fig

    return Results()


def __indicators(
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    indicators = collaboration_indicators_by_field(
        "countries",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, "OCC")

    if custom_items is None:
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    indicators = indicators[indicators.index.isin(custom_items)]

    return indicators


def __create_prompt(data_frame):
    main_text = (
        "Your task is to generate an analysis about the collaboration between countries "
        "according to the data in a scientific bibliography database. Summarize the table "
        "below, delimited by triple backticks, where the column 'single publication' is the "
        "number of documents in which all the authors belongs to the same country, and the  "
        "column 'multiple publication' is the number of documents in which the authors are "
        "from different countries. The column 'mcp ratio' is the ratio between the columns "
        "'multiple publication' and 'single publication'. The higher the ratio, the higher "
        "the collaboration between countries. Use the information in the table to draw "
        "conclusions about the level of collaboration between countries in the dataset. In "
        "your analysis, be sure to describe in a clear and concise way, any findings or any "
        "patterns you observe, and identify any outliers or anomalies in the data. Limit your "
        "description to one paragraph with no more than 250 words."
    )
    return format_prompt_for_dataframes(main_text, data_frame.to_markdown())


def __plot(indicators):
    indicators = indicators.copy()
    indicators = indicators.reset_index()

    indicators = indicators.melt(
        id_vars="countries",
        value_vars=["single_publication", "multiple_publication"],
    )
    indicators = indicators.rename(columns={"variable": "publication", "value": "Num Documents"})
    indicators.publication = indicators.publication.map(lambda x: x.replace("_", " ").title())
    indicators.countries = indicators.countries.map(lambda x: x.title())

    fig = px.bar(
        indicators,
        x="Num Documents",
        y="countries",
        color="publication",
        title="Corresponding Author's Country",
        hover_data=["Num Documents"],
        orientation="h",
        color_discrete_map={
            "Single Publication": "#7793a5",
            "Multiple Publication": "#465c6b",
        },
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    return fig
