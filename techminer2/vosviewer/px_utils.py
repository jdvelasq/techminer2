# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""Utils for network ploting based on ploly.express"""

import pandas as pd
import plotly.graph_objects as go


def px_create_network_chart(
    nx_graph,
    xaxes_range,
    yaxes_range,
    show_axes,
    n_labels,
):
    node_trace = px_create_node_trace(
        nx_graph,
    )

    edge_traces = px_create_edge_traces(
        nx_graph,
    )

    fig = px_create_network_fig(
        edge_traces,
        node_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    fig = px_add_node_labels_to_fig_nodes(
        fig,
        nx_graph,
        n_labels,
    )

    return fig


def px_create_edge_traces(graph):
    """Creates edge traces for a networkx graph."""

    edge_traces = []

    for edge in graph.edges():
        #
        pos_x0 = graph.nodes[edge[0]]["x"]
        pos_y0 = graph.nodes[edge[0]]["y"]
        #
        pos_x1 = graph.nodes[edge[1]]["x"]
        pos_y1 = graph.nodes[edge[1]]["y"]
        #
        color = graph.edges[edge]["color"]
        dash = graph.edges[edge]["dash"]
        width = graph.edges[edge]["width"]

        edge_trace = go.Scatter(
            x=(pos_x0, pos_x1),
            y=(pos_y0, pos_y1),
            line={
                "color": color,
                "dash": dash,
                "width": width,
            },
            hoverinfo="none",
            mode="lines",
        )

        edge_traces.append(edge_trace)

    return edge_traces


def px_create_node_trace(nx_graph):
    """Creates a node trace for a networkx graph."""

    node_x = [data["x"] for _, data in nx_graph.nodes(data=True)]
    node_y = [data["y"] for _, data in nx_graph.nodes(data=True)]
    node_color = [data["color"] for _, data in nx_graph.nodes(data=True)]
    node_size = [data["node_size"] for _, data in nx_graph.nodes(data=True)]
    node_text = [data["text"] for _, data in nx_graph.nodes(data=True)]

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        text=node_text,
        hoverinfo="text",
        marker={
            "color": node_color,
            "size": node_size,
            "line": {"width": 1.5, "color": "white"},
            "opacity": 1.0,
        },
    )

    return node_trace


