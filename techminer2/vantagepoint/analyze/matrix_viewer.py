# flake8: noqa
"""
Matrix Viewer --- ChatGPT
===============================================================================

>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-2.html"
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics='regtech',
... )
>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )


Example: Visulization of an occurrence matrix.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-0.html"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     criterion='author_keywords',
...     other_criterion='authors',
...     topic_occ_min=2,
...     topics_length=10,
...     root_dir=root_dir,
... )
>>> co_occ_matrix_list = vantagepoint.analyze.list_cells_in_matrix(
...     co_occ_matrix)
>>> co_occ_matrix_list.cells_list_.head()
                row                       column  OCC
0    Arner DW 3:185  financial regulation 04:035    2
1    Arner DW 3:185               regtech 28:329    2
2   Brennan R 2:014            compliance 07:030    2
3   Brennan R 2:014               regtech 28:329    2
4  Buckley RP 3:185  financial regulation 04:035    2

>>> chart = vantagepoint.analyze.matrix_viewer(
...     co_occ_matrix, xaxes_range=(-2,2)
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-0.html"
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.prompt_)
Analyze the table below, which contains the the occurrence values for \
author_keywords and authors. Identify any notable patterns, trends, or \
outliers in the data, and discuss their implications for the research field. \
Be sure to provide a concise summary of your findings in no more than 150 \
words.
<BLANKLINE>
|    | row               | column                         |   OCC |
|---:|:------------------|:-------------------------------|------:|
|  0 | Arner DW 3:185    | financial regulation 04:035    |     2 |
|  1 | Arner DW 3:185    | regtech 28:329                 |     2 |
|  2 | Brennan R 2:014   | compliance 07:030              |     2 |
|  3 | Brennan R 2:014   | regtech 28:329                 |     2 |
|  4 | Buckley RP 3:185  | financial regulation 04:035    |     2 |
|  5 | Buckley RP 3:185  | regtech 28:329                 |     2 |
|  6 | Butler T/1 2:041  | fintech 12:249                 |     2 |
|  7 | Butler T/1 2:041  | regtech 28:329                 |     2 |
|  8 | Crane M 2:014     | compliance 07:030              |     2 |
|  9 | Crane M 2:014     | regtech 28:329                 |     2 |
| 10 | Hamdan A 2:018    | regulatory technology 07:037   |     2 |
| 11 | Lin W 2:017       | regtech 28:329                 |     2 |
| 12 | Singh C 2:017     | regtech 28:329                 |     2 |
| 13 | Turki M 2:018     | regulatory technology 07:037   |     2 |
| 14 | Arner DW 3:185    | financial services 04:168      |     1 |
| 15 | Arner DW 3:185    | fintech 12:249                 |     1 |
| 16 | Barberis JN 2:161 | financial regulation 04:035    |     1 |
| 17 | Barberis JN 2:161 | financial services 04:168      |     1 |
| 18 | Barberis JN 2:161 | regtech 28:329                 |     1 |
| 19 | Buckley RP 3:185  | financial services 04:168      |     1 |
| 20 | Buckley RP 3:185  | fintech 12:249                 |     1 |
| 21 | Butler T/1 2:041  | regulation 05:164              |     1 |
| 22 | Butler T/1 2:041  | risk management 03:014         |     1 |
| 23 | Hamdan A 2:018    | anti-money laundering 03:021   |     1 |
| 24 | Lin W 2:017       | anti-money laundering 03:021   |     1 |
| 25 | Lin W 2:017       | artificial intelligence 04:023 |     1 |
| 26 | Singh C 2:017     | anti-money laundering 03:021   |     1 |
| 27 | Singh C 2:017     | artificial intelligence 04:023 |     1 |
| 28 | Turki M 2:018     | anti-money laundering 03:021   |     1 |
<BLANKLINE>
<BLANKLINE>


Example: Visulization of a co-occurrence matrix.
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-1.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     criterion='author_keywords',
...     topic_occ_min=7,
...     root_dir=root_dir,
... )
>>> co_occ_matrix_list = vantagepoint.analyze.list_cells_in_matrix(
...     co_occ_matrix)
>>> co_occ_matrix_list.cells_list_.head()
                 row             column  OCC
0     regtech 28:329     regtech 28:329   28
1     fintech 12:249     fintech 12:249   12
2     fintech 12:249     regtech 28:329   12
3     regtech 28:329     fintech 12:249   12
4  compliance 07:030  compliance 07:030    7

>>> chart = vantagepoint.analyze.matrix_viewer(
...     co_occ_matrix,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-1.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below, which contains the the co-occurrence values for \
author_keywords. Identify any notable patterns, trends, or outliers in the \
data, and discuss their implications for the research field. Be sure to \
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row               | column                       |   OCC |
|---:|:------------------|:-----------------------------|------:|
|  2 | fintech 12:249    | regtech 28:329               |    12 |
|  5 | compliance 07:030 | regtech 28:329               |     7 |
|  8 | compliance 07:030 | fintech 12:249               |     2 |
| 10 | regtech 28:329    | regulatory technology 07:037 |     2 |
| 12 | compliance 07:030 | regulatory technology 07:037 |     1 |
| 13 | fintech 12:249    | regulatory technology 07:037 |     1 |
<BLANKLINE>
<BLANKLINE>



Example: Visulization of a radial diagram (T-LAB).
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-2.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics='regtech',
... )
>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-2.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['regtech'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |
|:-------------------------------|-----------------:|
| fintech 12:249                 |               12 |
| regulatory technology 07:037   |                2 |
| compliance 07:030              |                7 |
| regulation 05:164              |                4 |
| financial services 04:168      |                3 |
| financial regulation 04:035    |                2 |
| artificial intelligence 04:023 |                2 |
| anti-money laundering 03:021   |                1 |
| risk management 03:014         |                2 |
| innovation 03:012              |                1 |
| blockchain 03:005              |                2 |
| suptech 03:004                 |                3 |
<BLANKLINE>
<BLANKLINE>



Example: Comparison between pairs of keywords (T-LAB).
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-3.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics=['regtech', 'regulatory technology'],
... )

>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-3.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['regtech', 'regulatory technology'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   regulatory technology 07:037 |
|:-------------------------------|-----------------:|-------------------------------:|
| fintech 12:249                 |               12 |                              1 |
| compliance 07:030              |                7 |                              1 |
| regulation 05:164              |                4 |                              1 |
| financial services 04:168      |                3 |                              0 |
| financial regulation 04:035    |                2 |                              0 |
| artificial intelligence 04:023 |                2 |                              1 |
| anti-money laundering 03:021   |                1 |                              1 |
| risk management 03:014         |                2 |                              2 |
| innovation 03:012              |                1 |                              1 |
| blockchain 03:005              |                2 |                              0 |
| suptech 03:004                 |                3 |                              1 |
<BLANKLINE>
<BLANKLINE>


Example: Ego-Network (T-LAB).
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-4.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics=['regtech'],
...    is_ego_matrix=True,
... )

>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-4.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   regulatory technology 07:037 |   compliance 07:030 |   regulation 05:164 |   financial services 04:168 |   financial regulation 04:035 |   artificial intelligence 04:023 |   anti-money laundering 03:021 |   risk management 03:014 |   innovation 03:012 |   blockchain 03:005 |   suptech 03:004 |   regtech 28:329 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------------:|-------------------------:|--------------------:|--------------------:|-----------------:|-----------------:|
| regtech 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                           3 |                             2 |                                2 |                              1 |                        2 |                   1 |                   2 |                3 |               28 |
| fintech 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                           2 |                             1 |                                1 |                              0 |                        2 |                   1 |                   1 |                2 |               12 |
| regulatory technology 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                           0 |                             0 |                                1 |                              1 |                        2 |                   1 |                   0 |                1 |                2 |
| compliance 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                           0 |                             0 |                                1 |                              0 |                        1 |                   0 |                   1 |                1 |                7 |
| regulation 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                           1 |                             0 |                                0 |                              0 |                        2 |                   1 |                   1 |                1 |                4 |
| financial services 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                           4 |                             2 |                                0 |                              0 |                        0 |                   0 |                   0 |                0 |                3 |
| financial regulation 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                           2 |                             4 |                                0 |                              0 |                        0 |                   1 |                   0 |                0 |                2 |
| artificial intelligence 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                           0 |                             0 |                                4 |                              1 |                        1 |                   0 |                   1 |                0 |                2 |
| anti-money laundering 03:021   |                1 |                0 |                              1 |                   0 |                   0 |                           0 |                             0 |                                1 |                              3 |                        0 |                   0 |                   0 |                0 |                1 |
| risk management 03:014         |                2 |                2 |                              2 |                   1 |                   2 |                           0 |                             0 |                                1 |                              0 |                        3 |                   0 |                   0 |                1 |                2 |
| innovation 03:012              |                1 |                1 |                              1 |                   0 |                   1 |                           0 |                             1 |                                0 |                              0 |                        0 |                   3 |                   0 |                0 |                1 |
| blockchain 03:005              |                2 |                1 |                              0 |                   1 |                   1 |                           0 |                             0 |                                1 |                              0 |                        0 |                   0 |                   3 |                0 |                2 |
| suptech 03:004                 |                3 |                2 |                              1 |                   1 |                   1 |                           0 |                             0 |                                0 |                              0 |                        1 |                   0 |                   0 |                3 |                3 |
| regtech 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                           3 |                             2 |                                2 |                              1 |                        2 |                   1 |                   2 |                3 |               28 |
<BLANKLINE>
<BLANKLINE>


"""

