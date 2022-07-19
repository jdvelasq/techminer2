"""
Word Dynamics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/word_dynamics.html"

>>> from techminer2 import word_dynamics
>>> word_dynamics(
...     column="author_keywords",
...     top_n=5,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/word_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...dynamics import dynamics


def word_dynamics(
    column="author_keywords",
    top_n=5,
    directory="./",
    title="Word Dynamics",
    plot=True,
):
    """Makes a dynamics chat for top sources."""

    return dynamics(
        column=column,
        top_n=top_n,
        directory=directory,
        plot=plot,
        title=title,
    )
