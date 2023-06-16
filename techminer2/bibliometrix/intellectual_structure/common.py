# flake8: noqa
"""
Common functions for network-based reference analysis.

"""
import copy

from ...record_utils import read_records


def compute_main_path(directory):
    """Implments the main path algorithm."""

    # Creates the links of the citation network
    records = read_records(directory)
    links = records[["local_references", "article"]]
    links = create_citation_network_links(links)

    # Gets the start and end nodes of the co-citation network
    start_nodes = get_start_nodes(links)
    end_nodes = get_end_nodes(links)

    paths = compute_network_paths(links, start_nodes, end_nodes)
    print("--INFO-- Paths computed")

    links = links.assign(points=0)
    links = compute_points_per_link(links, paths)
    print("--INFO-- Points per link computed")

    paths = compute_points_per_path(links, paths)
    print("--INFO-- Points per path computed")

    # sort paths by points (descending)
    paths = sorted(paths, key=lambda x: x[1], reverse=True)

    # obtains the best paths
    best_path = paths[0]

    # creates a subset of documents with only the articles in the best
    # the order of documents_in_main_path is the same as in best_path
    documents_in_main_path = records[records.article.isin(best_path[0])]
    documents_in_main_path = documents_in_main_path.assign(order=0)
    for i, article in enumerate(best_path[0]):
        documents_in_main_path.loc[
            documents_in_main_path.article == article, "order"
        ] = i
    documents_in_main_path = documents_in_main_path.sort_values(by="order")

    documents_in_main_path.index = documents_in_main_path.article
    documents_in_main_path = documents_in_main_path.assign(
        short_name=documents_in_main_path.index
    )
    documents_in_main_path = documents_in_main_path.assign(
        short_name=documents_in_main_path.short_name.str.split(", ")
        .str[:2]
        .str.join(", ")
    )

    return documents_in_main_path


def create_citation_network_links(records):
    """Creates a list of links between documents based on the local references."""

    # records contains the main database
    records = records.copy()

    records["local_references"] = records["local_references"].str.split("; ")

    # Sanity check: remove the article from its own local references
    for _, row in records.dropna().iterrows():
        if row.article in row.local_references:
            row.local_references.remove(row.article)

    records = records.explode("local_references")
    records["local_references"] = records.local_references.str.strip()

    records = records.rename(
        columns={
            "local_references": "cited_article",
            "article": "citing_article",
        }
    )

    # removes the rows with NaN values or duplicated.
    records = records.dropna(subset=["cited_article"])
    records = records.dropna(subset=["citing_article"])
    records = records.drop_duplicates()

    return records


def get_start_nodes(links):
    """Returns a list with the start nodes (most recent documents) of citation network."""

    links = links.copy()
    source_nodes = set(links.citing_article.drop_duplicates().tolist()) - set(
        links.cited_article.drop_duplicates().tolist()
    )

    return source_nodes


def get_end_nodes(links):
    """Returns a list with the end nodes (most oldest documents)of citation network."""

    links = links.copy()
    target_nodes = set(links.cited_article.drop_duplicates().tolist()) - set(
        links.citing_article.drop_duplicates().tolist()
    )

    return target_nodes


def compute_network_paths(links, start_nodes, end_nodes):
    """Computes all posible paths from start_nodes to end_nodes."""

    current_paths = [[[node], 0] for node in start_nodes]
    found_paths, current_paths = expand_network_paths(
        links, end_nodes, [], current_paths
    )
    return found_paths


def expand_network_paths(links, end_nodes, found_paths, current_paths):
    """Stack of founded complete paths"""

    found_paths = copy.deepcopy(found_paths)

    new_paths = []

    for current_path in current_paths:
        last_node = current_path[0][-1]

        if last_node in end_nodes:
            found_paths.append(copy.deepcopy(current_path))
            continue

        valid_links = links[links.citing_article == last_node].copy()

        for _, row in valid_links.iterrows():
            new_path = copy.deepcopy(current_path)
            new_path[0].append(row.cited_article)
            new_paths.append(new_path)

    if len(new_paths) > 0:
        found_paths, new_paths = expand_network_paths(
            links, end_nodes, found_paths, new_paths
        )

    return found_paths, new_paths


def compute_points_per_link(links, paths):
    """Computes the points per link in each path."""

    for path in paths:
        for link in zip(path[0], path[0][1:]):
            links.loc[
                (links.citing_article == link[0])
                & (links.cited_article == link[1]),
                "points",
            ] += 1
    return links


def compute_points_per_path(links, paths):
    """Computes the points per path."""

    for path in paths:
        for link in zip(path[0], path[0][1:]):
            path[1] += sum(
                links.loc[
                    (links.citing_article == link[0])
                    & (links.cited_article == link[1]),
                    "points",
                ]
            )
    return paths
