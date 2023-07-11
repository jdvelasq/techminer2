# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""
.. _average_citations_per_year_chart:

Average Citations per Year Chart
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/average_citations_per_year_chart.html"
>>> tm2p.average_citations_per_year_chart(
...     root_dir=root_dir,
...     title="Average Citations by Year",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/average_citations_per_year_chart.html" height="600px" width="100%" frameBorder="0"></iframe>
                                  
"""
from .global_indicators_by_year_chart import global_indicators_by_year_chart


def average_citations_per_year_chart(
    title: str = "Average Citations per Year",
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Makes a time line plot for indicators."""

    return global_indicators_by_year_chart(
        indicator_to_plot="mean_global_citations",
        title=title,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
