"""
Collaboration WorldMap
===============================================================================

>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/collaboration_worldmap.html"

>>> from techminer2 import collaboration_worldmap
>>> collaboration_worldmap(
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/collaboration_worldmap.html" height="410px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px
import plotly.graph_objects as go

from ...co_occ_matrix_list import co_occ_matrix_list


def collaboration_worldmap(
    directory="./",
    colormap="Blues",
):
    """Collaboration World Map"""

    collaboration = co_occ_matrix_list(
        column="countries",
        row=None,
        top_n=None,
        min_occ=None,
        max_occ=None,
        directory=directory,
        database="documents",
    )
    collaboration = collaboration[collaboration.row != collaboration.column]
    collaboration["row"] = collaboration["row"].map(lambda x: " ".join(x.split()[:-1]))
    collaboration["column"] = collaboration["column"].map(
        lambda x: " ".join(x.split()[:-1])
    )

    collaboration["pair"] = list(zip(collaboration.row, collaboration.column))
    collaboration["line"] = list(range(len(collaboration)))
    collaboration = collaboration[["pair", "line"]]
    collaboration = collaboration.explode("pair")

    fig = px.line_geo(
        collaboration,
        locations="pair",
        locationmode="country names",
        color="line",
        color_discrete_sequence=["darkslategray"],
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(l=1, r=1, t=1, b=1),
    )

    fig.update_geos(
        showcountries=True,
        landcolor="lightgray",
        countrycolor="Black",
        lataxis_showgrid=False,
        lonaxis_showgrid=False,
    )

    return fig
