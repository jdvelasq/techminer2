# flake8: noqa
"""
Main Path Analysis
===============================================================================

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> results = techminer2plus.report.intellectual_structure.main_path_analysis(
...     root_dir,
...     nx_k=None,
...     nx_iterations=30,
...     nx_seed=2,
... )
--INFO-- Paths computed
--INFO-- Points per link computed
--INFO-- Points per path computed


>>> file_name = "sphinx/_static/report/main_path.html"
>>> results.plot_.write_html(file_name)


.. raw:: html

    <iframe src="../../../../_static/report/main_path.html" height="600px" width="100%" frameBorder="0"></iframe>

# pylint: disable=line-too-long
"""

import copy

import networkx as nx

# from ...records import read_records
# from .historiograph import historiograph

#
# The function main_path_analysis apply the main path algorithm to the documents
# of the dataset
#


def main_path_analysis(
    root_dir="./",
    #
    node_size=10,
    n_labels=None,
    color="#8da4b4",
    textfont_size=10,
    nx_k=None,
    nx_iterations=50,
    nx_seed=0,
):
    """Main Path Analysis"""

    documents_in_main_path = _compute_main_path(root_dir)
    return historiograph(
        top_n=None,
        root_dir=root_dir,
        # Parameter used for main_path:
        selected_articles=documents_in_main_path,
        # Graph params:
        node_size=node_size,
        n_labels=n_labels,
        color=color,
        textfont_size=textfont_size,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_seed=nx_seed,
    )


def _compute_main_path(directory):
    """Implments the main path algorithm."""

    # Creates the links of the citation network
    records = read_records(directory)
    links = records[["local_references", "article"]]
    links = _create_citation_network_links(links)

    # Gets the start and end nodes of the co-citation network
    start_nodes = _get_start_nodes(links)
    end_nodes = _get_end_nodes(links)

    paths = _compute_network_paths(links, start_nodes, end_nodes)
    print("--INFO-- Paths computed")

    links = links.assign(points=0)
    links = _compute_points_per_link(links, paths)
    print("--INFO-- Points per link computed")

    paths = _compute_points_per_path(links, paths)
    print("--INFO-- Points per path computed")

    # sort paths by points (descending)
    paths = sorted(paths, key=lambda x: x[1], reverse=True)

    max_points = paths[0][1]

    # obtains the best paths
    best_paths = [path for path in paths if path[1] == max_points]

    # creates a subset of documents with only the articles in the best
    # the order of documents_in_main_path is the same as in best_path
    documents_in_main_path = set(
        [article for path in best_paths for article in path[0]]
    )

    # documents_in_main_path = records[records.article.isin(documents_in_main_path)]
    # documents_in_main_path = documents_in_main_path.assign(order=0)
    # for i, article in enumerate(best_path[0]):
    #     documents_in_main_path.loc[
    #         documents_in_main_path.article == article, "order"
    #     ] = i
    # documents_in_main_path = documents_in_main_path.sort_values(by="order")

    # documents_in_main_path.index = documents_in_main_path.article
    # documents_in_main_path = documents_in_main_path.assign(
    #     short_name=documents_in_main_path.index
    # )
    # documents_in_main_path = documents_in_main_path.assign(
    #     short_name=documents_in_main_path.short_name.str.split(", ")
    #     .str[:2]
    #     .str.join(", ")
    # )

    return documents_in_main_path


def _create_citation_network_links(records):
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


def _get_start_nodes(links):
    """Returns a list with the start nodes (most recent documents) of citation network."""

    links = links.copy()
    source_nodes = set(links.citing_article.drop_duplicates().tolist()) - set(
        links.cited_article.drop_duplicates().tolist()
    )

    return source_nodes


def _get_end_nodes(links):
    """Returns a list with the end nodes (most oldest documents)of citation network."""

    links = links.copy()
    target_nodes = set(links.cited_article.drop_duplicates().tolist()) - set(
        links.citing_article.drop_duplicates().tolist()
    )

    return target_nodes


def _compute_network_paths(links, start_nodes, end_nodes):
    """Computes all posible paths from start_nodes to end_nodes."""

    current_paths = [[[node], 0] for node in start_nodes]
    found_paths, current_paths = _expand_network_paths(
        links, end_nodes, [], current_paths
    )
    return found_paths


def _expand_network_paths(links, end_nodes, found_paths, current_paths):
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
        found_paths, new_paths = _expand_network_paths(
            links, end_nodes, found_paths, new_paths
        )

    return found_paths, new_paths


def _compute_points_per_link(links, paths):
    """Computes the points per link in each path."""

    for path in paths:
        for link in zip(path[0], path[0][1:]):
            links.loc[
                (links.citing_article == link[0])
                & (links.cited_article == link[1]),
                "points",
            ] += 1
    return links


def _compute_points_per_path(links, paths):
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


def _create_main_path_graph(documents, nx_k=0.1, nx_iterations=10, delta=1.0):
    graph = _build_graph(documents.short_name.to_list())
    return get_network_graph_plot(
        graph,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        delta=1.0,
    )


def _build_graph(nodes):
    graph = nx.DiGraph()
    graph = _create_nodes(graph, nodes)
    graph = _create_edges(graph, nodes)
    return graph


def _create_nodes(graph, nodes):
    nodes = [(node, {"group": 0}) for node in nodes]
    graph.add_nodes_from(nodes)
    return graph


def _create_edges(graph, nodes):
    for source_node, target_node in zip(nodes[:-1], nodes[1:]):
        graph.add_edge(source_node, target_node)
    return graph


def _create_prompts(documents):
    prompts = []
    for _, row in documents.iterrows():
        prompt = f"Summarize the following text in 30 words or less:\n\n{row.abstract}\n\n"
        prompts.append(prompt)
    return prompts
