"""
Word Co-occurrences Plot (ok!)
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_co_occurrentes_plot.html"

>>> from techminer2 import tlab__word_co_occurrentes_plot
>>> tlab__word_co_occurrentes_plot(
...     criterion='words',
...     topic="regtech",
...     topic_min_occ=4,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_co_occurrentes_plot.html" height="1000px" width="100%" frameBorder="0"></iframe>

"""
from ._plots.bar_plot import bar_plot
from ._plots.cleveland_plot import cleveland_plot
from ._plots.column_plot import column_plot
from ._plots.line_plot import line_plot
from ._plots.pie_plot import pie_plot
from .vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list


def tlab__word_co_occurrentes_plot(
    criterion,
    topic,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    plot="bar",
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Word Association"""

    matrix_list = vantagepoint__co_occ_matrix_list(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = matrix_list[
        matrix_list["row"].map(lambda x: " ".join(x.split()[:-1]) == topic)
    ]

    matrix_list = matrix_list[matrix_list["row"] != matrix_list["column"]]

    matrix_list = matrix_list[["column", "OCC"]]

    if topics_length is not None:
        matrix_list = matrix_list.head(topics_length)

    matrix_list = matrix_list.set_index("column")
    matrix_list = matrix_list.sort_values(by="OCC", ascending=False)

    plot_function = {
        "bar": bar_plot,
        "column": column_plot,
        "line": line_plot,
        "pie": pie_plot,
        "cleveland": cleveland_plot,
    }[plot]

    fig = plot_function(
        dataframe=matrix_list,
        metric="OCC",
        title=None,
    )
    fig.update_layout(
        yaxis_title=None,
        margin=dict(l=1, r=1, t=1, b=1),
    )

    return fig
