# flake8: noqa
# pylint: disable=line-too-long
"""
Bar Chart
===============================================================================

Displays a horizontal bar graph of the selected items in a ItemLlist object. 
Items in your list are the Y-axis, and the number of records are the X-axis.


* **COMPUTATIONAL API:**

>>> import techminer2plus.api as api
>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/bar_chart_1.html"
>>> api.bar_chart(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
...    title="Most Frequent Author Keywords"
... ).write_html(file_name)


.. raw:: html

    <iframe src="../_static/bar_chart_1.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from .list_items import list_items


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=invalid-name
def bar_chart(
    #
    # LISTITEMS PARAMS:
    field=None,
    metric="OCC",
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # CHART PARAMS:
    title=None,
    metric_label=None,
    field_label=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Bar chart."""

    data_frame, _ = list_items(
        #
        # LISTITEMS PARAMS:
        field=field,
        metric=metric,
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

    metric_label = (
        metric.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        field.replace("_", " ").upper() if field_label is None else field_label
    )

    fig = px.bar(
        data_frame,
        x=metric,
        y=None,
        hover_data=data_frame.columns.to_list(),
        orientation="h",
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker_color="rgb(171,171,171)",
        marker_line={"color": "darkslategray"},
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text=metric_label,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
        title_text=field_label,
    )

    return fig
