"""
Corresponding Author's Country
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__corresponding_authors_country.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.corresponding_authors_country(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__corresponding_authors_country.html"height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
                OCC  global_citations  ...  multiple_publication  mp_ratio
countries                              ...                                
United Kingdom    7               199  ...                     3      0.43
Australia         7               199  ...                     3      0.43
United States     6                59  ...                     2      0.33
Ireland           5                55  ...                     1      0.20
China             5                27  ...                     3      0.60
<BLANKLINE>
[5 rows x 6 columns]

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 most frequent countries in the dataset. 'single publication' is the number of documents in which all the authors are from the same country. 'multiple publication' is the number of documents in which the authors are from different countries. 'mcp ratio' is the ratio between 'multiple publication' and 'single publication'. The higher the ratio, the higher the collaboration between countries. Use the information in the table to draw conclusions about the level of collaboration between countries in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | countries            |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|---:|:---------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
|  0 | United Kingdom       |     7 |                199 |                34 |                    4 |                      3 |       0.43 |
|  1 | Australia            |     7 |                199 |                15 |                    4 |                      3 |       0.43 |
|  2 | United States        |     6 |                 59 |                11 |                    4 |                      2 |       0.33 |
|  3 | Ireland              |     5 |                 55 |                22 |                    4 |                      1 |       0.2  |
|  4 | China                |     5 |                 27 |                 5 |                    2 |                      3 |       0.6  |
|  5 | Italy                |     5 |                  5 |                 2 |                    4 |                      1 |       0.2  |
|  6 | Germany              |     4 |                 51 |                17 |                    2 |                      2 |       0.5  |
|  7 | Switzerland          |     4 |                 45 |                13 |                    1 |                      3 |       0.75 |
|  8 | Bahrain              |     4 |                 19 |                 5 |                    2 |                      2 |       0.5  |
|  9 | Hong Kong            |     3 |                185 |                 8 |                    0 |                      3 |       1    |
| 10 | Luxembourg           |     2 |                 34 |                 8 |                    1 |                      1 |       0.5  |
| 11 | United Arab Emirates |     2 |                 13 |                 7 |                    1 |                      1 |       0.5  |
| 12 | Spain                |     2 |                  4 |                 0 |                    2 |                      0 |       0    |
| 13 | Indonesia            |     2 |                  0 |                 0 |                    2 |                      0 |       0    |
| 14 | Greece               |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| 15 | Japan                |     1 |                 13 |                 1 |                    0 |                      1 |       1    |
| 16 | Jordan               |     1 |                 11 |                 4 |                    0 |                      1 |       1    |
| 17 | South Africa         |     1 |                 11 |                 4 |                    1 |                      0 |       0    |
| 18 | Ukraine              |     1 |                  4 |                 0 |                    1 |                      0 |       0    |
| 19 | Malaysia             |     1 |                  3 |                 0 |                    1 |                      0 |       0    |
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>


"""


import plotly.express as px

from ...classes import CorresponingAuthorCountry
from ...item_utils import generate_custom_items
from ...sort_utils import sort_indicators_by_metric
from ...techminer.indicators.collaboration_indicators_by_field import (
    collaboration_indicators_by_field,
)


def corresponding_authors_country(
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Corresponding Author's Country"""

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

    results = CorresponingAuthorCountry()
    results.table_ = indicators
    indicators = indicators.reset_index()
    results.plot_ = _make_plot(indicators)
    results.prompt_ = _create_prompt(indicators)
    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} most frequent countries in the \
dataset. 'single publication' is the number of documents in which all the \
authors are from the same country. 'multiple publication' is the number \
of documents in which the authors are from different countries. \
'mcp ratio' is the ratio between 'multiple publication' and 'single publication'. \
The higher the ratio, the higher the collaboration between countries. \
Use the information in the table to draw conclusions about the level of \
collaboration between countries in the dataset. In your analysis, be sure to \
describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""


# def _make_table(
#     directory,
#     database,
#     start_year,
#     end_year,
#     **filters,
# ):
#     indicators = indicators.sort_values(by="OCC", ascending=False)
#     indicators = indicators[["single_publication", "multiple_publication"]]
#     indicators = indicators.assign(
#         mcp_ratio=indicators["multiple_publication"]
#         / indicators["single_publication"]
#     )
#     indicators = indicators.replace(np.inf, "-")
#     return indicators


def _make_plot(indicators):
    indicators = indicators.melt(
        id_vars="countries",
        value_vars=["single_publication", "multiple_publication"],
    )
    indicators = indicators.rename(
        columns={"variable": "publication", "value": "Num Documents"}
    )
    indicators.publication = indicators.publication.map(
        lambda x: x.replace("_", " ").title()
    )
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
            "Single Publication": "#8da4b4",
            "Multiple Publication": "#556f81",
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
