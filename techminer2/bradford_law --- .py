"""
Bradford's Law
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/bradford.png"
>>> bradford_law(directory=directory).savefig(file_name)

.. image:: images/bradford.png
    :width: 700px
    :align: center


>>> bradford_law(directory=directory, plot=False).head(5)
                 iso_source_name  num_documents  ...  cum_num_documents    zone
0                 SUSTAINABILITY             15  ...                 15  zone 1
1                FINANCIAL INNOV             11  ...                 26  zone 1
2  J OPEN INNOV: TECHNOL MARK CO              8  ...                 34  zone 1
3                   E3S WEB CONF              7  ...                 41  zone 1
4          FRONTIER ARTIF INTELL              5  ...                 46  zone 1
<BLANKLINE>
[5 rows x 5 columns]


"""
import numpy as np
import plotly.express as px

from ._read_records import read_filtered_records


def bradford_law(
    top_n=10,
    directory="./",
):

    # -----------------------------------------------------------------------------------
    documents = read_filtered_records(directory)
    documents = documents.copy()
    documents = documents.assign(num_documents=1)
    sources = documents.groupby("iso_source_name", as_index=False).agg(
        {
            "num_documents": np.sum,
            "global_citations": np.sum,
        }
    )
    sources["global_citations"] = sources["global_citations"].map(int)
    sources = sources.sort_values(
        by=["num_documents", "global_citations", "iso_source_name"],
        ascending=[False, False, True],
    )
    sources = sources.reset_index(drop=True)
    sources = sources.assign(cum_num_documents=sources.num_documents.cumsum())
    num_documents_per_zone = int(len(documents) / 3)
    sources["zone"] = np.where(
        sources.cum_num_documents <= num_documents_per_zone,
        "zone 1",
        np.where(
            sources.cum_num_documents <= 2 * num_documents_per_zone, "zone 2", "zone 3"
        ),
    )

    core_sources = sources[sources.cum_num_documents <= num_documents_per_zone]

    # -----------------------------------------------------------------------------------

    n_sources = len(sources)
    n_core_sources = len(core_sources)
    num_records_by_source = sources.num_documents.tolist()

    matplotlib.rc("font")
    fig, ax_ = plt.subplots(figsize=figsize)

    cmap = plt.cm.get_cmap(cmap)
    color = cmap(0.6)

    ax_.plot(
        list(range(1, n_sources + 1)),
        num_records_by_source,
        linestyle="-",
        linewidth=2,
        color="k",
    )

    ax_.fill_between(
        list(range(1, n_sources + 1)),
        num_records_by_source,
        color=color,
        alpha=0.6,
    )

    ax_.axvspan(
        1,
        n_core_sources + 1,
        color=color,
        alpha=0.2,
    )

    for side in ["top", "right", "left", "bottom"]:
        ax_.spines[side].set_visible(False)

    ax_.set_xscale("log")

    ax_.grid(axis="y", color="lightgray", linestyle=":")
    ax_.grid(axis="x", color="lightgray", linestyle=":")
    ax_.set_ylabel("Num Documents", fontsize=7)

    ax_.tick_params(axis="x", labelrotation=90)

    ax_.set_xticks(list(range(1, top_n + 1)))
    # ax_.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax_.set_xticklabels(sources.iso_source_name.head(top_n).tolist(), fontsize=7)

    ax_.set_xlim(1, n_sources)
    ax_.set_ylim(0, max(num_records_by_source))

    for item in ax_.get_yticklabels():
        item.set_fontsize(7)

    ax_.set_title("Bradford's Law", fontsize=10, loc="left", color="k")
    fig.set_tight_layout(True)
    return fig
