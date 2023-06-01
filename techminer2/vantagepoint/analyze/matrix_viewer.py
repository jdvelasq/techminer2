# flake8: noqa
"""
Matrix Viewer
===============================================================================



Example: Visulization of an occurrence matrix.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-0.html"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     columns='author_keywords',
...     rows='authors',
...     col_occ_range=(2, None),
...     row_occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> vantagepoint.analyze.list_cells_in_matrix(co_occ_matrix).cells_list_.head()
                 row          column  OCC
0     Arner DW 3:185  regtech 28:329    2
1   Buckley RP 3:185  regtech 28:329    2
2  Barberis JN 2:161  regtech 28:329    1
3   Butler T/1 2:041  regtech 28:329    2
4        Lin W 2:017  regtech 28:329    2


>>> chart = vantagepoint.analyze.matrix_viewer(
...     co_occ_matrix, xaxes_range=(-2,2)
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-0.html"
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.prompt_)
Analyze the table below, which contains the the occurrence values for author_keywords and authors. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row                | column                             |   OCC |
|---:|:-------------------|:-----------------------------------|------:|
|  0 | Arner DW 3:185     | regtech 28:329                     |     2 |
|  1 | Buckley RP 3:185   | regtech 28:329                     |     2 |
|  2 | Barberis JN 2:161  | regtech 28:329                     |     1 |
|  3 | Butler T/1 2:041   | regtech 28:329                     |     2 |
|  4 | Lin W 2:017        | regtech 28:329                     |     2 |
|  5 | Singh C 2:017      | regtech 28:329                     |     2 |
|  6 | Brennan R 2:014    | regtech 28:329                     |     2 |
|  7 | Crane M 2:014      | regtech 28:329                     |     2 |
|  8 | Ryan P 2:014       | regtech 28:329                     |     2 |
|  9 | Grassi L 2:002     | regtech 28:329                     |     2 |
| 10 | Lanfranchi D 2:002 | regtech 28:329                     |     2 |
| 11 | Arman AA 2:000     | regtech 28:329                     |     2 |
| 12 | Arner DW 3:185     | fintech 12:249                     |     1 |
| 13 | Buckley RP 3:185   | fintech 12:249                     |     1 |
| 14 | Butler T/1 2:041   | fintech 12:249                     |     2 |
| 15 | Grassi L 2:002     | fintech 12:249                     |     2 |
| 16 | Lanfranchi D 2:002 | fintech 12:249                     |     2 |
| 17 | Hamdan A 2:018     | regulatory technology 07:037       |     2 |
| 18 | Turki M 2:018      | regulatory technology 07:037       |     2 |
| 19 | Sarea A 2:012      | regulatory technology 07:037       |     1 |
| 20 | Grassi L 2:002     | regulatory technology 07:037       |     1 |
| 21 | Lanfranchi D 2:002 | regulatory technology 07:037       |     1 |
| 22 | Brennan R 2:014    | compliance 07:030                  |     2 |
| 23 | Crane M 2:014      | compliance 07:030                  |     2 |
| 24 | Ryan P 2:014       | compliance 07:030                  |     2 |
| 25 | Grassi L 2:002     | compliance 07:030                  |     1 |
| 26 | Lanfranchi D 2:002 | compliance 07:030                  |     1 |
| 27 | Butler T/1 2:041   | regulation 05:164                  |     1 |
| 28 | Grassi L 2:002     | regulation 05:164                  |     2 |
| 29 | Lanfranchi D 2:002 | regulation 05:164                  |     2 |
| 30 | Arner DW 3:185     | financial services 04:168          |     1 |
| 31 | Buckley RP 3:185   | financial services 04:168          |     1 |
| 32 | Barberis JN 2:161  | financial services 04:168          |     1 |
| 33 | Arner DW 3:185     | financial regulation 04:035        |     2 |
| 34 | Buckley RP 3:185   | financial regulation 04:035        |     2 |
| 35 | Barberis JN 2:161  | financial regulation 04:035        |     1 |
| 36 | Lin W 2:017        | artificial intelligence 04:023     |     1 |
| 37 | Singh C 2:017      | artificial intelligence 04:023     |     1 |
| 38 | Sarea A 2:012      | artificial intelligence 04:023     |     1 |
| 39 | Hamdan A 2:018     | anti-money laundering 03:021       |     1 |
| 40 | Turki M 2:018      | anti-money laundering 03:021       |     1 |
| 41 | Lin W 2:017        | anti-money laundering 03:021       |     1 |
| 42 | Singh C 2:017      | anti-money laundering 03:021       |     1 |
| 43 | Butler T/1 2:041   | risk management 03:014             |     1 |
| 44 | Grassi L 2:002     | risk management 03:014             |     1 |
| 45 | Lanfranchi D 2:002 | risk management 03:014             |     1 |
| 46 | Grassi L 2:002     | innovation 03:012                  |     1 |
| 47 | Lanfranchi D 2:002 | innovation 03:012                  |     1 |
| 48 | Grassi L 2:002     | suptech 03:004                     |     1 |
| 49 | Lanfranchi D 2:002 | suptech 03:004                     |     1 |
| 50 | Arman AA 2:000     | suptech 03:004                     |     1 |
| 51 | Butler T/1 2:041   | semantic technologies 02:041       |     2 |
| 52 | Arner DW 3:185     | data protection 02:027             |     1 |
| 53 | Buckley RP 3:185   | data protection 02:027             |     1 |
| 54 | Lin W 2:017        | charitytech 02:017                 |     2 |
| 55 | Singh C 2:017      | charitytech 02:017                 |     2 |
| 56 | Lin W 2:017        | english law 02:017                 |     2 |
| 57 | Singh C 2:017      | english law 02:017                 |     2 |
| 58 | Brennan R 2:014    | accountability 02:014              |     2 |
| 59 | Crane M 2:014      | accountability 02:014              |     2 |
| 60 | Ryan P 2:014       | accountability 02:014              |     2 |
| 61 | Brennan R 2:014    | data protection officer 02:014     |     2 |
| 62 | Crane M 2:014      | data protection officer 02:014     |     2 |
| 63 | Ryan P 2:014       | data protection officer 02:014     |     2 |
| 64 | Brennan R 2:014    | gdpr 02:014                        |     2 |
| 65 | Crane M 2:014      | gdpr 02:014                        |     2 |
| 66 | Ryan P 2:014       | gdpr 02:014                        |     2 |
| 67 | Hamdan A 2:018     | anti money laundering (aml) 02:013 |     1 |
| 68 | Turki M 2:018      | anti money laundering (aml) 02:013 |     1 |
| 69 | Sarea A 2:012      | anti money laundering (aml) 02:013 |     1 |
| 70 | Arner DW 3:185     | sandbox 02:012                     |     1 |
| 71 | Buckley RP 3:185   | sandbox 02:012                     |     1 |
| 72 | Barberis JN 2:161  | sandbox 02:012                     |     1 |
| 73 | Arman AA 2:000     | technology 02:010                  |     1 |
| 74 | Grassi L 2:002     | finance 02:001                     |     1 |
| 75 | Lanfranchi D 2:002 | finance 02:001                     |     1 |
| 76 | Grassi L 2:002     | reporting 02:001                   |     1 |
| 77 | Lanfranchi D 2:002 | reporting 02:001                   |     1 |
<BLANKLINE>
<BLANKLINE>


Example: Visulization of a co-occurrence matrix.
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-1.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    root_dir=root_dir,
... )
>>> vantagepoint.analyze.list_cells_in_matrix(co_occ_matrix).cells_list_.head()
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
...    columns='author_keywords',
...    col_top_n=3,
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
...    columns='author_keywords',
...    col_top_n=3,
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
...    columns='author_keywords',
...    col_top_n=10,
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

from ...classes import MatrixSubset, MatrixViewer
from ...network_utils import (
    compute_spring_layout,
    create_graph,
    set_node_colors,
)
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

    graph = create_graph(
        matrix_list,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )
    ####
    # node_sizes = network_utils.extract_node_sizes(graph)
    ####

    if isinstance(obj, MatrixSubset):
        graph = set_node_colors(graph, obj.topics_, "#556f81")

    graph = compute_spring_layout(graph, nx_k, nx_iterations, random_state)

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
