# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .px_utils import px_create_network_chart


def visualize_nx_graph(
    #
    # FUNCTION PARAMS:
    nx_graph,
    #
    # NETWORK PARAMS:
    n_labels=None,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    #
    # Creates the figure
    return px_create_network_chart(
        nx_graph=nx_graph,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
        n_labels=n_labels,
    )

    # @dataclass
    # class Results:
    #     fig_ = fig
    #     nx_graph_ = nx_graph
    #     communities_ = network_communities(nx_graph)

    # return Results()
