# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Treemap
===============================================================================


"""
import plotly.express as px
import plotly.graph_objs as go

CLUSTER_COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


def factor_treemap(
    #
    # FACTOR:
    communities,
    #
    # CHART PARAMS:
    title=None,
):
    """Creates a treemap.

    :meta private:
    """

    node_occ = []
    node_color = []
    node_text = []
    parents = []

    #
    # Converts communities dataframe in dictionary
    clusters = {}
    for key, names in communities.items():
        for name in names:
            if name.strip() != "":
                if key in clusters:
                    clusters[key] += [name.strip()]
                else:
                    clusters[key] = [name.strip()]
    #
    # Treemap
    cluster_occ = {key: 0 for key in clusters}
    for i_key, (key, names) in enumerate(clusters.items()):
        for name in names:
            #
            # Extracs occurrences from node names. Example: 'regtech 10:100' -> 10
            occ = name.split(" ")[-1]
            occ = occ.split(":")[0]
            occ = float(occ)
            node_occ.append(occ)

            cluster_occ[key] += occ

            #
            # Uses the same color of clusters
            node_color.append(CLUSTER_COLORS[i_key])

            #
            # Sets text to node names without metrics
            node_name = name
            node_name = node_name.split(" ")[:-1]
            node_name = " ".join(node_name)

            node_text.append(node_name)
            parents.append(key)

    node_occ = [cluster_occ[key] * 0 for key in clusters] + node_occ
    node_color = ["lightgrey"] * len(clusters) + node_color
    node_text = list(clusters.keys()) + node_text
    parents = [""] * len(clusters) + parents

    fig = go.Figure()
    fig.add_trace(
        go.Treemap(
            labels=node_text,
            parents=parents,
            values=node_occ,
            textinfo="label+value+percent entry",
            opacity=0.9,
        )
    )
    fig.update_traces(marker={"cornerradius": 5})
    fig.update_layout(
        showlegend=False,
        margin={"t": 30, "l": 0, "r": 0, "b": 0},
        title=title if title is not None else "",
    )

    #
    # Change the colors of the treemap white
    fig.update_traces(
        marker_colors=node_color,
    )

    #
    # Change the font size of the labels
    fig.update_traces(textfont_size=12)

    return fig
