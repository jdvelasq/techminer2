"""
Corresponding author's country (TODO)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/corresponding_authors_country.html"

>>> corresponding_authors_country(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/corresponding_authors_country.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> corresponding_authors_country(directory=directory, plot=False).head()
                single_publication  multiple_publication  mcp_ratio
countries                                                          
china                           20                    23   1.150000
united kingdom                  19                    22   1.157895
indonesia                       21                     1   0.047619
united states                    7                    15   2.142857
australia                        4                    14   3.500000


"""
import plotly.express as px

from .collaboration_indicators import collaboration_indicators


def corresponding_authors_country(top_n=20, directory="./", plot=True):

    indicators = collaboration_indicators("countries", directory=directory)
    indicators = indicators.sort_values(by="num_documents", ascending=False)
    indicators = indicators[["single_publication", "multiple_publication"]]

    if plot is False:
        indicators = indicators.assign(
            mcp_ratio=indicators["multiple_publication"]
            / indicators["single_publication"]
        )
        return indicators

    indicators = indicators.head(top_n)
    indicators = indicators.reset_index()

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
        title="Corresponding author's country",
        hover_data=["Num Documents"],
        orientation="h",
        color_discrete_map={
            "Single Publication": "#8da4b4",
            "Multiple Publication": "#556f81",
        },
    )
    # "slategray"
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        # gridcolor="gray",
        # griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    return fig
