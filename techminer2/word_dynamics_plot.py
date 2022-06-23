"""
Word dynamics plot (TODO)
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 

>>> from techminer2.bibliometrix import *
>>> directory = "data/"
>>> file_name = "sphinx/images/word_dynamics_plot.png"

>>> word_dynamics_plot(
...     column="author_keywords",
...     top_n=10, 
...     directory=directory,
... ).write_image(file_name)

.. image:: images/word_dynamics_plot.png
    :width: 700px
    :align: center

"""
from .column_dynamics_plot import column_dynamics_plot


def word_dynamics_plot(
    column="author_keywords",
    top_n=10,
    directory="./",
):
    return column_dynamics_plot(
        column=column,
        top_n=top_n,
        directory=directory,
    )
