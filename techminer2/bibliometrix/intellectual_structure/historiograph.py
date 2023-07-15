# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Historiograph
===============================================================================



>>> root_dir = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.intellectual_structure.historiograph(
...     top_n=20,
...     root_dir=root_dir,
...     nx_k=None,
...     nx_iterations=40,
...     nx_seed=0,
... )


>>> file_name = "sphinx/_static/examples/historiograph_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/examples/historiograph_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.links_.head()    
                                       citing_article                                      cited_article
3                Muganyi T, 2022, FINANCIAL INNOV, V8      Anagnostopoulos I, 2018, J ECON BUS, V100, P7
34  Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V...  Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL,...
24                         Turki M, 2020, HELIYON, V6      Anagnostopoulos I, 2018, J ECON BUS, V100, P7
15         von Solms J, 2021, J BANK REGUL, V22, P152      Anagnostopoulos I, 2018, J ECON BUS, V100, P7
35                      Kurum E, 2020, J FINANC CRIME      Anagnostopoulos I, 2018, J ECON BUS, V100, P7

>>> nnet.articles_.head(10)    
0        Anagnostopoulos I, 2018, J ECON BUS, V100, P7
1    Becker M, 2020, INTELL SYST ACCOUNT FINANCE M,...
2    Butler T, 2018, J RISK MANG FINANCIAL INST, V1...
3    Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL,...
4          Kavassalis P, 2018, J RISK FINANC, V19, P39
5                        Kurum E, 2020, J FINANC CRIME
6                 Muganyi T, 2022, FINANCIAL INNOV, V8
7    Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V...
8                           Turki M, 2020, HELIYON, V6
9            Waye V, 2020, ADELAIDE LAW REV, V40, P363
dtype: object

"""
import networkx as nx
import pandas as pd

# from ...classes import HistoriographResults
# from ...network_lib import (
#     nx_compute_spring_layout,
#     px_add_names_to_fig_nodes,
#     px_create_edge_traces,
#     px_create_network_fig,
#     px_create_node_trace,
# )
# from ...records_lib import read_records


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def historiograph(
    top_n=50,
    root_dir="./",
    # Parameter used for main_path:
    selected_articles=None,
    # Graph params:
    node_size=10,
    n_labels=None,
    color="#7793a5",
    textfont_size=10,
    nx_k=None,
    nx_iterations=50,
    nx_seed=0,
    # Items params:
):
    """Historiograph network."""

    def create_links_database():
        """Creates a database with links between citing and cited articles."""

        records = read_records(root_dir=root_dir, database="main")

        records = records.sort_values(
            ["global_citations", "local_citations", "year"],
            ascending=[False, False, True],
        )

        if selected_articles is None:
            records = records.head(top_n)
        else:
            records = records[records.article.isin(selected_articles)]

        valid_articles = records.article.tolist()

        records["local_references"] = records.local_references.str.split("; ")
        records = records.explode("local_references")
        records["local_references"] = records.local_references.str.strip()
        records = records[records.local_references.isin(valid_articles)]

        # Sanity check: remove the article from its own local references
        for _, row in records.dropna().iterrows():
            if row.article in row.local_references:
                row.local_references.remove(row.article)

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

        # Creates the links of the citation network
        links = records[["citing_article", "cited_article"]]

        return links

    def nx_create_graph_from_links(links):
        """Creates a networkx graph from a list of links."""

        graph = nx.DiGraph()

        for source_node, target_node in zip(
            links.citing_article, links.cited_article
        ):
            graph.add_edges_from(
                [(source_node, target_node)],
                width=1,
                dash="solid",
                color=color,
            )

        for node in graph.nodes():
            graph.nodes[node]["group"] = 0
            graph.nodes[node]["color"] = color
            graph.nodes[node]["textfont_color"] = color
            graph.nodes[node]["textfont_size"] = textfont_size
            graph.nodes[node]["node_size"] = node_size
            graph.nodes[node]["OCC"] = 10

        graph = nx_compute_spring_layout(
            graph, k=nx_k, iterations=nx_iterations, seed=nx_seed
        )

        return graph

    def fig_draw_arrows(fig, graph):
        # pylint: disable=invalid-name
        for edge in graph.edges():
            node_citing_article = edge[0]
            node_cited_article = edge[1]

            citing_x, citing_y = graph.nodes[node_citing_article]["pos"]
            cited_x, cited_y = graph.nodes[node_cited_article]["pos"]

            head_x = (citing_x + cited_x) / 2
            head_y = (citing_y + cited_y) / 2

            ax = head_x - (cited_x - citing_x) / 2 * 0.5
            ay = head_y - (cited_y - citing_y) / 2 * 0.5

            fig.add_annotation(
                axref="x",
                ayref="y",
                x=head_x,
                y=head_y,
                ax=ax,
                ay=ay,
                showarrow=True,
                arrowhead=4,
                arrowsize=2,
                arrowcolor="#7793a5",
                arrowwidth=0.7,
            )

        return fig

    links = create_links_database()
    graph = nx_create_graph_from_links(links)

    node_traces = px_create_node_trace(graph)
    edge_traces = px_create_edge_traces(graph)

    fig = px_create_network_fig(
        edge_traces=edge_traces,
        node_trace=node_traces,
        xaxes_range=None,
        yaxes_range=None,
        show_axes=False,
    )

    fig = fig_draw_arrows(fig, graph)

    fig = px_add_names_to_fig_nodes(
        fig, graph, n_labels=n_labels, is_article=True
    )

    histograph = HistoriographResults()
    histograph.nx_graph_ = graph
    histograph.plot_ = fig
    histograph.links_ = links
    histograph.articles_ = (
        pd.concat([links.citing_article, links.cited_article])
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )

    return histograph
