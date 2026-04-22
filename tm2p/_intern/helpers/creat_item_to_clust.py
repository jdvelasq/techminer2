from .assign_clust_num_by_clust_size import assign_cluster_numbers_by_cluster_size


def create_item_to_cluster(items: list[str], clusters: list[int]):

    cluster_to_items = assign_cluster_numbers_by_cluster_size(items, clusters)
    item_to_cluster = {}
    for cluster, cluster_items in cluster_to_items.items():
        for item in cluster_items:
            item_to_cluster[item] = cluster

    return item_to_cluster
