"""
Bradford Law's Algorithm

"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from techminer.data.records import load_records
from techminer.utils.explode import explode


def bradford(
    directory_or_records, max_items=5, cmap="Greys", figsize=(8, 6), fontsize=11
):
    """
    Plots the Bradford's law core source  distribution.



    """
    if isinstance(directory_or_records, str):
        records = load_records(directory_or_records)
    else:
        records = directory_or_records.copy()

    records = records.assign(num_documents=1)
    records = explode(
        records[
            [
                "publication_name",
                "num_documents",
                "global_citations",
                "record_id",
            ]
        ],
        "publication_name",
    )
    sources = records.groupby("publication_name", as_index=False).agg(
        {
            "num_documents": np.sum,
            "global_citations": np.sum,
        }
    )
    sources["global_citations"] = sources["global_citations"].map(int)
    sources = sources.sort_values(
        by=["num_documents", "global_citations"], ascending=False
    )
    sources = sources.reset_index()
    sources = sources.assign(cum_num_documents=sources.num_documents.cumsum())

    core_documents = int(len(records) / 3)

    core_sources = sources[sources.cum_num_documents <= core_documents]

    core_sources.drop(columns="index", inplace=True)
    sources.drop(columns="index", inplace=True)

    #
    # Plot
    #
    core_sources_names = core_sources.publication_name.copy()

    core_sources_names = core_sources_names.head(max_items)
    core_sources_names = core_sources_names.map(
        lambda w: w[0:27] + " [...]" if len(w) > 30 else w
    )

    matplotlib.rc("font", size=fontsize)
    fig, axs = plt.subplots(figsize=figsize)

    cmap = plt.cm.get_cmap(cmap)
    color = cmap(0.6)

    axs.plot(
        list(range(1, len(sources) + 1)),
        sources.num_documents.tolist(),
        linestyle="-",
        linewidth=3,
        color="k",
    )

    axs.fill_between(
        list(range(1, len(sources) + 1)),
        sources.num_documents.tolist(),
        color=color,
        alpha=0.6,
    )

    axs.fill_between(
        [1, len(core_sources) + 1],
        [axs.get_ylim()[1], axs.get_ylim()[1]],
        color=color,
        alpha=0.2,
    )

    for side in ["top", "right", "left", "bottom"]:
        axs.spines[side].set_visible(False)

    axs.set_xscale("log")

    axs.grid(axis="y", color="gray", linestyle=":")
    axs.grid(axis="x", color="gray", linestyle=":")
    axs.set_ylabel("Num Documents")

    axs.tick_params(axis="x", labelrotation=90)

    axs.set_xticks(list(range(1, len(core_sources_names) + 1)))
    axs.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axs.set_xticklabels(core_sources_names.tolist())

    fig.set_tight_layout(True)
    return fig
