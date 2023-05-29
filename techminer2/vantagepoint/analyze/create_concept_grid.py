"""
Create concept grid
===============================================================================



Example:
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=2,
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.cluster_criterion(
...    occ_matrix,
...    community_clustering='louvain',
... )
>>> vantagepoint.analyze.create_concept_grid(graph)



"""

import pandas as pd


def create_concept_grid(graph):
    """Gets communities from a networkx graph as a dataframe."""

    def extract_communities(graph):
        """Gets communities from a networkx graph as a dictionary."""

        communities = {}

        for node, data in graph.nodes(data=True):
            text = f"CL_{data['group'] :02d}"
            if text not in communities:
                communities[text] = []
            communities[text].append(node)

        return communities

    def sort_community_members(communities):
        """Sorts community members in a dictionary."""

        for key, items in communities.items():
            pdf = pd.DataFrame({"members": items})
            pdf = pdf.assign(
                OCC=pdf.members.map(lambda x: x.split()[-1].split(":")[0])
            )
            pdf = pdf.assign(
                gc=pdf.members.map(lambda x: x.split()[-1].split(":")[1])
            )
            pdf = pdf.sort_values(
                by=["OCC", "gc", "members"], ascending=[False, False, True]
            )
            communities[key] = pdf.members.tolist()

        return communities

    #
    # main:
    #
    communities = extract_communities(graph)
    communities = sort_community_members(communities)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
