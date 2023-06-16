# flake8: noqa
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

# pylint: disable=line-too-long
"""


from dataclasses import dataclass

import networkx as nx

from ..._get_network_graph_plot import get_network_graph_plot
from .common import compute_main_path

#
# The function main_path_analysis apply the main path algorithm to the documents
# of the dataset
#


@dataclass(init=False)
class _Results:
    table_ = None
    plot_ = None
    prompts_ = None


def main_path_analysis(
    directory="./",
    nx_k=0.1,
    nx_iterations=10,
    nx_seed=0,
    delta=1.0,
):
    """Main Path Analysis"""

    results = _Results()
    documents_in_main_path = compute_main_path(directory)

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
