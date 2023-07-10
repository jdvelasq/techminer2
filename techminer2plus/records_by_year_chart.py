# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""
.. _records_by_year_chart:

Records by Year Chart
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/records_by_year_chart.html"
>>> tm2p.records_by_year_chart(
...     root_dir=root_dir,
...     title="Annual Scientific Production",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/records_by_year_chart.html" height="600px" width="100%" frameBorder="0"></iframe>
                                  
"""
from .global_indicators_by_year_chart import global_indicators_by_year_chart


def records_by_year_chart(
    title: str = "Annual Scientific Production",
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Makes a time line plot for indicators."""

    return global_indicators_by_year_chart(
        indicator_to_plot="OCC",
        title=title,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
