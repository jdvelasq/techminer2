"""
Country Dynamics
===============================================================================

See :doc:`column indicators by year <column_indicators_by_year>` to obtain a 
`pandas.Dataframe` with the data. 


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/country_dynamics.html"


>>> from techminer2.bbx.authors.countries import country_dynamics
>>> country_dynamics(
...     top_n=5, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/country_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from ...dynamics import dynamics


def country_dynamics(
    top_n=5,
    directory="./",
    title="Country Dynamics",
    plot=True,
):
    """Makes a dynamics chat for top sources."""

    return dynamics(
        column="countries",
        top_n=top_n,
        directory=directory,
        plot=plot,
        title=title,
    )
