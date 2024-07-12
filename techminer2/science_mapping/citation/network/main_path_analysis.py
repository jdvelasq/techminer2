# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Main Path Analysis
===============================================================================

>>> from techminer2.science_mapping.citation.network import main_path_analysis
>>> results = main_path_analysis(
...     #
...     # COLUMN PARAMS:
...     top_n=None,
...     citations_threshold=0,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_size_range=(30, 70),
...     textfont_size_range=(10, 20),
...     textfont_opacity_range=(0.35, 1.00),
...     #
...     # EDGES:
...     edge_color="#7793a5",
...     edge_width_range=(0.8, 3.0),
...     #
...     # DATABASE PARAMS:
...     root_dir="example/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- Paths computed
--INFO-- Points per link computed
--INFO-- Points per path computed
--INFO-- The file 'example/reports/main_path_analysis.txt' was created.
>>> results.fig_.write_html("sphinx/_static/analyze/citation/network/main_path_analysis.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/network/main_path_analysis.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> results.df_.head()
                                      citing_article  ... points
0  Gomber P., 2018, J MANAGE INF SYST, V35, P220 ...  ...      3
1  Gomber P., 2018, J MANAGE INF SYST, V35, P220 ...  ...      3
2                   Hu Z., 2019, SYMMETRY, V11 1:176  ...      4
3       Alt R., 2018, ELECTRON MARK, V28, P235 1:150  ...      1
4       Alt R., 2018, ELECTRON MARK, V28, P235 1:150  ...      2
<BLANKLINE>
[5 rows x 3 columns]

"""

import copy
from dataclasses import dataclass

import networkx as nx
import numpy as np

from ...._common.format_report_for_records import format_report_for_records
from ...._common.nx_compute_edge_width_from_edge_weight import (
    nx_compute_edge_width_from_edge_weight,
)
from ...._common.nx_compute_node_size_from_item_citations import (
    nx_compute_node_size_from_item_citations,
)
from ...._common.nx_compute_spring_layout import nx_compute_spring_layout
from ...._common.nx_compute_textfont_opacity_from_item_citations import (
    nx_compute_textfont_opacity_from_item_citations,
)
from ...._common.nx_compute_textfont_size_from_item_citations import (
    nx_compute_textfont_size_from_item_citations,
)
from ...._common.nx_compute_textposition_from_graph import (
    nx_compute_textposition_from_graph,
)
from ...._common.nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from ...._common.nx_set_node_color_to_constant import nx_set_node_color_to_constant
from ...._common.nx_visualize_graph import nx_visualize_graph
from ....core.read_records import read_records


def main_path_analysis(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    #
    # Creates a table with citing and cited articles
    data_frame = ___create_citations_table(
        #
        # NETWORK PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Extracts the articles in the main path(s)
    articles_in_main_path, data_frame = ___compute_main_path(data_frame)

    #
    # Filters the table
    data_frame = data_frame[
        (data_frame.citing_article.isin(articles_in_main_path))
        & (data_frame.cited_article.isin(articles_in_main_path))
    ]

    #
    # Create the networkx graph
    nx_graph = nx.Graph()

    ___generate_report(
        articles=articles_in_main_path,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Adds the links to the network:
    for _, row in data_frame.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row.citing_article, row.cited_article, row.points)],
            dash="solid",
        )

    #
    # Sets the layout
    nx_graph = nx_set_node_color_to_constant(nx_graph, "#7793a5")
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)
    nx_graph = nx_compute_node_size_from_item_citations(nx_graph, node_size_range)
    nx_graph = nx_compute_textfont_size_from_item_citations(
        nx_graph, textfont_size_range
    )
    nx_graph = nx_compute_textfont_opacity_from_item_citations(
        nx_graph, textfont_opacity_range
    )

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_range)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)
    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    @dataclass
    class Results:
        fig_ = nx_visualize_graph(
            #
            # FUNCTION PARAMS:
            nx_graph=nx_graph,
            #
            # NETWORK PARAMS:
            xaxes_range=None,
            yaxes_range=None,
            show_axes=False,
            #
            # ARROWS:
            draw_arrows=True,
        )
        df_ = data_frame.reset_index(drop=True)

    return Results()


def ___generate_report(
    articles,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    articles = [" ".join(article.split(" ")[:-1]) for article in articles]

    #
    # Extracts the records using the specified parameters
    records = read_records(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    records = records[records.article.isin(articles)]

    format_report_for_records(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename="main_path_analysis.txt",
    )


def ___compute_main_path(data_frame):
    """Implments the main path algorithm."""

    # Creates the links of the citation network
    data_frame = data_frame.copy()

    #
    # Computes the start nodes in the citation network
    def compute_start_nodes(data_frame):
        data_frame = data_frame.copy()
        return set(data_frame.citing_article.drop_duplicates().tolist()) - set(
            data_frame.cited_article.drop_duplicates().tolist()
        )

    start_nodes = compute_start_nodes(data_frame)

    #
    # Computes the end nodes in the citation network
    def compute_end_nodes(data_frame):
        data_frame = data_frame.copy()
        return set(data_frame.cited_article.drop_duplicates().tolist()) - set(
            data_frame.citing_article.drop_duplicates().tolist()
        )

    end_nodes = compute_end_nodes(data_frame)

    #
    # Compute paths
    def compute_all_network_paths(data_frame, start_nodes, end_nodes):
        """Computes all possible paths in the citattion network from start nodes to end nodes"""

        # This is a recursive process where new node is added to each path in
        # each iteration until the end node is reached.
        def expand_network_paths(data_frame, end_nodes, found_paths, current_paths):
            """Stack of founded complete paths"""

            found_paths = copy.deepcopy(found_paths)

            new_paths = []

            for current_path in current_paths:
                last_node = current_path[0][-1]

                if last_node in end_nodes:
                    found_paths.append(copy.deepcopy(current_path))
                    continue

                valid_links = data_frame[data_frame.citing_article == last_node].copy()

                for _, row in valid_links.iterrows():
                    new_path = copy.deepcopy(current_path)
                    new_path[0].append(row.cited_article)
                    new_paths.append(new_path)

            if len(new_paths) > 0:
                found_paths, new_paths = expand_network_paths(
                    data_frame, end_nodes, found_paths, new_paths
                )

            return found_paths, new_paths

        #
        # Main code:
        data_frame = data_frame.copy()
        current_paths = [[[node], 0] for node in start_nodes]
        found_paths, current_paths = expand_network_paths(
            data_frame, end_nodes, [], current_paths
        )
        return found_paths

    paths = compute_all_network_paths(data_frame, start_nodes, end_nodes)
    print("--INFO-- Paths computed")

    #
    # Computes the points per link in each path
    def compute_points_per_link(data_frame, paths):
        for path in paths:
            for link in zip(path[0], path[0][1:]):
                data_frame.loc[
                    (data_frame.citing_article == link[0])
                    & (data_frame.cited_article == link[1]),
                    "points",
                ] += 1
        return data_frame

    data_frame = data_frame.assign(points=0)
    data_frame = compute_points_per_link(data_frame, paths)
    print("--INFO-- Points per link computed")

    #
    # Computes the points per path as the sum of points per link
    # in the path
    def compute_points_per_path(data_frame, paths):
        """Computes the points per path."""

        for path in paths:
            for link in zip(path[0], path[0][1:]):
                path[1] += sum(
                    data_frame.loc[
                        (data_frame.citing_article == link[0])
                        & (data_frame.cited_article == link[1]),
                        "points",
                    ]
                )
        return paths

    paths = compute_points_per_path(data_frame, paths)
    print("--INFO-- Points per path computed")

    #
    # Sort paths by points (descending)
    paths = sorted(paths, key=lambda x: x[1], reverse=True)
    max_points = paths[0][1]

    #
    # Obtains the best paths
    best_paths = [path for path in paths if path[1] == max_points]

    # Creates a subset of documents with only the articles in the best
    # the order of documents_in_main_path is the same as in best_path
    article_in_main_path = set(article for path in best_paths for article in path[0])

    return article_in_main_path, data_frame


def _create_prompts(documents):
    prompts = []
    for _, row in documents.iterrows():
        prompt = (
            f"Summarize the following text in 30 words or less:\n\n{row.abstract}\n\n"
        )
        prompts.append(prompt)
    return prompts


def ___create_citations_table(
    #
    # NETWORK PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    #
    # Extracts the records using the specified parameters
    records = read_records(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records = records.sort_values(
        ["global_citations", "local_citations", "year", "article"],
        ascending=[False, False, False, True],
    )

    if citations_threshold is not None:
        records = records.loc[records.global_citations >= citations_threshold, :]
    if top_n is not None:
        records = records.head(top_n)

    #
    # Builds a dataframe with citing and cited articles
    data_frame = records[["article", "local_references", "global_citations"]]

    data_frame["local_references"] = data_frame.local_references.str.split(";")
    data_frame = data_frame.explode("local_references")
    data_frame["local_references"] = data_frame["local_references"].str.strip()

    data_frame = data_frame[
        data_frame["local_references"].map(lambda x: x in data_frame.article.to_list())
    ]

    #
    # Adds citations to the article
    max_citations = records.global_citations.max()
    n_zeros = int(np.log10(max_citations - 1)) + 1
    fmt = " 1:{:0" + str(n_zeros) + "d}"
    #
    rename_dict = {
        key: value
        for key, value in zip(
            records["article"].to_list(),
            (
                records["article"] + records["global_citations"].map(fmt.format)
            ).to_list(),
        )
    }
    #
    data_frame["article"] = data_frame["article"].map(rename_dict)
    data_frame["local_references"] = data_frame["local_references"].map(rename_dict)

    #
    # Creates the citation network
    data_frame = data_frame[["article", "local_references"]]
    data_frame = data_frame.rename(
        columns={
            "article": "citing_article",
            "local_references": "cited_article",
        }
    )

    data_frame = data_frame.dropna()

    return data_frame
