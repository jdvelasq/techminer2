# flake8: noqa
"""
Cross-correlation Map
===============================================================================

Creates an Cross-correlation Map.


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/techminer2plus__cross_correlation_map.html"

>>> import techminer2plus
>>> chart = techminer2plus.system.analyze.cross_correlation_map(
...     rows_and_columns='authors',
...     cross_with='countries',
...     top_n=10,
...     color="#1f77b4", # tab:blue
...     root_dir=root_dir,
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/techminer2plus__cross_correlation_map.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below which contains the auto-correlation values for the authors. High correlation values indicate that the topics tends to appear together in the same document and forms a group. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row               | column            |   CORR |
|---:|:------------------|:------------------|-------:|
|  3 | Arner DW 3:185    | Buckley RP 3:185  |  1     |
|  5 | Barberis JN 2:161 | Buckley RP 3:185  |  0.907 |
|  6 | Arner DW 3:185    | Barberis JN 2:161 |  0.907 |
| 12 | Brennan R 2:014   | Butler T/1 2:041  |  0.886 |
| 16 | Hamdan A 2:018    | Turki M 2:018     |  1     |
| 18 | Butler T/1 2:041  | Lin W 2:017       |  0.283 |
| 21 | Butler T/1 2:041  | Singh C 2:017     |  0.283 |
| 22 | Lin W 2:017       | Singh C 2:017     |  1     |
| 27 | Butler T/1 2:041  | Crane M 2:014     |  0.886 |
| 28 | Brennan R 2:014   | Crane M 2:014     |  1     |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""

from ...classes import CorrMap
from ...network import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix_list,
    nx_set_edge_properties_for_corr_maps,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)
from .cross_correlation_matrix import cross_correlation_matrix
from .list_cells_in_matrix import list_cells_in_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def cross_correlation_map(
    # Matrix params:
    rows_and_columns,
    cross_with,
    method="pearson",
    # Map params:
    n_labels=None,
    color="#8da4b4",
    nx_k=0.1,
    nx_iterations=10,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Correlation map."""

    matrix = cross_correlation_matrix(
        rows_and_columns=rows_and_columns,
        cross_with=cross_with,
        method=method,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_list = list_cells_in_matrix(matrix)

    graph = nx_create_graph_from_matrix_list(
        matrix_list,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )

    for node in graph.nodes():
        graph.nodes[node]["color"] = color

    graph = nx_set_edge_properties_for_corr_maps(graph, color)

    graph = nx_compute_spring_layout(
        graph, nx_k, nx_iterations, nx_random_state
    )

    node_trace = px_create_node_trace(graph)
    # text_trace = network_utils.create_text_trace(graph)
    edge_traces = px_create_edge_traces(graph)

    fig = px_create_network_fig(
        edge_traces,
        node_trace,
        # text_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    fig = px_add_names_to_fig_nodes(fig, graph, n_labels)

    corrmap = CorrMap()
    corrmap.plot_ = fig
    corrmap.table_ = matrix_list.cells_list_
    corrmap.prompt_ = matrix_list.prompt_

    return corrmap
