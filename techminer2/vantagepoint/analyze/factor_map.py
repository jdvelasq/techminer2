# flake8: noqa
"""
Factor Map
===============================================================================

Creates a Factor Map.

* **Note:** The number of factors affects the number of columns in the concept grid.

Example:
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> c_grid = vantagepoint.analyze.concept_grid(
...    field='authors',
...    occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> print(c_grid.table_.to_markdown())
|    | CL_00             | CL_01           | CL_02          | CL_03         | CL_04              | CL_05            |
|---:|:------------------|:----------------|:---------------|:--------------|:-------------------|:-----------------|
|  0 | Arner DW 3:185    | Brennan R 2:014 | Hamdan A 2:018 | Lin W 2:017   | Grassi L 2:002     | Butler T/1 2:041 |
|  1 | Buckley RP 3:185  | Crane M 2:014   | Turki M 2:018  | Singh C 2:017 | Lanfranchi D 2:002 | Arman AA 2:000   |
|  2 | Barberis JN 2:161 | Ryan P 2:014    | Sarea A 2:012  |               |                    |                  |


>>> file_name = "sphinx/_static/vantagepoint__factor_map.html"
>>> chart = vantagepoint.analyze.factor_map(
...    field='authors',
...    occ_range=(2, None),
...    nx_k=0.1,
...    nx_iterations=10,
...    root_dir=root_dir,
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint__factor_map.html" height="600px" width="100%" frameBorder="0"></iframe>



# pylint: disable=line-too-long
"""

import pandas as pd

from ... import network_utils
from ...classes import FactorMap
from .co_occurrence_matrix import co_occurrence_matrix
from .concept_grid import concept_grid
from .list_cells_in_matrix import list_cells_in_matrix


def factor_map(
    # Specific params:
    field,
    threshold=0.5,
    pca=None,
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
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Create a Factor Map from the clusters of a Factor Matrix."""

    concept_grid_ = concept_grid(
        field=field,
        threshold=threshold,
        pca=pca,
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

    coc_matrix = co_occurrence_matrix(
        columns=field,
        # Columns item filters:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = coc_matrix.matrix_.copy()
    clusters = concept_grid_.table_.copy()

    for col in matrix.columns:
        for row in matrix.index:
            if col == row:
                continue

            found = False
            for factor_col in clusters.columns:
                if (
                    col in clusters[factor_col].values
                    and row in clusters[factor_col].values
                ):
                    found = True
                    break

            if found is False:
                matrix.loc[row, col] = 0
            else:
                if matrix.loc[row, col] == 0:
                    matrix.loc[row, col] = 1

    coc_matrix.matrix_ = matrix.copy()

    matrix_list = list_cells_in_matrix(coc_matrix)

    graph = network_utils.create_graph(
        matrix_list,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )

    for node in graph.nodes():
        graph.nodes[node]["color"] = color

    ## graph = network_utils.set_edge_properties_for_corr_maps(graph, color)

    graph = network_utils.compute_spring_layout(
        graph, nx_k, nx_iterations, nx_random_state
    )

    node_trace = network_utils.create_node_trace(graph)
    edge_traces = network_utils.create_edge_traces(graph)

    fig = network_utils.create_network_graph(
        edge_traces,
        node_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    fig = network_utils.add_names_to_fig_nodes(fig, graph, n_labels)

    factormap = FactorMap()
    factormap.plot_ = fig
    factormap.table_ = matrix_list.cells_list_
    factormap.prompt_ = matrix_list.prompt_

    return factormap
