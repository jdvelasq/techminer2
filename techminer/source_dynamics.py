"""
Source dynamics
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/source_dynamics.png"
>>> source_dynamics(10, directory=directory).savefig(file_name)

.. image:: images/source_dynamics.png
    :width: 700px
    :align: center


>>> source_dynamics(5, directory=directory, plot=False).tail(10)
iso_source_name  SUSTAINABILITY  ...  FRONTIER ARTIF INTELL
2016                          0  ...                      0
2017                          0  ...                      0
2018                          0  ...                      1
2019                          4  ...                      1
2020                         10  ...                      4
2021                         15  ...                      5
<BLANKLINE>
[6 rows x 5 columns]

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoMinorLocator

from .column_indicators_by_year import column_indicators_by_year


def source_dynamics(n_sources=10, figsize=(8, 6), directory="./", plot=True):

    source_dynamics = column_indicators_by_year(
        directory=directory, column="iso_source_name"
    )[["pub_year", "num_documents"]]
    source_dynamics = source_dynamics.pivot(columns="pub_year")
    source_dynamics = source_dynamics.transpose()
    source_dynamics.index = source_dynamics.index.get_level_values(1)

    year_range = list(
        range(source_dynamics.index.min(), source_dynamics.index.max() + 1)
    )
    missing_years = [year for year in year_range if year not in source_dynamics.index]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(source_dynamics.columns))),
        index=missing_years,
        columns=source_dynamics.columns,
    )
    source_dynamics = source_dynamics.append(pdf)
    source_dynamics = source_dynamics.sort_index(axis="index")
    source_dynamics = source_dynamics.fillna(0)

    num_documents = source_dynamics.sum(axis=0)
    num_documents = num_documents.sort_values(ascending=False)

    source_dynamics = source_dynamics[num_documents.index[:n_sources]]
    source_dynamics = source_dynamics.cumsum()
    source_dynamics = source_dynamics.astype(int)

    if plot is False:
        return source_dynamics

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    for column in source_dynamics.columns:
        ax.plot(source_dynamics.index, source_dynamics[column], label=column)

    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="mayor", color="k", length=5)
    ax.tick_params(which="minor", color="k", length=2)

    for side in ["top", "bottom", "right"]:
        ax.spines[side].set_visible(False)

    ax.set_xlabel("Year", fontsize=9)
    ax.set_ylabel("Cum num documents", fontsize=9)
    ax.tick_params(axis="x", labelrotation=90)
    ax.grid(axis="y", color="gray", linestyle=":")
    ax.grid(axis="x", color="gray", linestyle=":")
    ax.legend(fontsize=8)

    fig.set_tight_layout(True)

    return fig
