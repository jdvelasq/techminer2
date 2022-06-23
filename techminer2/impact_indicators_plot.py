import plotly.express as px

from .impact_indicators import impact_indicators


def impact_indicators_plot(
    column,
    impact_measure="h_index",
    top_n=20,
    directory="./",
    title=None,
):
    if impact_measure not in [
        "h_index",
        "g_index",
        "m_index",
        "global_citations",
    ]:
        raise ValueError(
            "Impact measure must be one of: h_index, g_index, m_index, global_citations"
        )

    indicators = impact_indicators(directory=directory, column=column)
    indicators = indicators.sort_values(by=impact_measure, ascending=False)
    indicators = indicators.head(top_n)

    indicators = indicators.reset_index()
    column_names = {
        column: column.replace("_", " ").title() for column in indicators.columns
    }
    indicators = indicators.rename(columns=column_names)

    fig = px.scatter(
        indicators,
        x=impact_measure.replace("_", " ").title(),
        y=column.replace("_", " ").title(),
        hover_data=["H Index", "M Index", "G Index", "Global Citations"],
        title=title,
    )
    fig.update_traces(marker=dict(size=10, color="black"))
    fig.update_traces(textposition="middle right")
    fig.update_traces(line=dict(color="black"))
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        autorange="reversed",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )

    return fig
