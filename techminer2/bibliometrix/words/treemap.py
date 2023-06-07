# flake8: noqa
"""
TreeMap
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__treemap.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.words.treemap(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

# pylint: disable=line-too-long
"""
from ..._plots.treemap_plot import treemap_plot
from ...techminer.indicators.indicators_by_item import indicators_by_item


def treemap(
    field,
    root_dir="./",
    metric="OCC",
    top_n=20,
    title=None,
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Makes a treemap."""

    indicators = indicators_by_item(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = indicators.sort_values(
        by=["OCC", "global_citations", "local_citations"],
        ascending=False,
    )
    indicators = indicators.head(top_n)

    return treemap_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
