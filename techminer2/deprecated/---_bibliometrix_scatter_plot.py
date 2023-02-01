import plotly.express as px


def bibliometrix_scatter_plot(x, y, title, text, xlabel, ylabel):

    fig = px.scatter(
        x=x,
        y=y,
        title=title,
        text=text,
        labels={
            "x": xlabel,
            "y": ylabel,
        },
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
    fig.update_xaxes(showticklabels=False)
    return fig
