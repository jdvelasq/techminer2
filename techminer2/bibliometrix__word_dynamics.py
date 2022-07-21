"""
Word Dynamics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__word_dynamics.html"

>>> from techminer2 import bibliometrix__word_dynamics
>>> bibliometrix__word_dynamics(
...     column="author_keywords",
...     top_n=5,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__word_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bibliometrix__dynamics import bibliometrix__dynamics


def bibliometrix__word_dynamics(
    column="author_keywords",
    top_n=5,
    directory="./",
    title="Word Dynamics",
    plot=True,
):
    """Makes a dynamics chat for top sources."""

    return bibliometrix__dynamics(
        column=column,
        top_n=top_n,
        directory=directory,
        plot=plot,
        title=title,
    )
