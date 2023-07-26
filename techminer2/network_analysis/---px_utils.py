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


###############################################################################


# pylint: disable=too-many-arguments

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
