"""
Bradford Law's Algorithm

"""

import os
import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.utils.datastore import load_datastore
from src.utils.explode import explode


class Bradford:
    """
    Executes Braddorf analysis of core sources.


    """

    def __init__(self, datastoredir="./"):
        self.datastoredir = datastoredir
        self._core_sources = None
        self._sources = None

    def _compute_core_sources(self):
        """
        Compute the Bradford analysis.
        """
        datastore = load_datastore(datastoredir=self.datastoredir)
        datastore = datastore.assign(num_documents=1)
        datastore = explode(
            datastore[
                [
                    "publication_name",
                    "num_documents",
                    "global_citations",
                    "record_id",
                ]
            ],
            "publication_name",
        )
        sources = datastore.groupby("publication_name", as_index=False).agg(
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
        self._sources = sources
        core_documents = int(len(datastore) / 3)
        core_sources = sources[sources.cum_num_documents <= core_documents]
        self._core_sources = core_sources

        self._core_sources.pop("index")
        self._sources.pop("index")

    @property
    def sources_(self):
        """
        Returns the sources.
        """
        if self._sources is None:
            self._compute_core_sources()
        return self._sources

    @property
    def core_sources_(self):
        """
        Returns the list of core sources
        """
        if self._core_sources is None:
            self._compute_core_sources()
        return self._core_sources

    @property
    def core_sources_names_(self):
        """
        Returns the list of core sources names

        """
        return self._core_sources.publication_name

    def plot(self, max_items=5, cmap="Greys", figsize=(8, 6), fontsize=11):
        """
        Plot the Bradford analysis.

        """
        if self.core_sources_ is None:
            self._compute_core_sources()

        core_sources_names = self.core_sources_names_.head(max_items)
        core_sources_names = core_sources_names.map(
            lambda w: w[0:27] + " [...]" if len(w) > 30 else w
        )

        matplotlib.rc("font", size=fontsize)
        fig, axs = plt.subplots(figsize=figsize)

        cmap = plt.cm.get_cmap(cmap)
        color = cmap(0.6)

        axs.plot(
            list(range(1, len(self.sources_) + 1)),
            self.sources_.num_documents.tolist(),
            linestyle="-",
            linewidth=3,
            color="k",
        )

        axs.fill_between(
            list(range(1, len(self.sources_) + 1)),
            self.sources_.num_documents.tolist(),
            color=color,
            alpha=0.6,
        )

        axs.fill_between(
            [1, len(self.core_sources_) + 1],
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
