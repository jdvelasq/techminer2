"""Primitive to make a circle plot."""

import plotly.express as px


def pie_px(
    dataframe,
    values,
    names,
    title,
    hole,
):
    """Makes a circle plot."""

    fig = px.pie(
        dataframe,
        values=values,
        names=names,
        hole=hole,
        title=title,
    )
    fig.update_traces(textinfo="value")
    fig.update_layout(legend=dict(y=0.5))
    return fig

    # fig = px.scatter(
    #     dataframe,
    #     x=x_label,
    #     y=y_label,
    #     hover_data=dataframe.columns.to_list(),
    #     title=title,
    # )
    # fig.update_layout(
    #     paper_bgcolor="white",
    #     plot_bgcolor="white",
    # )
    # fig.update_traces(
    #     marker=dict(size=10),
    #     marker_color="rgb(171,171,171)",
    #     marker_line={"color": "darkslategray"},
    # )
    # fig.update_xaxes(
    #     linecolor="gray",
    #     linewidth=2,
    #     gridcolor="lightgray",
    #     griddash="dot",
    # )
    # fig.update_yaxes(
    #     linecolor="gray",
    #     linewidth=2,
    #     autorange="reversed",
    #     gridcolor="lightgray",
    #     griddash="dot",
    # )
    # return fig
