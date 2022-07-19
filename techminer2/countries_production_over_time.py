"""
Countries' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/countries_production_over_time.html"


>>> from techminer2 import countries_production_over_time
>>> countries_production_over_time(
...    top_n=10, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/countries_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .production_over_time import production_over_time


def countries_production_over_time(
    top_n=10,
    directory="./",
):

    return production_over_time(
        column="countries",
        top_n=top_n,
        directory=directory,
        title="Countries' Production over Time",
    )
