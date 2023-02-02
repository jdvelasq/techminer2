"""Networkx graph communities"""

import pandas as pd


def get_network_graph_communities(graph):
    """Extracts communities from a networkx graph"""

    members = {}
    for node, data in graph.nodes(data=True):
        text = f"CL_{data['group'] :02d}"
        if text not in members:
            members[text] = []
        members[text].append(node)

    for key, items in members.items():
        pdf = pd.DataFrame({"members": items})
        pdf = pdf.assign(OCC=pdf.members.map(lambda x: x.split()[-1].split(":")[0]))
        pdf = pdf.assign(gc=pdf.members.map(lambda x: x.split()[-1].split(":")[1]))
        pdf = pdf.sort_values(
            by=["OCC", "gc", "members"], ascending=[False, False, True]
        )
        members[key] = pdf.members.tolist()

    df = pd.DataFrame.from_dict(members, orient="index").T
    df = df.fillna("")
    df = df.sort_index(axis=1)

    return df
