# flake8: noqa
"""
Correlation Map
===============================================================================

Creates auto-correlation and cross-correlation maps.

Example: Auto-correlation map 
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/vantagepoint__corr_map_1.html"

>>> from techminer2 import vantagepoint
>>> matrix = vantagepoint.analyze.auto_corr_matrix(
...     rows_and_columns='authors',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> chart = vantagepoint.analyze.corr_map(matrix)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__corr_map_1.html"
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.prompt_)
Analyze the table below which contains the auto-correlation values for the authors. High correlation values indicate that the topics tends to appear together in the same document and forms a group. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row             | column           |   CORR |
|---:|:----------------|:-----------------|-------:|
|  2 | Arner DW 3:185  | Buckley RP 3:185 |  1     |
|  9 | Lin W 2:017     | Singh C 2:017    |  1     |
| 13 | Brennan R 2:014 | Crane M 2:014    |  1     |
| 15 | Hamdan A 2:018  | Sarea A 2:012    |  0.417 |
<BLANKLINE>
<BLANKLINE>

Example: Cross-correlation map 
-------------------------------------------------------------------------------


>>> file_name = "sphinx/_static/vantagepoint__corr_map_2.html"

>>> from techminer2 import vantagepoint
>>> matrix = vantagepoint.analyze.cross_corr_matrix(
...     rows_and_columns='authors',
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> chart = vantagepoint.analyze.corr_map(matrix)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__corr_map_2.html" height="600px" width="100%" frameBorder="0"></iframe>

    
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

from ... import network_utils
from ...classes import CorrMap
from .list_cells_in_matrix import list_cells_in_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-local-variables
def corr_map(
    matrix,
    nx_k=0.5,
    nx_iterations=10,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Correlation map."""

    matrix_list = list_cells_in_matrix(matrix)

    graph = network_utils.create_graph(
        matrix_list,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )

    graph = network_utils.set_edge_properties_for_corr_maps(graph)

    graph = network_utils.compute_spring_layout(
        graph, nx_k, nx_iterations, nx_random_state
    )

    node_trace = network_utils.create_node_trace(graph)
    text_trace = network_utils.create_text_trace(graph)
    edge_traces = network_utils.create_edge_traces(graph)

    fig = network_utils.create_network_graph(
        edge_traces,
        node_trace,
        text_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    corrmap = CorrMap()
    corrmap.plot_ = fig
    corrmap.table_ = matrix_list.cells_list_
    corrmap.prompt_ = matrix_list.prompt_

    return corrmap
