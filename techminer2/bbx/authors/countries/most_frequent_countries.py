"""
Most Frequent Countries
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_countries.html"


>>> from techminer2.bbx.authors.countries import most_frequent_countries
>>> most_frequent_countries(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/most_frequent_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ....vp.report.chart import chart


def most_frequent_countries(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Plots the number of documents by country using the specified plot."""

    return chart(
        column="countries",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Countries",
        plot=plot,
        database=database,
    )
