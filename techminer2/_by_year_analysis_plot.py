import plotly.express as px

from .annual_indicators import annual_indicators


def by_year_analysis_plot(
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
        # hover_name="Year",
        hover_data=["Num Documents", "Global Citations", "Local Citations"],
    )
    fig.update_traces(marker=dict(size=12))
    fig.update_traces(line=dict(color="black"))
    fig.update_xaxes(tickangle=270)
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_xaxes(linecolor="gray", gridcolor="lightgray")
    fig.update_yaxes(linecolor="gray", gridcolor="lightgray")
    return fig
