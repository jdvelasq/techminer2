import plotly.express as px

from .tm2.indicators.document_indicators import document_indicators


def most_cited_documents(
    metric,
    top_n=20,
    directory="./",
    title=None,
    database="documents",
    use_filter=True,
):
    """Most cited documents."""

    indicators = document_indicators(
        directory=directory, database=database, use_filter=use_filter
    )
    indicators = indicators.sort_values(by=metric, ascending=False)
    indicators = indicators.head(top_n)
    indicators = indicators.rename(
        columns={col: col.replace("_", " ").title() for col in indicators.columns}
    )
    indicators = indicators.reset_index()

    indicators = indicators.rename(columns={"article": "Document"})

    fig = px.scatter(
        indicators,
        x=metric.replace("_", " ").title(),
        y="Document",
        hover_data=["Global Citations", "Local Citations"],
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
