"""
Topic Dynamics
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/topic_dynamics.png"
>>> topic_dynamics(
...     column='iso_source_name', 
...     top_n=10, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/topic_dynamics.png
    :width: 700px
    :align: center


>>> topic_dynamics('iso_source_name', 5, directory=directory, plot=False).tail(10)
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


def topic_dynamics(column, top_n=10, figsize=(8, 6), directory="./", plot=True):

    column_dynamics = column_indicators_by_year(directory=directory, column=column)
    column_dynamics = column_dynamics.assign(
        pub_year=column_dynamics.index.get_level_values(1)
    )
    column_dynamics.index = column_dynamics.index.get_level_values(0)

    column_dynamics = column_dynamics[["pub_year", "num_documents"]].copy()
    column_dynamics = column_dynamics.pivot(columns="pub_year")
    column_dynamics = column_dynamics.transpose()
    column_dynamics.index = column_dynamics.index.get_level_values(1)

    year_range = list(
        range(column_dynamics.index.min(), column_dynamics.index.max() + 1)
    )
    missing_years = [year for year in year_range if year not in column_dynamics.index]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(column_dynamics.columns))),
        index=missing_years,
        columns=column_dynamics.columns,
    )
    column_dynamics = column_dynamics.append(pdf)
    column_dynamics = column_dynamics.sort_index(axis="index")
    column_dynamics = column_dynamics.fillna(0)

    num_documents = column_dynamics.sum(axis=0)
    num_documents = num_documents.sort_values(ascending=False)

    column_dynamics = column_dynamics[num_documents.index[:top_n]]
    column_dynamics = column_dynamics.cumsum()
    column_dynamics = column_dynamics.astype(int)

    if plot is False:
        return column_dynamics

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    for column in column_dynamics.columns:
        ax.plot(column_dynamics.index, column_dynamics[column], label=column)

    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="major", color="k", length=5)
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
