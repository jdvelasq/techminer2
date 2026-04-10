def assign_cluster_numbers_by_cluster_size(
    items: list[str],
    clusters: list[int],
) -> dict[int, list[str]]:

    mapping = dict(zip(items, clusters))

    basic_c2i: dict[int, list[str]] = {}
    for member, cluster in mapping.items():
        basic_c2i.setdefault(cluster, []).append(member)

    values = list(basic_c2i.values())

    def f(x):
        return (
            len(x),
            x[0].split(" ")[-1].split(":")[0],
            x[0].split(" ")[-1].split(":")[1],
            x,
        )

    sorted_clusters = sorted(values, key=f, reverse=True)
    sorted_mapping: dict[int, list[str]] = {}
    for sorted_cluster, cluster_items in enumerate(sorted_clusters):
        sorted_mapping[sorted_cluster] = cluster_items

    return sorted_mapping
