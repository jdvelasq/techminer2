"""
Word dynamics plot
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 

>>> from techminer2.bibliometrix import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/word_dynamics_plot.html"

>>> word_dynamics_plot(
...     word="author_keywords",
...     top_n=10, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/word_dynamics_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .column_dynamics_plot import column_dynamics_plot


def word_dynamics_plot(
    word,
    top_n=10,
    directory="./",
):
    """Makes a dynamics chat for a word."""
    return column_dynamics_plot(
        column=word,
        top_n=top_n,
        directory=directory,
        title=word.replace("_", " ").title() + " dynamics",
    )
