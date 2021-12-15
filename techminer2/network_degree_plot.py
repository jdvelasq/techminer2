"""
Network Degree Plot
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_network_degree_plot.png"
>>> coc_matrix = co_occurrence_matrix(column='author_keywords', min_occ=7,directory=directory)
>>> network = co_occurrence_network(coc_matrix)
>>> network_degree_plot(network).savefig(file_name)

.. image:: images/co_occurrence_network_degree_plot.png
    :width: 700px
    :align: center


"""


import matplotlib.pyplot as plt


def network_degree_plot(
    network,
    figsize=(6, 6),
):
    G = network["G"]

    degree = [val for (_, val) in G.degree()]
    degree = sorted(degree, reverse=True)

    fig = plt.figure(figsize=figsize)
    ax = fig.subplots()

    ax.plot(degree, ".-k")
    ax.set_xlabel("Node")
    ax.set_ylabel("Degree")

    ax.set_yticklabels(
        ax.get_yticks(),
        fontsize=7,
        color="dimgray",
    )

    for x in ["top", "right"]:
        ax.spines[x].set_visible(False)

    ax.spines["left"].set_color("dimgray")
    ax.spines["bottom"].set_color("dimgray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.5)

    fig.set_tight_layout(True)

    return fig
