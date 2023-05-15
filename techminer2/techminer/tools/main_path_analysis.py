"""
Main Path Analysis
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import techminer
>>> r = techminer.tools.main_path_analysis(directory)
--INFO-- Paths computed
--INFO-- Points per link computed
--INFO-- Points per path computed
--INFO-- The file 'data/regtech/reports/main_path_analysis.txt' was created

>>> print(r.prompts_[0])
Summarize the following text in 30 words or less:
<BLANKLINE>
the purpose of this paper is to develop an insight and review the effect of fintech development against the broader environment in financial technology. we further aim to offer various perspectives in order to aid the understanding of the disruptive potential of fintech, and its implications for the wider financial ecosystem. by drawing upon very recent and highly topical research on this area this study examines the implications for financial institutions, and regulation especially when technology poses a challenge to the global banking and regulatory system. it is driven by a wide-ranging overview of the development, the current state, and possible future of fintech. this paper attempts to connect practitioner-led and academic research. while it draws on academic research, the perspective it takes is also practice-oriented. it relies on the current academic literature as well as insights from industry sources, action research and other publicly available commentaries. it also draws on professional practitioners roundtable discussions, and think-tanks in which the author has been an active participant. we attempt to interpret banking, and regulatory issues from a behavioural perspective. the last crisis exposed significant failures in regulation and supervision. it has made the financial market law and compliance a key topic on the current agenda. disruptive technological change also seems to be important in investigating regulatory compliance followed by change. we contribute to the current literature review on financial and digital innovation by new entrants where this has also practical implications. we also provide for an updated review of the current regulatory issues addressing the contextual root causes of disruption within the financial services domain. the aim here is to assist market participants to improve effectiveness and collaboration. the difficulties arising from extensive regulation may suggest a more liberal and principled approach to financial regulation. disruptive innovation has the potential for welfare outcomes for consumers, regulatory, and supervisory gains as well as reputational gains for the financial services industry. it becomes even more important as the financial services industry evolves. for example, the preparedness of the regulators to instil culture change and harmonise technological advancements with regulation could likely achieve many desired outcomes. such results range from achieving an orderly market growth, further aiding systemic stability and restoring trust and confidence in the financial system. our action-led research results have implications for both research and practice. these should be of interest to regulatory standard setters, investors, international organisations and other academics who are researching regulatory and competition issues, and their manifestation within the financial and social contexts. as a perspective on a social construct, this study appeals to regulators and law makers, entrepreneurs, and investors who participate in technology applied within the innovative financial services domain. it is also of interest to bankers who might consider fintech and strategic partnerships as a prospective, future strategic direction.1  2018 elsevier inc.
<BLANKLINE>
<BLANKLINE>

>>> file_name = "sphinx/_static/techminer__tools__main_path.html"
>>> r.plot_.write_html(file_name)


.. raw:: html

    <iframe src="../../../../_static/techminer__tools__main_path.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import copy
import sys
from dataclasses import dataclass
from pprint import pprint

import networkx as nx

#
# The function main_path_analysis apply the main path algorithm to the documents
# of the dataset
#
import pandas as pd

from ..._get_network_graph_plot import get_network_graph_plot
from ..._read_records import read_records
from ..reports.abstracts_report import _write_report


@dataclass(init=False)
class _Results:
    table_ = None
    plot_ = None
    prompts_ = None


def main_path_analysis(directory="./", nx_k=0.5, nx_iterations=10, delta=1.0):
    """
    This function computes the main path algorithm to found the path of
    cocited documents in the dataset.

    Parameters
    ----------
    directory : str
        The path to the directory where the dataset is stored.

    Returns





    """

    results = _Results()
    documents_in_main_path = _compute_main_path(directory)

    _write_report(
        "author_keywords",
        file_name="main_path_analysis.txt",
        use_textwrap=True,
        directory=directory,
        records=documents_in_main_path,
    )

    results.table_ = documents_in_main_path.copy()
    results.prompts_ = _create_prompts(documents_in_main_path)
    results.plot_ = _create_main_path_graph(
        documents_in_main_path, nx_k, nx_iterations, delta
    )
    return results


def _create_main_path_graph(documents, nx_k=0.5, nx_iterations=10, delta=1.0):
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
        prompt = (
            f"Summarize the following text in 30 words or less:\n\n{row.abstract}\n\n"
        )
        prompts.append(prompt)
    return prompts


def _compute_main_path(directory):
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
    sys.stdout.write("--INFO-- Points per path computed\n")

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
