"""
TreeMap
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__treemap.html"

>>> from techminer2 import bibliometrix__treemap
>>> bibliometrix__treemap(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .list_view import list_view
from .treemap_plot import treemap_plot


def bibliometrix__treemap(
    column,
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title=None,
    database="documents",
    metric="OCC",
):
    """Makes a treemap."""

    indicators = list_view(
        column=column,
        metric=metric,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database=database,
    )

    return treemap_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
