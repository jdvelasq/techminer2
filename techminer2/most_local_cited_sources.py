"""
Most Local Cited Sources in References (*)
===============================================================================

Plot the most local cited sources in the references.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_local_cited_sources.png"
>>> most_local_cited_sources(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_local_cited_sources.png
    :width: 700px
    :align: center

"""
import os.path

import pandas as pd

from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .column_indicators import column_indicators


def most_local_cited_sources(
    top_n=10,
    directory="./",
):

    indicators = pd.read_csv(
        os.path.join(directory, "processed", "references.csv"),
        sep=",",
        encoding="utf-8",
    )
    indicators = indicators[["iso_source_name", "local_citations"]]
    indicators = indicators.groupby("iso_source_name").sum()
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    indicators = indicators.head(top_n)
    indicators = indicators.local_citations

    return bibliometrix_scatter_plot(
        x=indicators.values,
        y=indicators.index,
        title="Most local cited sources in references",
        text=indicators.astype(str),
        xlabel="Local citations",
        ylabel="Source title",
    )
