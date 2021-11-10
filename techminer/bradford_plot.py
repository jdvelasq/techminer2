"""
Bradford Law's plot
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> bradford_plot(directory)

.. image:: images/bradford.png
    :width: 400px
    :align: center

"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from .lib import explode, load_filtered_documents


def _plot(
    num_records_by_source,
    core_sources_names,
    cmap,
    figsize,
    fontsize,
):

    n_sources = len(num_records_by_source)
    n_core_sources = len(core_sources_names)
    num_records_by_source = num_records_by_source.tolist()

    matplotlib.rc("font", size=fontsize)
    fig, ax_ = plt.subplots(figsize=figsize)

    cmap = plt.cm.get_cmap(cmap)
    color = cmap(0.6)

    ax_.plot(
        list(range(1, n_sources + 1)),
        num_records_by_source,
        linestyle="-",
        linewidth=3,
        color="k",
    )

    ax_.fill_between(
        list(range(1, n_sources + 1)),
        num_records_by_source,
        color=color,
        alpha=0.6,
    )

    ax_.fill_between(
        [1, n_core_sources + 1],
        [ax_.get_ylim()[1], ax_.get_ylim()[1]],
        color=color,
        alpha=0.2,
    )

    for side in ["top", "right", "left", "bottom"]:
        ax_.spines[side].set_visible(False)

    ax_.set_xscale("log")

    ax_.grid(axis="y", color="gray", linestyle=":")
    ax_.grid(axis="x", color="gray", linestyle=":")
    ax_.set_ylabel("Num Documents")

    ax_.tick_params(axis="x", labelrotation=90)

    ax_.set_xticks(list(range(1, n_core_sources + 1)))
    ax_.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax_.set_xticklabels(core_sources_names.tolist())

    fig.set_tight_layout(True)
    return fig


def _prepare_table(documents):

    documents = documents.copy()

    documents = documents.assign(num_documents=1)
    exploded_records = explode(
        documents[
            [
                "source_name",
                "num_documents",
                "global_citations",
                "document_id",
                "iso_source_name",
            ]
        ],
        "source_name",
        sep="; ",
    )
    sources = exploded_records.groupby("iso_source_name", as_index=False).agg(
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
    core_documents = int(len(documents) / 3)
    core_sources = sources[sources.cum_num_documents <= core_documents]

    num_documents_by_source = core_sources.num_documents.copy()
    core_sources_names = core_sources.iso_source_name.copy()

    return num_documents_by_source, core_sources_names


def bradford_plot(
    directory,
    max_items=5,
    cmap="Greys",
    figsize=(8, 6),
    fontsize=11,
):
    documents = load_filtered_documents(directory)

    num_records_by_source, core_sources_names = _prepare_table(documents)
    core_sources_names = core_sources_names.head(max_items)
    fig = _plot(
        num_records_by_source=num_records_by_source,
        core_sources_names=core_sources_names,
        cmap=cmap,
        figsize=figsize,
        fontsize=fontsize,
    )
    return fig
