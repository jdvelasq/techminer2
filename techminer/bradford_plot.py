"""
Bradford Law's Plot
===============================================================================

"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from techminer.utils import explode, load_filtered_documents


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


def _prepare_table(records):

    records = records.copy()

    records = records.assign(num_records=1)
    exploded_records = explode(
        records[
            [
                "publication_name",
                "num_records",
                "global_citations",
                "record_id",
            ]
        ],
        "publication_name",
        sep="; ",
    )
    sources = exploded_records.groupby("publication_name", as_index=False).agg(
        {
            "num_records": np.sum,
            "global_citations": np.sum,
        }
    )
    sources["global_citations"] = sources["global_citations"].map(int)
    sources = sources.sort_values(
        by=["num_records", "global_citations"], ascending=False
    )
    sources = sources.reset_index()
    sources = sources.assign(cum_num_records=sources.num_records.cumsum())
    core_documents = int(len(records) / 3)
    core_sources = sources[sources.cum_num_records <= core_documents]

    num_records_by_source = core_sources.num_records.copy()
    core_sources_names = core_sources.publication_name.copy()

    return num_records_by_source, core_sources_names


def _bradford_plot_from_records(
    records,
    max_items=5,
    cmap="Greys",
    figsize=(8, 6),
    fontsize=11,
):

    num_records_by_source, core_sources_names = _prepare_table(records)
    fig = _plot(
        num_records_by_source=num_records_by_source,
        core_sources_names=core_sources_names,
        cmap=cmap,
        figsize=figsize,
        fontsize=fontsize,
    )
    return fig


def _bradford_plot_from_directory(
    directory,
    max_items,
    cmap,
    figsize,
    fontsize,
):
    return _bradford_plot_from_records(
        records=load_filtered_documents(directory),
        max_items=max_items,
        cmap=cmap,
        figsize=figsize,
        fontsize=fontsize,
    )


def bradford_plot(
    dirpath_or_records,
    max_items=5,
    cmap="Greys",
    figsize=(8, 6),
    fontsize=11,
):
    """
    Plots the Bradford's law core source  distribution.



    """
    if isinstance(dirpath_or_records, str):
        return _bradford_plot_from_directory(
            directory=dirpath_or_records,
            max_items=max_items,
            cmap=cmap,
            figsize=figsize,
            fontsize=fontsize,
        )
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _bradford_plot_from_records(
            records=dirpath_or_records,
            max_items=max_items,
            cmap=cmap,
            figsize=figsize,
            fontsize=fontsize,
        )
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")
