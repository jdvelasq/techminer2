"""
Most Frequent Words
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_words.html"

>>> from techminer2 import most_frequent_words
>>> most_frequent_words(
...     column="author_keywords",
...     directory=directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/most_frequent_words.html" height="600px" width="100%" frameBorder="0"></iframe>




"""
from ....chart import chart


def most_frequent_words(
    column="author_keywords",
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Plots the number of documents by country using the specified plot."""

    return chart(
        column=column,
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Countries",
        plot=plot,
        database=database,
    )
