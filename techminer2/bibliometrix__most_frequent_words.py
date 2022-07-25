"""
Most Frequent Words
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_words.html"

>>> from techminer2 import bibliometrix__most_frequent_words
>>> bibliometrix__most_frequent_words(
...     column="author_keywords",
...     directory=directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_words.html" height="600px" width="100%" frameBorder="0"></iframe>




"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_frequent_words(
    column="author_keywords",
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Plots the number of documents by country using the specified plot."""

    return vantagepoint__chart(
        criterion=column,
        directory=directory,
        topics_length=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Countries",
        plot=plot,
        database=database,
    )
