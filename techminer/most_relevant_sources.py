"""
Most relevant sources
===============================================================================


>>> from techminer import *
>>> most_relevant_sources().table_
iso_source_name
ACM INT CONF PROC SER       25
SUSTAINABILITY              25
ADV INTELL SYS COMPUT       22
LECT NOTES COMPUT SCI       18
LECT NOTES NETWORKS SYST    16
Name: num_documents, dtype: int64


>>> most_relevant_sources().plot()

.. image:: images/most_relevant_sources.png
    :width: 500px
    :align: center


"""
import matplotlib.pyplot as plt

from .column_indicators import column_indicators


class Most_relevant_sources:
    def __init__(self, directory):
        self.directory = directory
        self._run()

    def _run(self):
        self.most_relevant_sources = terms_report(
            self.directory, column="iso_source_name"
        ).num_documents

    @property
    def table_(self):
        return self.most_relevant_sources

    def plot(self, top_n=20, figsize=(6, 6), color="tab:blue"):

        fig = plt.Figure(figsize=figsize)
        ax = fig.subplots()

        sources = self.most_relevant_sources.head(top_n)

        ax.barh(
            sources.index,
            sources.values,
            color=color,
            alpha=0.7,
        )
        ax.set_title("Most relevant sources", fontsize=9)
        ax.set_ylabel("Source")
        ax.set_xlabel("Num Documents")
        ax.set_yticklabels(
            sources.index,
            fontsize=7,
        )
        ax.invert_yaxis()

        ax.spines["left"].set_color("gray")
        ax.spines["bottom"].set_color("gray")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(alpha=0.5)
        return fig


def most_relevant_sources(directory=None):
    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"
    return Most_relevant_sources(directory)
