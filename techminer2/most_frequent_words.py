"""
Most Frequent Words
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_frequent_words.html"

>>> most_frequent_words(
...     column="author_keywords",
...     directory=directory,
...     top_n=20,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_words.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cleveland_chart import cleveland_chart


def most_frequent_words(
    column="author_keywords",
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
):
    """Plot the most frequent words."""

    return cleveland_chart(
        column=column,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        metric="num_documents",
        title="Most frequent words",
    )
