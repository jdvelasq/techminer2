"""
Main Path Analysis
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.tools.main_path_analysis(directory)




"""
import copy
import sys
from dataclasses import dataclass
from pprint import pprint

#
# The function main_path_analysis apply the main path algorithm to the documents
# of the dataset
#
import pandas as pd

from ..._read_records import read_records
from ..reports.abstracts_report import _write_report


class _Results:
    table_ = None
    plot_ = None


def main_path_analysis(directory="./"):
    """
    This function computes the main path algorithm to found the path of
    cocited documents in the dataset.

    Parameters
    ----------
    directory : str
        The path to the directory where the dataset is stored.

    Returns


    """

    documents = read_records(directory)

    # creates a subset of documents with only the columns 'local_references' and 'article'
    links = documents[["local_references", "article"]]

    # creates a list of links between documents
    links = _create_links(links)
    # ------------------------------------------------------------------------------
    # links = pd.DataFrame(
    #     {
    #         "source": list("ABBBCCDDEFFGHIIJM"),
    #         "target": list("CCDJEHFIGHIHKLMMN"),
    #     }
    # )
    # ------------------------------------------------------------------------------
    # assigns 0 points to the links
    links = links.assign(points=0)

    # obtains the start and end nodes from links
    start_nodes = _get_start_nodes(links)
    end_nodes = _get_end_nodes(links)

    # computes the paths between the start and end nodes
    paths = _compute_paths(links, start_nodes, end_nodes)
    sys.stdout.write("--INFO-- Paths computed\n")

    # compute points per link in each path
    links = _compute_points_per_link(links, paths)
    sys.stdout.write("--INFO-- Points per link computed\n")

    # compute points per path
    paths = _compute_points_per_path(links, paths)
    sys.stdout.write("--INFO-- Points per computed\n")

    # sort paths by points (descending)
    paths = sorted(paths, key=lambda x: x[1], reverse=True)

    # obtains the best path
    best_path = paths[0]

    # creates a subset of documents with only the articles in the best
    # the order of documents_in_main_path is the same as in best_path
    documents_in_main_path = documents[documents.article.isin(best_path[0])]
    documents_in_main_path = documents_in_main_path.assign(order=0)
    for i, article in enumerate(best_path[0]):
        documents_in_main_path.loc[
            documents_in_main_path.article == article, "order"
        ] = i
    documents_in_main_path = documents_in_main_path.sort_values(by="order")

    # writes the report
    _write_report(
        "author_keywords",
        file_name="main_path_analysis.txt",
        use_textwrap=True,
        directory=directory,
        records=documents_in_main_path,
    )


def _compute_points_per_path(links, paths):
    for path in paths:
        for link in zip(path[0], path[0][1:]):
            path[1] += sum(
                links.loc[
                    (links.source == link[0]) & (links.target == link[1]), "points"
                ]
            )
    return paths


def _compute_points_per_link(links, paths):
    for path in paths:
        for link in zip(path[0], path[0][1:]):
            links.loc[
                (links.source == link[0]) & (links.target == link[1]), "points"
            ] += 1
    return links


def _get_end_nodes(links):
    # Retuns a list with the end nodes in the network from links. The end nodes
    # are the nodes in the target column that are not in the source column.

    # creates a copy of links
    links = links.copy()

    # removes the rows with NaN values in the column 'source'
    links = links.dropna(subset=["source"])

    # removes the rows with NaN values in the column 'target'
    links = links.dropna(subset=["target"])

    # creates a list with the target nodes
    target_nodes = set(links.target.unique().tolist()) - set(
        links.source.unique().tolist()
    )

    return target_nodes


def _get_start_nodes(links):
    """Returns a list with the start nodes in the network from links. The
    start nodes are the nodes in the source column that are not in the target column.


    Parameters
    ----------
    links : pandas.DataFrame
        A dataframe with columns 'source' and 'target' containing the links.

    Returns
    -------
    list
        A list with the source nodes in the network.

    """

    # creates a copy of links
    links = links.copy()

    # removes the rows with NaN values in the column 'source'
    links = links.dropna(subset=["source"])

    # removes the rows with NaN values in the column 'target'
    links = links.dropna(subset=["target"])

    # creates a list with the source nodes
    source_nodes = set(links.source.unique().tolist()) - set(
        links.target.unique().tolist()
    )

    return source_nodes


def _compute_paths(links, start_nodes, end_nodes):
    current_paths = [[[node], 0] for node in start_nodes]
    found_paths, current_paths = _expand_paths(links, end_nodes, [], current_paths)
    return found_paths


