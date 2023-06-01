"""
Three Fields Plot
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__three_fields_plot.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.overview.three_fields_plot(
...     directory=directory,
...     left_criterion='authors',
...     middle_criterion='countries',
...     right_criterion='author_keywords',
...     topics_length_left=2,
...     topics_length_right=8,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__three_fields_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go

from ...vantagepoint.analyze.co_occ_matrix import co_occ_matrix


def three_fields_plot(
    left_criterion,
    middle_criterion,
    right_criterion,
    topics_length_left,
    topics_length_right,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Sankey plot"""

    matrix_left = co_occ_matrix(
        columns=middle_criterion,
        rows=left_criterion,
        col_top_n=topics_length_left,
        col_gc_range=topic_min_citations,
        root_dir=directory,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    ).matrix_

    matrix_right = co_occ_matrix(
        columns=right_criterion,
        rows=middle_criterion,
        col_top_n=topics_length_right,
        col_gc_range=topic_min_citations,
        root_dir=directory,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
    ).matrix_

    return _make_sankey_plot(matrix_left, matrix_right)


def _make_sankey_plot(matrix_left, matrix_right):
    left_labels = matrix_left.index.to_list()
    middle_labels = list(
        set(matrix_left.columns.to_list() + matrix_right.index.to_list())
    )
    right_labels = matrix_right.columns.to_list()

    labels = left_labels + middle_labels + right_labels
    labels = {key: pos for pos, key in enumerate(labels)}

    connections_left = {
        (labels[row], labels[col]): matrix_left.loc[row, col]
        for row in matrix_left.index
        for col in matrix_left.columns
        if matrix_left.loc[row, col] != 0
    }

    connections_right = {
        (labels[row], labels[col]): matrix_right.loc[row, col]
        for row in matrix_right.index
        for col in matrix_right.columns
        if matrix_right.loc[row, col] != 0
    }

    connections = {**connections_left, **connections_right}

    fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node={
                "label": [key for key in labels.keys()],
                "x": [0] * len(left_labels)
                + [0.5] * len(middle_labels)
                + [1] * len(right_labels),
                "y": [0] * len(left_labels)
                + [0.01] * len(middle_labels)
                + [0.02] * len(right_labels),
                "pad": 10,
                "color": "#333",
            },
            link={
                "source": [key[0] for key in connections.keys()],
                "target": [key[1] for key in connections.keys()],
                "value": list(connections.values()),
            },
        )
    )

    fig.update_layout(
        hovermode="x",
        font={"size": 10, "color": "black"},
    )

    return fig
