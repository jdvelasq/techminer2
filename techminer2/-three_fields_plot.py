"""
Three fields plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/three_fields_plot.png"
>>> three_fields_plot(
...     directory=directory,
...     left_column='authors',
...     middle_column='countries',
...     right_column='author_keywords',
...     min_occ_left=2, 
...     min_occ_middle=6,
...     min_occ_right=8,
... ).write_image(file_name)

.. image:: images/three_fields_plot.png
    :width: 700px
    :align: center

"""

import plotly.graph_objects as go

from .occurrence_matrix import occurrence_matrix


def three_fields_plot(
    directory="./",
    left_column="authors",
    middle_column="countries",
    right_column="author_keywords",
    min_occ_left=4,
    min_occ_middle=4,
    min_occ_right=4,
):

    matrix_left, matrix_right = _make_matrices(
        directory=directory,
        left_column=left_column,
        middle_column=middle_column,
        right_column=right_column,
        min_occ_left=min_occ_left,
        min_occ_middle=min_occ_middle,
        min_occ_right=min_occ_right,
    )

    label, source, target, value = _make_links(matrix_left, matrix_right)

    print(label)
    node_x = []
    node_x += [0] * len(matrix_left.index)
    node_x += [1] * len(matrix_left.columns)
    node_x += [2] * len(matrix_right.index)

    print(node_x)

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=label,
                    x=node_x,
                    y=
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value,
                ),
            )
        ]
    )

    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)

    return fig


def _make_links(matrix_left, matrix_right):

    labels = {
        key: index
        for index, key in enumerate(
            matrix_left.index.to_list()
            + matrix_left.columns.to_list()
            + matrix_right.columns.to_list()
        )
    }

    values = dict()

    for row in matrix_left.index:
        for col in matrix_left.columns:
            # if matrix_left.loc[row, col] > 0:
            values[(labels[row], labels[col])] = matrix_left.loc[row, col]

    for row in matrix_right.index:
        for col in matrix_right.columns:
            # if matrix_right.loc[row, col] > 0:
            values[(labels[row], labels[col])] = matrix_right.loc[row, col]

    source = [key[0] for key in values.keys()]
    target = [key[1] for key in values.keys()]
    value = list(values.values())

    return list(labels.keys()), source, target, value


def _make_matrices(
    directory,
    left_column,
    middle_column,
    right_column,
    min_occ_left,
    min_occ_middle,
    min_occ_right,
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

    for col in matrix_left.columns:
        if col not in matrix_right.index:
            matrix_right.loc[col] = 0

    for index in matrix_right.index:
        if index not in matrix_left.columns:
            matrix_left[index] = 0

    matrix_left = matrix_left.sort_index(axis=1, ascending=True)
    matrix_right = matrix_right.sort_index(axis=0, ascending=True)

    return matrix_left, matrix_right
