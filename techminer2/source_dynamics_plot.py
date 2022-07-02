"""
Source dynamics plot
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 

>>> from techminer2.bibliometrix import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/source_dynamics_plot.html"

>>> source_dynamics_plot(
...     top_n=10, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/source_dynamics_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .column_dynamics_plot import column_dynamics_plot


def source_dynamics_plot(
    top_n=10,
    directory="./",
):
    """Makes a dynamics chat for top sources."""
    return column_dynamics_plot(
        column="source_abbr",
        top_n=top_n,
        directory=directory,
        title="Source dynamics",
    )
