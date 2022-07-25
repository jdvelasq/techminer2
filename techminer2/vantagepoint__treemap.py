"""
Treemap
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__treemap.html"

>>> from techminer2 import vantagepoint__treemap
>>> vantagepoint__treemap(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def vantagepoint__treemap(
    column,
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title=None,
    database="documents",
):
    """Treemap."""

    return vantagepoint__chart(
        criterion=column,
        directory=directory,
        topics_length=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot="treemap",
        database=database,
    )
