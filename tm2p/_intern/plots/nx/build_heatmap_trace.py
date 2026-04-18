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

    # min_weight = node_raw_weights.min()
    # max_weight = node_raw_weights.max()
    # weight_range = max_weight - min_weight
    # node_raw_weights += 3.0 * weight_range

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

    kde1 = KernelDensity(
        kernel="gaussian",
        bandwidth=bandwidth * 0.2,
    ).fit(
        xy,
        sample_weight=0.8 * np.ones(xy.shape[0]),
    )
    z1_mtx = np.exp(kde1.score_samples(grid)).reshape(x_mtx_plot.shape)
    z1_mtx = z1_mtx / z1_mtx.max()
    z1_mtx = z1_mtx**0.1
    z1_mtx[z1_mtx < 0.03] = 0.0

    kde2 = KernelDensity(
        kernel="gaussian",
        bandwidth=bandwidth,
    ).fit(
        xy,
        sample_weight=node_raw_weights,
    )
    z2_mtx = np.exp(kde2.score_samples(grid)).reshape(x_mtx_plot.shape)
    z2_mtx = z2_mtx / z2_mtx.max()
    z2_mtx = z2_mtx**0.1
    z2_mtx[z2_mtx < 0.03] = 0.0

    z_final = 0.75 * z1_mtx + 0.25 * z2_mtx
    z_final = z_final**0.35
    z_final = z_final / z_final.max()
    z_final[z_final < 0.03] = 0.0

    contour_trace = go.Heatmap(
        # z=0.1 * z1_mtx + 0.9 * z2_mtx,
        # z=1.0 * z1_mtx + 0.0 * z2_mtx,
        z=0.0 * z1_mtx + 1.0 * z2_mtx,
        x=x_plot,
        y=y_plot,
        opacity=params.contour_opacity,
        showscale=False,
        colorscale=params.colorscale,
    )

    return contour_trace


def build_contour_trace_1(
    params: Params,
    nx_graph: nx.Graph,
) -> go.Contour:

    node_x = [data["x"] for _, data in nx_graph.nodes(data=True)]
    node_y = [data["y"] for _, data in nx_graph.nodes(data=True)]
    node_raw_weights = np.asarray(
        [data["raw_node_size"] for _, data in nx_graph.nodes(data=True)],
        dtype=float,
    )

    # min_weight = node_raw_weights.min()
    # max_weight = node_raw_weights.max()
    # weight_range = max_weight - min_weight
    # node_raw_weights += 3.0 * weight_range

    xy = np.column_stack([node_x, node_y]).astype(float)

    n = xy.shape[0]
    pairwise = np.sqrt(((xy[:, None, :] - xy[None, :, :]) ** 2).sum(axis=2))
    dbar = pairwise[np.triu_indices(n, k=1)].mean()
    bandwidth = dbar * params.kernel_bandwidth

    kde = KernelDensity(
        bandwidth=bandwidth,
        kernel="gaussian",
    ).fit(
        xy,
        sample_weight=node_raw_weights,
    )

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

    z_mtx = np.exp(kde.score_samples(grid)).reshape(x_mtx_plot.shape)
    z_mtx = z_mtx / z_mtx.max()
    z_mtx = z_mtx**0.5

    contour_trace = go.Contour(
        z=z_mtx,
        x=x_plot,
        y=y_plot,
        opacity=params.contour_opacity,
        showscale=False,
        colorscale=params.colorscale,
    )

    return contour_trace
