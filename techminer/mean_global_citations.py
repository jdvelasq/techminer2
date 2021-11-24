"""
Mean global citations
===============================================================================


>>> from techminer import *
>>> mean_global_citations().table_
pub_year
2015     9.222222
2016    21.357143
2017    18.767123
2018    13.643939
2019     6.606195
2020     3.282238
2021     0.783133
2022     0.000000
Name: mean_global_citations, dtype: float64

>>> mean_global_citations().plot()

.. image:: images/mean_global_citations.png
    :width: 400px
    :align: center


"""
import matplotlib.pyplot as plt

from .annual_indicators import annual_indicators


class Mean_global_citations:
    def __init__(self, directory):
        self.directory = directory
        self._run()

    def _run(self):
        self.mean_global_citations = annual_indicators()(
            self.directory
        ).mean_global_citations

    @property
    def table_(self):
        return self.mean_global_citations

    def plot(self, figsize=(6, 6), color="tab:blue"):

        fig = plt.Figure(figsize=figsize)
        ax = fig.subplots()

        ax.plot(
            self.mean_global_citations.index.astype(str),
            self.mean_global_citations.values,
            "o-",
            color=color,
            alpha=0.7,
        )
        ax.set_title("Mean citations per year", fontsize=9)
        ax.set_ylabel("Number of citations")
        ax.set_xlabel("Year")
        ax.set_xticklabels(
            self.mean_global_citations.index.astype(str),
            rotation=90,
            horizontalalignment="center",
            fontsize=7,
        )
        ax.set_yticklabels(
            ax.get_yticks(),
            fontsize=7,
        )

        ax.spines["left"].set_color("gray")
        ax.spines["bottom"].set_color("gray")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(alpha=0.5)
        return fig


def mean_global_citations(directory=None):
    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"
    return Mean_global_citations(directory)
