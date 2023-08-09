# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .manifold_2d_map import manifold_2d_map


def factor_2d_chart(
    #
    # DATA:
    embedding,
    #
    # MAP PARAMS:
    dim_x,
    dim_y,
    #
    # MAP:
    node_color="#465c6b",
    node_size=10,
    textfont_size=8,
    textfont_color="#465c6b",
    xaxes_range=None,
    yaxes_range=None,
):
    return manifold_2d_map(
        node_x=embedding[dim_x],
        node_y=embedding[dim_y],
        node_text=embedding.index.to_list(),
        node_color=node_color,
        node_size=node_size,
        title_x=dim_x,
        title_y=dim_y,
        textfont_size=textfont_size,
        textfont_color=textfont_color,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
