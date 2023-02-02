"""
Corresponding Author's Country
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__corresponding_authors_country.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.authors.countries.corresponding_authors_country(
...     topics_length=20,
...     directory=directory,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__corresponding_authors_country.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> from techminer2 import bibliometrix
>>> bibliometrix.authors.countries.corresponding_authors_country(
...     directory=directory, 
...     topics_length=20,
... ).table_.head()
                single_publication  multiple_publication  mcp_ratio
countries                                                          
United Kingdom                   4                     3       0.75
Australia                        4                     3       0.75
United States                    4                     2       0.50
Ireland                          4                     1       0.25
China                            2                     3       1.50

"""
from dataclasses import dataclass

import plotly.express as px

from ....techminer.indicators.collaboration_indicators_by_topic import (
    collaboration_indicators_by_topic,
)


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def corresponding_authors_country(
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Corresponding Author's Country"""

    results = _Results()
    table = _make_table(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if topic_min_occ is not None:
        table = table[table.OCC >= topic_min_occ]
    if topic_min_citations is not None:
        table = table[table.global_citations >= topic_min_citations]
    table = table.head(topics_length)

    results.table_ = table
    table = table.reset_index()
    results.plot_ = _make_plot(table)
    return results


def _make_table(
    directory,
    database,
    start_year,
    end_year,
    **filters,
):

    indicators = collaboration_indicators_by_topic(
        "countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = indicators.sort_values(by="OCC", ascending=False)
    indicators = indicators[["single_publication", "multiple_publication"]]
    indicators = indicators.assign(
        mcp_ratio=indicators["multiple_publication"] / indicators["single_publication"]
    )
    return indicators


def _make_plot(indicators):

    indicators = indicators.melt(
        id_vars="countries", value_vars=["single_publication", "multiple_publication"]
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