def px_create_network_fig(
    edge_traces,
    node_trace,
    xaxes_range,
    yaxes_range,
    show_axes,
):
    """Creates a network graph from tracesusing plotly express."""

    layout = go.Layout(
        title="",
        titlefont={"size": 16},
        showlegend=False,
        hovermode="closest",
        margin={"b": 0, "l": 0, "r": 0, "t": 0},
        annotations=[
            {
                "text": "",
                "showarrow": False,
                "xref": "paper",
                "yref": "paper",
                "x": 0.005,
                "y": -0.002,
                "align": "left",
                "font": {"size": 10},
            }
        ],
    )

    fig = go.Figure(
        data=edge_traces + [node_trace],
        layout=layout,
    )

    if show_axes is False:
        fig.update_layout(
            xaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
            },
            yaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
            },
        )

    if xaxes_range is not None:
        fig.update_xaxes(range=xaxes_range)

    if yaxes_range is not None:
        fig.update_yaxes(range=yaxes_range)

    fig.update_layout(
        hoverlabel={
            "bgcolor": "white",
            "font_family": "monospace",
        },
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    return fig


def px_add_node_labels_to_fig_nodes(fig, nx_graph, n_labels):
    """Adds node names to a network figure."""

    node_x = [data["x"] for _, data in nx_graph.nodes(data=True)]

    node_y = [data["y"] for _, data in nx_graph.nodes(data=True)]

    node_labels = [data["text"] for _, data in nx_graph.nodes(data=True)]

    textfont_sizes = [
        data["textfont_size"] for _, data in nx_graph.nodes(data=True)
    ]

    textpositions = [
        data["textposition"] for _, data in nx_graph.nodes(data=True)
    ]

    node_occs = [data["OCC"] for _, data in nx_graph.nodes(data=True)]

    node_citations = [
        data["global_citations"] for _, data in nx_graph.nodes(data=True)
    ]

    frame = pd.DataFrame(
        {
            "name": node_labels,
            "occ": node_occs,
            "citation": node_citations,
        }
    )
    frame = frame.sort_values(["occ", "citation", "name"], ascending=False)
    selected_names = frame["name"].tolist()[:n_labels]

    if n_labels is None:
        n_labels = len(node_labels)

    #
    node_x.reverse()
    node_y.reverse()
    node_labels.reverse()
    textfont_sizes.reverse()
    textpositions.reverse()
    node_occs.reverse()
    #

    for pos_x, pos_y, name, textfont_size, textpos in zip(
        node_x, node_y, node_labels, textfont_sizes, textpositions
    ):
        if name not in selected_names:
            continue

        if textpos == "top right":
            xanchor = "left"
            yanchor = "bottom"
            xshift = 4
            yshift = 4
        elif textpos == "top left":
            xanchor = "right"
            yanchor = "bottom"
            xshift = -4
            yshift = 4
        elif textpos == "bottom right":
            xanchor = "left"
            yanchor = "top"
            xshift = 4
            yshift = -4
        elif textpos == "bottom left":
            xanchor = "right"
            yanchor = "top"
            xshift = -4
            yshift = -4
        else:
            xanchor = "center"
            yanchor = "center"

        # if is_article is True:
        #     name = ", ".join(name.split(", ")[:2])

        fig.add_annotation(
            x=pos_x,
            y=pos_y,
            text=name,
            showarrow=False,
            font={"size": textfont_size},
            bordercolor="grey",
            bgcolor="white",
            xanchor=xanchor,
            yanchor=yanchor,
            xshift=xshift,
            yshift=yshift,
        )

    return fig


###############################################################################


# pylint: disable=too-many-arguments
# def extract_records_per_cluster(
#     communities,
#     field,
#     # Database params:
#     root_dir,
#     database,
#     year_filter,
#     cited_by_filter,
#     **filters,
# ):
#     """Return a dictionary of records per cluster."""

#     def convert_cluster_to_items_dict(communities):
#         """Converts the cluster to items dict."""

#         items2cluster = {}
#         for cluster, items in communities.items():
#             for item in items:
#                 items2cluster[item] = cluster

#         return items2cluster

#     def explode_field(records, field):
#         """Explodes records."""

#         records = records.copy()
#         records = records[field]
#         records = records.dropna()
#         records = records.str.split("; ").explode().map(lambda w: w.strip())

#         return records

#     def select_valid_records(records, clusters):
#         """Selects valid records."""

#         community_terms = []
#         for cluster in clusters.values():
#             community_terms.extend(cluster)

#         records = records.copy()
#         records = records[records.isin(community_terms)]

#         return records

#     def create_raw_cluster_field(records, field, clusters):
#         """Adds a cluster field with non unique elements."""

#         records = records.to_frame()
#         records["clusters"] = records[field].map(clusters)
#         # records["article"] = records.index.to_list()
#         records = records.groupby("article").agg({"clusters": list})
#         records["clusters"] = (
#             records["clusters"].apply(lambda x: sorted(x)).str.join("; ")
#         )

#         return records

#     def compute_cluster(list_of_clusters):
#         """Computes the cluster most frequent in a list."""

#         counter = defaultdict(int)
#         for cluster in list_of_clusters:
#             counter[cluster] += 1
#         return max(counter, key=counter.get)

#     #
#     # Main code:
#     #

#     records_main = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
#     records_main.index = pd.Index(records_main.article)

#     items2cluster = convert_cluster_to_items_dict(communities)
#     exploded_records = explode_field(records_main, field)
#     selected_records = select_valid_records(exploded_records, communities)
#     selected_records = create_raw_cluster_field(
#         selected_records, field, items2cluster
#     )

#     records_main = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
#     records_main.index = pd.Index(records_main.article)

#     records_main["_RAW_CLUSTERS_"] = pd.NA
#     records_main.loc[records_main.index, "_RAW_CLUSTERS_"] = selected_records[
#         "clusters"
#     ]
#     records_main["_CLUSTERS_"] = records_main["_RAW_CLUSTERS_"]
#     records_main = records_main.dropna(subset=["_CLUSTERS_"])
#     records_main["_CLUSTERS_"] = (
#         records_main["_CLUSTERS_"]
#         .str.split("; ")
#         .map(lambda x: [z.strip() for z in x])
#         .map(set)
#         .str.join("; ")
#     )

#     records_main["_ASSIGNED_CLUSTER_"] = (
#         records_main["_RAW_CLUSTERS_"]
#         .str.split("; ")
#         .map(lambda x: [z.strip() for z in x])
#         .map(compute_cluster)
#     )

#     clusters = (
#         records_main["_ASSIGNED_CLUSTER_"].dropna().drop_duplicates().to_list()
#     )

#     records_per_cluster = dict()

#     for cluster in clusters:
#         clustered_records = records_main[
#             records_main._ASSIGNED_CLUSTER_ == cluster
#         ].copy()
#         clustered_records = clustered_records.sort_values(
#             ["global_citations", "local_citations"],
#             ascending=[False, False],
#         )

#         records_per_cluster[cluster] = clustered_records.copy()

#     return records_per_cluster


# def generate_clusters_database(
#     communities,
#     field,
#     # Database params:
#     root_dir,
#     database,
#     year_filter,
#     cited_by_filter,
#     **filters,
# ):
#     """Generates the file root_dir/databases/_CLUSTERS_.csv"""

#     def convert_cluster_to_items_dict(communities):
#         """Converts the cluster to items dict."""

#         items2cluster = {}
#         for cluster, items in communities.items():
#             for item in items:
#                 items2cluster[item] = cluster

#         return items2cluster

#     def explode_field(records, field):
#         """Explodes records."""

#         records = records.copy()
#         records = records[field]
#         records = records.dropna()
#         records = records.str.split("; ").explode().map(lambda w: w.strip())

#         return records

#     def select_valid_records(records, clusters):
#         """Selects valid records."""

#         community_terms = []
#         for cluster in clusters.values():
#             community_terms.extend(cluster)

#         records = records.copy()
#         records = records[records.isin(community_terms)]

#         return records

#     def create_raw_cluster_field(records, field, clusters):
#         """Adds a cluster field with non unique elements."""

#         records = records.to_frame()
#         records["clusters"] = records[field].map(clusters)
#         # records["article"] = records.index.to_list()
#         records = records.groupby("article").agg({"clusters": list})
#         records["clusters"] = (
#             records["clusters"].apply(lambda x: sorted(x)).str.join("; ")
#         )

#         return records

#     #
#     # Main code:
#     #

#     records = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
#     records.index = records.article

#     items2cluster = convert_cluster_to_items_dict(communities)
#     exploded_records = explode_field(records, field)
#     selected_records = select_valid_records(exploded_records, communities)
#     selected_records = create_raw_cluster_field(
#         selected_records, field, items2cluster
#     )

#     records = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
#     records.index = records.article

#     records["_RAW_CLUSTERS_"] = pd.NA
#     records.loc[records.index, "_RAW_CLUSTERS_"] = selected_records["clusters"]
#     records["_CLUSTERS_"] = records["_RAW_CLUSTERS_"]
#     records = records.dropna(subset=["_CLUSTERS_"])
#     records["_CLUSTERS_"] = (
#         records["_CLUSTERS_"]
#         .str.split("; ")
#         .map(lambda x: [z.strip() for z in x])
#         .map(set)
#         .str.join("; ")
#     )

#     database_path = pathlib.Path(root_dir) / "databases" / "_CLUSTERS_.csv"

#     records.to_csv(database_path, index=False, encoding="utf-8")


# def --generate_databases_per_cluster(root_dir):
#     """Generates the files root_dir/databases/_CLUSTER_XX_.csv"""

#     def compute_cluster(list_of_clusters):
#         """Computes the cluster most frequent in a list."""

#         counter = defaultdict(int)
#         for cluster in list_of_clusters:
#             counter[cluster] += 1
#         return max(counter, key=counter.get)

#     #
#     # Main code:
#     #

#     records = read_records(
#         root_dir=root_dir,
#         database="_CLUSTERS_",
#     )

#     records["_ASSIGNED_CLUSTER_"] = (
#         records["_RAW_CLUSTERS_"]
#         .str.split("; ")
#         .map(lambda x: [z.strip() for z in x])
#         .map(compute_cluster)
#     )

#     clusters = (
#         records["_ASSIGNED_CLUSTER_"].dropna().drop_duplicates().to_list()
#     )

#     # Remove existent _CLUSTER_XX_.csv files:
#     database_dir = pathlib.Path(root_dir) / "databases"
#     files = list(database_dir.glob("_CLUSTER_*_.csv"))
#     for file in files:
#         os.remove(file)

#     for cluster in clusters:
#         clustered_records = records[records._ASSIGNED_CLUSTER_ == cluster]
#         clustered_records = clustered_records.sort_values(
#             ["global_citations", "local_citations"],
#             ascending=[False, False],
#         )

#         file_name = f"_CLUSTER_{cluster[-2:]}_.csv"
#         file_path = os.path.join(root_dir, "databases", file_name)
#         clustered_records.to_csv(file_path, index=False, encoding="utf-8")
