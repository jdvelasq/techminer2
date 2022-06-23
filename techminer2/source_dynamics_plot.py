"""
Source dynamics plot (ok!)
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 

>>> from techminer2.bibliometrix import *
>>> directory = "data/"
>>> file_name = "sphinx/images/source_dynamics_plot.png"

>>> source_dynamics_plot(
...     top_n=10, 
...     directory=directory,
... ).write_image(file_name)

.. image:: images/source_dynamics_plot.png
    :width: 700px
    :align: center

"""
from .column_dynamics_plot import column_dynamics_plot


def source_dynamics_plot(
    top_n=10,
    directory="./",
):
    return column_dynamics_plot(
        column="iso_source_name",
        top_n=top_n,
        directory=directory,
    )
