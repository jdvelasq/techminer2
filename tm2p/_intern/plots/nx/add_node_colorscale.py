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

    for trace in fig.data:
        if getattr(trace, "mode", None) and "markers" in trace.mode:  # type: ignore
            trace.marker.update(  #  type: ignore
                color=years,
                colorscale=colorscale,
                showscale=True,
                cmin=vmin,
                cmax=vmax,
                colorbar={
                    "title": {"text": "Year", "font": {"size": 10}},
                    "thickness": 10,
                    "len": 0.45,
                    "tickfont": {"size": 10},
                },
            )

    return fig
