"""
Annual scientific production
===============================================================================


>>> from techminer import *
>>> annual_scientific_production().table_
pub_year
2015      9
2016     28
2017     73
2018    132
2019    226
2020    411
2021    415
2022      7
Name: num_documents, dtype: int64


>>> annual_scientific_production().plot()

.. image:: images/annual_scientific_production.png
    :width: 400px
    :align: center


"""
import matplotlib.pyplot as plt

from .time_report import time_report


class Annual_scientific_production:
    def __init__(self, directory):
        self.directory = directory
        self._run()

    def _run(self):
        self.annual_scientific_production = time_report(self.directory).num_documents

    @property
    def table_(self):
        return self.annual_scientific_production

    def plot(self, figsize=(6, 6), color="tab:blue"):

        fig = plt.Figure(figsize=figsize)
        ax = fig.subplots()

        ax.plot(
            self.annual_scientific_production.index.astype(str),
            self.annual_scientific_production.values,
            "o-",
            color=color,
            alpha=0.7,
        )
        ax.set_title("Annual scientific production", fontsize=9)
        ax.set_ylabel("Number of publications")
        ax.set_xlabel("Year")
        ax.set_xticklabels(
            self.annual_scientific_production.index.astype(str),
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


def annual_scientific_production(directory=None):
    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"
    return Annual_scientific_production(directory)
