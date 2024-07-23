# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Collaboration WorldMap
===============================================================================


>>> from techminer2.report import collaboration_world_map
>>> chart = collaboration_world_map(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.write_html("sphinx/_static/report/collaboration_world_map.html")

.. raw:: html

    <iframe src="../_static/report/collaboration_world_map.html" 
    height="410px" width="100%" frameBorder="0"></iframe>



"""
import plotly.express as px

from ..co_occurrence_matrix.co_occurrence_matrix import co_occurrence_matrix


def collaboration_world_map(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    matrix = co_occurrence_matrix(
        columns="countries",
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    collaboration = matrix.list_cells_.head()

    collaboration = collaboration[collaboration.row != collaboration.column]
    collaboration["row"] = collaboration["row"].map(lambda x: " ".join(x.split()[:-1]))
    collaboration["column"] = collaboration["column"].map(lambda x: " ".join(x.split()[:-1]))

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
