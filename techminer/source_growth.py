"""
Source growth
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/source_growth.png"
>>> source_growth(10, directory=directory).savefig(file_name)

.. image:: images/source_growth.png
    :width: 700px
    :align: center


>>> source_growth(5, directory=directory, plot=False).tail(10)
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


def source_growth(n_sources=10, figsize=(8, 6), directory="./", plot=True):

    source_growth = column_indicators_by_year(
        directory=directory, column="iso_source_name"
    )[["pub_year", "num_documents"]]
    source_growth = source_growth.pivot(columns="pub_year")
    source_growth = source_growth.transpose()
    source_growth.index = source_growth.index.get_level_values(1)

    year_range = list(range(source_growth.index.min(), source_growth.index.max() + 1))
    missing_years = [year for year in year_range if year not in source_growth.index]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(source_growth.columns))),
        index=missing_years,
        columns=source_growth.columns,
    )
    source_growth = source_growth.append(pdf)
    source_growth = source_growth.sort_index(axis="index")
    source_growth = source_growth.fillna(0)

    num_documents = source_growth.sum(axis=0)
    num_documents = num_documents.sort_values(ascending=False)

    source_growth = source_growth[num_documents.index[:n_sources]]
    source_growth = source_growth.cumsum()
    source_growth = source_growth.astype(int)

    if plot is False:
        return source_growth

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    for column in source_growth.columns:
        ax.plot(source_growth.index, source_growth[column], label=column)

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
