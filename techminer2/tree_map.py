"""
Tree Map
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/tree_map.html"

>>> tree_map(
...     'author_keywords',
...     top_n=15, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/tree_map.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from .column_indicators import column_indicators


def tree_map(
    column,
    min_occ=None,
    max_occ=None,
    top_n=None,
    directory="./",
    metric="num_documents",
    title=None,
    database="documents",
):

    indicators = column_indicators(
        column=column,
        directory=directory,
        database=database,
        use_filter=(database == "documents"),
        sep=";",
    )

    indicators = indicators.sort_values(metric, ascending=False)

    if min_occ is not None:
        indicators = indicators[indicators.num_documents >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.num_documents <= max_occ]
    if top_n is not None:
        indicators = indicators.head(top_n)

    indicators = indicators.reset_index()

    fig = px.treemap(
        indicators,
        path=[column],
        values=metric,
        color=metric,
        color_continuous_scale="Greys",
        # names=indicators.index,
        # parents=[""] * len(indicators),
        title=title,
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=1, l=1, r=1, b=1))
    return fig
