from os.path import isfile

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from techminer.utils.explode import explode


def bradford_plot(datastorepath="./", max_items=5, ax=None, cmap="Greys", **kwarg):
    """
    Bradford Law plot.

    """

    if datastorepath[-1] != "/":
        datastorepath = datastorepath + "/"

    datastorefile = datastorepath + "datastore.csv"
    if isfile(datastorefile):
        datastore = pd.read_csv(datastorefile)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(datastorefile))

    if ax is None:
        ax = plt.gca()

    datastore["num_documents"] = 1
    datastore = explode(
        datastore[
            [
                "publication_name",
                "num_documents",
                "global_citations",
                "id",
            ]
        ],
        "publication_name",
    )
    result = datastore.groupby("publication_name", as_index=False).agg(
        {
            "num_documents": np.sum,
            "global_citations": np.sum,
        }
    )
    result["global_citations"] = result["global_citations"].map(lambda w: int(w))
    result = result.sort_values(
        by=["num_documents", "global_citations"], ascending=False
    )
    result = result.reset_index()
    result["cum_num_documents"] = result.num_documents.cumsum()

    cmap = plt.cm.get_cmap(cmap)
    color = cmap(0.6)

    out = ax.plot(
        list(range(1, len(result) + 1)),
        result.num_documents.tolist(),
        linestyle="-",
        linewidth=3,
        color="k",
    )
    ax.fill_between(
        list(range(1, len(result) + 1)),
        result.num_documents.tolist(),
        color=color,
        alpha=0.6,
    )

    ##
    ## Compute core sources
    ##
    core_documents = int(len(datastore) / 3)
    core_sources = result[
        result.cum_num_documents <= core_documents
    ].publication_name.head(max_items)
    core_sources = core_sources.map(lambda w: w[0:27] + " [...]" if len(w) > 30 else w)

    ax.fill_between(
        [1, len(core_sources) + 1],
        [ax.get_ylim()[1], ax.get_ylim()[1]],
        color=color,
        alpha=0.2,
    )

    for x in ["top", "right", "left", "bottom"]:
        ax.spines[x].set_visible(False)

    ax.set_xscale("log")

    ax.grid(axis="y", color="gray", linestyle=":")
    ax.grid(axis="x", color="gray", linestyle=":")
    ax.set_ylabel("Num Documnets")

    ax.tick_params(axis="x", labelrotation=90)

    ax.set_xticks(list(range(1, len(core_sources) + 1)))
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.set_xticklabels(core_sources.tolist())

    return out