from ... import network_utils
from ...classes import MatrixSubset, MatrixViewer
from .list_cells_in_matrix import list_cells_in_matrix
from .network_viewer import network_viewer


# pylint: disable=too-many-arguments disable=too-many-locals
def matrix_viewer(
    obj,
    nx_k=0.5,
    nx_iterations=10,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    random_state=0,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Makes cluster map from a ocurrence flooding matrix."""

    matrix_list = list_cells_in_matrix(obj)

    graph = network_utils.create_graph(
        matrix_list,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )
    ####
    node_sizes = network_utils.extract_node_sizes(graph)
    ####

    if isinstance(obj, MatrixSubset):
        graph = network_utils.set_node_colors(graph, obj.topics_, "#556f81")

    graph = network_utils.compute_spring_layout(
        graph, nx_k, nx_iterations, random_state
    )

    fig = network_viewer(
        graph=graph,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        random_state=random_state,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )

    # node_trace = network_utils.create_node_trace(graph)
    # text_trace = network_utils.create_text_trace(graph)
    # edge_traces = network_utils.create_edge_traces(graph)

    # fig = network_utils.create_network_graph(
    #     edge_traces=edge_traces,
    #     node_trace=node_trace,
    #     text_trace=text_trace,
    #     xaxes_range=xaxes_range,
    #     yaxes_range=yaxes_range,
    #     show_axes=show_axes,
    # )

    matrix_viewer_ = MatrixViewer()
    matrix_viewer_.plot_ = fig
    matrix_viewer_.graph_ = graph
    matrix_viewer_.table_ = matrix_list.cells_list_

    if isinstance(obj, MatrixSubset):
        matrix_viewer_.prompt_ = obj.prompt_
    else:
        matrix_viewer_.prompt_ = matrix_list.prompt_

    return matrix_viewer_
