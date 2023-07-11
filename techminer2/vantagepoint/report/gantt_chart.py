# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _gantt_chart:

Gantt Chart
===============================================================================

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> tm2.gantt_chart(
...     root_dir=root_dir,
...     field="author_keywords",
...     top_n=10,
... ).write_html("sphinx/_static/gantt_chart.html")

.. raw:: html

    <iframe src="../../../../_static/gantt_chart.html" height="800px" width="100%" frameBorder="0"></iframe>


"""
import plotly.express as px

# from ..analyze.discover.terms_by_year_table import terms_by_year_table

COLOR = "#556f81"
TEXTLEN = 40


def gantt_chart(
    #
    # PARAMS:
    field,
    cumulative=False,
    #
    # CHART PARAMS:
    title=None,
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
    # pylint: disable=line-too-long
    """Computes a table with the number of occurrences of each term by year."""

    data_frame = terms_by_year_table(
        #
        # PARAMS:
        field=field,
        cumulative=cumulative,
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

    data_frame["RANKING"] = range(1, len(data_frame) + 1)
    data_frame = data_frame.melt(
        value_name="OCC",
        var_name="column",
        ignore_index=False,
        id_vars=["RANKING"],
    )

    data_frame = data_frame[data_frame.OCC > 0]
    data_frame = data_frame.sort_values(by=["RANKING"], ascending=True)
    data_frame = data_frame.drop(columns=["RANKING"])

    data_frame = data_frame.rename(columns={"column": "Year"})
    data_frame = data_frame.reset_index()

    fig = px.scatter(
        data_frame,
        x="Year",
        y=field,
        size="OCC",
        hover_data=data_frame.columns.to_list(),
        title=title,
        color=field,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis_title=None,
        yaxis_title=field.replace("_", " ").upper(),
    )
    fig.update_traces(
        marker={
            "line": {"color": "white", "width": 0.5},
            "opacity": 1.0,
        },
        marker_color=COLOR,
        mode="lines+markers",
        line={"width": 2, "color": COLOR},
    )
    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
        tickangle=270,
        dtick=1.0,
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
    )

    return fig
