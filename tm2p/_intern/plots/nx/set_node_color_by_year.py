import networkx as nx  # type: ignore
from plotly.colors import sample_colorscale  # type: ignore

from tm2p._intern import Params


def set_node_color_by_year(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    years = [nx_graph.nodes[node]["year"] for node in nx_graph.nodes()]
    years = [round(year, 1) for year in years]
    years = sorted(years)

    year_min = min(years)
    year_max = max(years)
    year_norm = [(year - year_min) / (year_max - year_min) for year in years]

    rgb_colors = sample_colorscale(params.colorscale, year_norm)
    hex_colors = [rgb_to_hex(c) for c in rgb_colors]

    mapping = dict(zip(years, hex_colors))

    for node in nx_graph.nodes():
        year = nx_graph.nodes[node]["year"]
        nx_graph.nodes[node]["node_color"] = mapping[year]
    return nx_graph


def rgb_to_hex(rgb_str):
    r, g, b = map(int, rgb_str.strip("rgb()").split(","))
    return f"#{r:02x}{g:02x}{b:02x}"
