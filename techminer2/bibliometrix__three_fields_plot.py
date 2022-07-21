"""
Three Fields Plot
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__three_fields_plot.html"

>>> from techminer2 import bibliometrix__three_fields_plot
>>> bibliometrix__three_fields_plot(
...     directory=directory,
...     left_column='authors',
...     middle_column='countries',
...     right_column='author_keywords',
...     top_n_left=2, 
...     top_n_right=8,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__three_fields_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go

from .co_occ_matrix import co_occ_matrix


def bibliometrix__three_fields_plot(
    left_column,
    middle_column,
    right_column,
    top_n_left,
    top_n_right,
    directory="./",
):
    """Sankey plot"""

    matrix_left = co_occ_matrix(
        column=middle_column,
        row=left_column,
        top_n=top_n_left,
        directory=directory,
    )

    matrix_right = co_occ_matrix(
        column=right_column,
        row=middle_column,
        top_n=top_n_right,
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
        font=dict(size=10, color="black"),
    )

    return fig
