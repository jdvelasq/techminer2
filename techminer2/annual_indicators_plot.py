import plotly.express as px

from .annual_indicators import annual_indicators


def annual_indicators_plot(
    column,
    title,
    directory,
):
    indicators = annual_indicators(directory)
    indicators = indicators.reset_index()
    column_names = {
        column: column.replace("_", " ").title() for column in indicators.columns
    }
    indicators = indicators.rename(columns=column_names)
    indicators = indicators.rename(columns={"Pub Year": "Year"})
    fig = px.line(
        indicators,
        x="Year",
        y=column_names[column],
        title=title,
        markers=True,
        hover_data=["Num Documents", "Global Citations", "Local Citations"],
    )
    fig.update_traces(
        marker=dict(size=10, line=dict(color="darkslategray", width=2)),
        marker_color="rgb(171,171,171)",
        line=dict(color="darkslategray"),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
    )
    return fig
