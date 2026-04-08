import plotly.express as px  # type: ignore

STRENGTH = "STRENGTH"
NAME = "NAME"
NODE = "NODE"
RANK = "RANK"


def create_node_degree_plot(params, df):

    df = df.copy()
    df[RANK] = range(1, len(df) + 1)

    fig = px.line(
        df,
        x=RANK,
        y=STRENGTH,
        hover_data=NODE,
        markers=True,
    )
    fig.update_traces(
        marker={
            "size": params.marker_size,
            "line": {"color": params.line_color, "width": 0},
        },
        marker_color=params.line_color,
        line={
            "color": params.line_color,
            "width": params.line_width,
        },
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
        title="Strength",
    )

    nticks = min(30, len(df))

    fig.update_xaxes(
        tickmode="linear",
        tick0=1,
        dtick=1,
        nticks=nticks,
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title="Node",
    )

    for _, row in df.iterrows():
        fig.add_annotation(
            x=row[RANK],
            y=row[STRENGTH],
            text=row[NODE],
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": params.textfont_size},
            yshift=params.yshift,
        )

    return fig
