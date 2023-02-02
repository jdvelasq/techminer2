"""
TreeMap
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__treemap.html"

>>> from techminer2 import bibliometrix__treemap
>>> bibliometrix__treemap(
...    criterion='author_keywords',
...    topics_length=20,
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...._plots.treemap_plot import treemap_plot
from ....techminer.indicators.indicators_by_topic import indicators_by_topic


def bibliometrix__treemap(
    criterion,
    directory="./",
    metric="OCC",
    topics_length=20,
    title=None,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a treemap."""

    indicators = indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = indicators.sort_values(
        by=["OCC", "global_citations", "local_citations"],
        ascending=False,
    )
    indicators = indicators.head(topics_length)

    return treemap_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
