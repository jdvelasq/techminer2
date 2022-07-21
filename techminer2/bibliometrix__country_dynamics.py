"""
Country Dynamics
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_dynamics.html"


>>> from techminer2 import bibliometrix__country_dynamics
>>> bibliometrix__country_dynamics(
...     top_n=5, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .bibliometrix__dynamics import bibliometrix__dynamics


def bibliometrix__country_dynamics(
    top_n=5,
    directory="./",
    title="Country Dynamics",
    plot=True,
):
    """Makes a dynamics chat for top sources."""

    return bibliometrix__dynamics(
        column="countries",
        top_n=top_n,
        directory=directory,
        plot=plot,
        title=title,
    )
