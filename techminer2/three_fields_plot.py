"""
Three fields plot (TODO)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/three_fields_plot.html"

>>> three_fields_plot(
...     directory=directory,
...     left_column='authors',
...     middle_column='countries',
...     right_column='author_keywords',
...     min_occ_left=2, 
...     min_occ_middle=6,
...     min_occ_right=8,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/three_fields_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""


import plotly.graph_objects as go

from .occurrence_matrix import occurrence_matrix


def three_fields_plot(
    left_column,
    middle_column,
    right_column,
    min_occ_left=1,
    min_occ_middle=1,
    min_occ_right=1,
    directory="./",
):
    """Sankey plot"""

    matrix_left, matrix_right = _compute_matrixes(
        left_column=left_column,
        middle_column=middle_column,
        right_column=right_column,
        min_occ_left=min_occ_left,
        min_occ_middle=min_occ_middle,
        min_occ_right=min_occ_right,
        directory=directory,
    )

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
                "color": "dimgray",
            },
            link={
                "source": [key[0] for key in connections.keys()],
                "target": [key[1] for key in connections.keys()],
                "value": [value for value in connections.values()],
                "color": "lightgray",
            },
        )
    )

    fig.update_layout(
        hovermode="x",
        title="Three field plot",
        font=dict(size=10, color="black"),
    )

    return fig


def _compute_matrixes(
    left_column,
    middle_column,
    right_column,
    min_occ_left,
    min_occ_middle,
    min_occ_right=1,
    directory="./",
):

    matrix_left = occurrence_matrix(
        column=middle_column,
        by=left_column,
        min_occ=min_occ_middle,
        min_occ_by=min_occ_left,
        directory=directory,
    )

    matrix_right = occurrence_matrix(
        column=right_column,
        by=middle_column,
        min_occ=min_occ_right,
        min_occ_by=min_occ_middle,
        directory=directory,
    )

    matrix_left.columns = matrix_left.columns.get_level_values(0)
    matrix_right.columns = matrix_right.columns.get_level_values(0)
    matrix_left.index = matrix_left.index.get_level_values(0)
    matrix_right.index = matrix_right.index.get_level_values(0)

    matrix_left = matrix_left.sort_index(axis=1, ascending=True)
    matrix_right = matrix_right.sort_index(axis=0, ascending=True)

    return matrix_left, matrix_right
