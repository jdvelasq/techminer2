"""
Countries' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__countries_production_over_time.html"


>>> from techminer2 import bibliometrix__countries_production_over_time
>>> bibliometrix__countries_production_over_time(
...    top_n=10, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__countries_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bibliometrix__production_over_time import bibliometrix__production_over_time


def bibliometrix__countries_production_over_time(
    top_n=10,
    directory="./",
):
    """Countries' Production over Time."""

    return bibliometrix__production_over_time(
        column="countries",
        top_n=top_n,
        directory=directory,
        title="Countries' Production over Time",
    )
