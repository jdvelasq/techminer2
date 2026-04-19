import networkx as nx  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params


def add_node_colorscale(
    params: Params,
    fig: go.Figure,
    nx_graph: nx.Graph,
):
    """:meta private:"""

    colorscale = params.colorscale  # your custom scale

    years = [nx_graph.nodes[node]["year"] for node in nx_graph.nodes()]
    years = [round(year, 1) for year in years]
    years = sorted(years)

    vmin = min(years)
    vmax = max(years)

    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="markers",
            marker=dict(
                colorscale=colorscale,
                cmin=vmin,
                cmax=vmax,
                color=[vmin, vmax],  # needed to activate colorscale
                showscale=True,
                colorbar={
                    "title": {"text": "Year", "font": {"size": 10}},
                    "thickness": 10,
                    "len": 0.45,
                    "tickfont": {"size": 10},
                },
            ),
            hoverinfo="none",
            showlegend=False,
        )
    )

    return fig
