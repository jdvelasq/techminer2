"""
Most Frequent Institutions
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_institutions.html"

>>> from techminer2 import bibliometrix__most_frequent_institutions
>>> bibliometrix__most_frequent_institutions(
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_institutions.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_frequent_institutions(
    directory="./",
    topics_length=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the number of documents by institutions using the specified plot."""

    return vantagepoint__chart(
        criterion="institutions",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        min_occ=min_occ,
        max_occ=max_occ,
        custom_topics=None,
        title="Most Frequent Institutions",
        plot=plot,
        **filters,
    )
