import networkx as nx  # type: ignore
import numpy as np  # type: ignore
import plotly.graph_objects as go  # type: ignore
from sklearn.neighbors import KernelDensity  # type: ignore

from tm2p._intern import Params


def build_heatmap_trace(
    params: Params,
    nx_graph: nx.Graph,
) -> go.Heatmap:

    node_x = [data["x"] for _, data in nx_graph.nodes(data=True)]
    node_y = [data["y"] for _, data in nx_graph.nodes(data=True)]
    node_raw_weights = np.asarray(
        [data["raw_node_size"] for _, data in nx_graph.nodes(data=True)],
        dtype=float,
    )

    xy = np.column_stack([node_x, node_y]).astype(float)

    x_range = xy[:, 0].max() - xy[:, 0].min()
    x_max = xy[:, 0].max() + 0.1 * x_range
    x_min = xy[:, 0].min() - 0.1 * x_range

    y_range = xy[:, 1].max() - xy[:, 1].min()
    y_max = xy[:, 1].max() + 0.1 * y_range
    y_min = xy[:, 1].min() - 0.1 * y_range

    x_plot = np.linspace(x_min, x_max, 500)
    y_plot = np.linspace(y_min, y_max, 500)

    x_mtx_plot, y_mtx_plot = np.meshgrid(x_plot, y_plot)

    grid = np.column_stack([x_mtx_plot.ravel(), y_mtx_plot.ravel()])

    n = xy.shape[0]
    pairwise = np.sqrt(((xy[:, None, :] - xy[None, :, :]) ** 2).sum(axis=2))
    dbar = pairwise[np.triu_indices(n, k=1)].mean()
    bandwidth = dbar * params.kernel_bandwidth

    kde = KernelDensity(
        kernel="gaussian",
        bandwidth=bandwidth,
    ).fit(
        xy,
        sample_weight=node_raw_weights,
    )
    z_mtx = np.exp(kde.score_samples(grid)).reshape(x_mtx_plot.shape)
    z_mtx = z_mtx / z_mtx.max()
    z_mtx = z_mtx**0.1
    z_mtx[z_mtx < 0.03] = 0.0

    contour_trace = go.Heatmap(
        z=z_mtx,
        x=x_plot,
        y=y_plot,
        opacity=params.contour_opacity,
        showscale=False,
        colorscale=params.colorscale,
    )

    return contour_trace
