"""
Word Associations Co-occurrences Plot
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_associations_co_occurrences_plot.html"

>>> from techminer2 import tlab__word_associations_co_occurrences_plot
>>> tlab__word_associations_co_occurrences_plot(
...     criterion='words',
...     topic="regtech",
...     topics_length=10,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_associations_co_occurrences_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ._plots.bar_plot import bar_plot
from .vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list


def tlab__word_associations_co_occurrences_plot(
    criterion,
    topic,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
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
    matrix_list["total_OCC"] = matrix_list["row"].map(lambda x: x.split())
    matrix_list["total_OCC"] = matrix_list["total_OCC"].str[-1]
    matrix_list["total_OCC"] = matrix_list["total_OCC"].str.split(":")
    matrix_list["total_OCC"] = matrix_list["total_OCC"].str[-1]
    matrix_list["total_OCC"] = matrix_list["total_OCC"].astype(int)
    matrix_list = matrix_list.assign(OCC=matrix_list["OCC"] / matrix_list["total_OCC"])
    matrix_list["OCC"] = matrix_list["OCC"].round(2)

    matrix_list = matrix_list[["column", "OCC"]]

    if topics_length is not None:
        matrix_list = matrix_list.head(topics_length)

    matrix_list = matrix_list.set_index("column")
    matrix_list = matrix_list.sort_values(by="OCC", ascending=False)

    # matrix_list = matrix_list.rename(columns={"OCC": "% OCC"})

    fig = bar_plot(
        dataframe=matrix_list,
        metric="OCC",
        title="(%) Co-occurrence with '{topic}'",
    )
    fig.update_layout(
        yaxis_title=None,
        margin=dict(l=1, r=1, t=1, b=1),
    )

    return fig
