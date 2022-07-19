"""
Source Dynamics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/source_dynamics.html"

>>> from techminer2 import source_dynamics
>>> source_dynamics(
...     top_n=10, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/source_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .dynamics import dynamics


def source_dynamics(
    top_n=10,
    directory="./",
    title="Source Dynamics",
    plot=True,
):
    """Makes a dynamics chat for top sources."""

    return dynamics(
        column="source_abbr",
        top_n=top_n,
        directory=directory,
        plot=plot,
        title=title,
    )
