"""
Co-Occurrences Plot
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

    total_occ_topic = matrix_list["row"].iloc[0]
    total_occ_topic = total_occ_topic.split()[-1]
    total_occ_topic = total_occ_topic.split(":")[0]
    total_occ_topic = int(total_occ_topic)

    matrix_list = matrix_list[matrix_list["row"] != matrix_list["column"]]

    # matrix_list["total_OCC"] = matrix_list["row"].map(lambda x: x.split())
    # matrix_list["total_OCC"] = matrix_list["total_OCC"].str[-1]
    # matrix_list["total_OCC"] = matrix_list["total_OCC"].str.split(":")
    # matrix_list["total_OCC"] = matrix_list["total_OCC"].str[-1]
    # matrix_list["total_OCC"] = matrix_list["total_OCC"].astype(float)
    matrix_list = matrix_list.assign(OCC=100 * matrix_list["OCC"] / total_occ_topic)
    matrix_list["OCC"] = matrix_list["OCC"].round(1)

    matrix_list = matrix_list[["column", "OCC"]]

    matrix_list = matrix_list.set_index("column")
    matrix_list = matrix_list.sort_values(by="OCC", ascending=False)

    matrix_list = matrix_list[matrix_list.OCC > 0.0]

    fig = bar_plot(
        dataframe=matrix_list,
        metric="OCC",
        title=f"(%) Co-occurrence with '{topic}'",
    )

    fig.update_layout(
        yaxis_title=None,
    )

    return fig
