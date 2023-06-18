# flake8: noqa
"""
Collaboration WorldMap
===============================================================================

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__collaboration_worldmap.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.social_structure.collaboration_worldmap(
...     root_dir=root_dir,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__collaboration_worldmap.html" height="410px" width="100%" frameBorder="0"></iframe>


# pylint: disable=line-too-long
"""
import plotly.express as px

# from ...vantagepoint.analyze import co_occurrence_matrix, list_cells_in_matrix


def collaboration_worldmap(
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Collaboration World Map"""

    matrix = co_occurrence_matrix(
        columns="countries",
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    collaboration = list_cells_in_matrix(matrix).cells_list_

    collaboration = collaboration[collaboration.row != collaboration.column]
    collaboration["row"] = collaboration["row"].map(
        lambda x: " ".join(x.split()[:-1])
    )
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