def _expand_paths(links, end_nodes, found_paths, current_paths):
    # stack of founded  complete paths
    found_paths = copy.deepcopy(found_paths)

    new_paths = []

    for current_path in current_paths:
        last_node = current_path[0][-1]

        if last_node in end_nodes:
            found_paths.append(copy.deepcopy(current_path))
            continue

        df = links[links.source == last_node].copy()

        for _, row in df.iterrows():
            new_path = copy.deepcopy(current_path)

            new_path[0].append(row.target)
            # new_path[1] += row.points
            new_paths.append(new_path)

    if len(new_paths) > 0:
        found_paths, new_paths = _expand_paths(links, end_nodes, found_paths, new_paths)

    return found_paths, new_paths


def _create_links(documents):
    """Creates a list of links between documents based on the local references.

    Parameters
    ----------
    documents : pandas.DataFrame
        A dataframe with columns 'local_references' and 'article'.

    Returns
    -------
    pandas.DataFrame
        A dataframe with columns 'source' and 'target' containing the links.
        The 'source' column contains a reference in the 'target' column.

    """

    # creates a copy of documents
    documents = documents.copy()

    # Split the column 'local_references' by '; ' and then explodes the column
    # to create a row for each reference if the value in not NaN
    documents = documents.assign(
        local_references=documents.local_references.str.split("; ")
    )

    for _, row in documents.dropna().iterrows():
        if row.article in row.local_references:
            row.local_references.remove(row.article)

    #     assert (
    #         row.article not in row.local_references
    #     ), "The article is in the local references"

    documents = documents.explode("local_references")

    # Remote spaces at the beginning and end of the string in the column
    # 'local_references'
    documents = documents.assign(
        local_references=documents.local_references.str.strip()
    )

    # rename the column 'local_references' to 'source' and the column 'article'
    # to 'target'
    documents = documents.rename(
        columns={"local_references": "source", "article": "target"}
    )

    # removes the rows with NaN values in the column 'source'
    documents = documents.dropna(subset=["source"])

    # removes the rows with NaN values in the column 'target'
    documents = documents.dropna(subset=["target"])

    # drop duplicates
    documents = documents.drop_duplicates()

    return documents


############################################################################################################


# def _build_paths(links, start_nodes, end_nodes):
#     links = links.copy()
#     paths = []
#     for node in start_nodes:
#         paths.append(_build_path_aux(links, node, end_nodes))
#     return paths


# def _build_path_aux(links, current_node, end_nodes):
#     df = links[links.source == current_node]
#     if len(df) == 0:
#         return []
#     path = [current_node]
#     for _, row in df.iterrows():
#         if row.target in end_nodes:
#             return path.extend([row.target])
#         else:
#             following = _build_path_aux(links, row.target, end_nodes)
#             path.extend(following)
#     return path


# def _compute_points_per_link(links, start_nodes, end_nodes):
#     links = links.copy()

#     # adds one point to all the links that have a start node as source
#     links.loc[links.source.map(lambda x: x in start_nodes), "points"] += 1

#     # selects the links that have a start node as source and a target node that is not a end node
#     current_links = links[links.source.map(lambda x: x in start_nodes)].copy()
#     current_links = current_links[
#         current_links.target.map(lambda x: x not in end_nodes)
#     ]

#     if len(current_links) == 0:
#         return links

#     start_nodes = set(current_links.target.unique().tolist())
#     links = _compute_points_per_link(links, start_nodes, end_nodes)
#     return links


# def _compute_points_per_link_aux(links, path):
#     links = links.copy()

#     if isinstance(path, list):
#         for path_ in path:
#             links = _compute_points_per_link_aux(links, path_)

#     else:
#         source = path[0]
#         target = path[1]
#         links.loc[(links.source == source) & (links.target == target), "points"] += 1

#     return links


def _build_path(links, current_node, end_nodes):
    df = links[links.source == current_node]
    if len(df) == 0:
        return [current_node, None]
    path = []
    for _, row in df.iterrows():
        if row.target in end_nodes:
            return [current_node, row.target]
        else:
            following = _build_path(links, row.target, end_nodes)
            path.append([current_node, following])

    return path


def _create_paths(links, start_nodes, end_nodes):
    # computes all the posibles paths between the start nodes and the end nodes
    # in the network

    # creates a copy of links
    links = links.copy()

    # removes the rows with NaN values in the column 'source'
    links = links.dropna(subset=["source"])

    # removes the rows with NaN values in the column 'target'
    links = links.dropna(subset=["target"])

    # creates a list with the target nodes
