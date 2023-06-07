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
0     Arner DW 3:185  REGTECH 28:329    2
1   Buckley RP 3:185  REGTECH 28:329    2
2  Barberis JN 2:161  REGTECH 28:329    1
3   Butler T/1 2:041  REGTECH 28:329    2
4        Lin W 2:017  REGTECH 28:329    2



>>> chart = vantagepoint.analyze.matrix_viewer(
...     co_occ_matrix, 
...     n_labels=15,
...     node_size_min=20,
...     node_size_max=70,
...     textfont_size_min=8,
...     textfont_size_max=20,
...     xaxes_range=(-2,2)
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-0.html"
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.prompt_)
Analyze the table below, which contains the the occurrence values for author_keywords and authors. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row                | column                                 |   OCC |
|---:|:-------------------|:---------------------------------------|------:|
|  0 | Arner DW 3:185     | REGTECH 28:329                         |     2 |
|  1 | Buckley RP 3:185   | REGTECH 28:329                         |     2 |
|  2 | Barberis JN 2:161  | REGTECH 28:329                         |     1 |
|  3 | Butler T/1 2:041   | REGTECH 28:329                         |     2 |
|  4 | Lin W 2:017        | REGTECH 28:329                         |     2 |
|  6 | Brennan R 2:014    | REGTECH 28:329                         |     2 |
|  7 | Crane M 2:014      | REGTECH 28:329                         |     2 |
|  9 | Grassi L 2:002     | REGTECH 28:329                         |     2 |
| 10 | Lanfranchi D 2:002 | REGTECH 28:329                         |     2 |
| 11 | Arman AA 2:000     | REGTECH 28:329                         |     2 |
| 12 | Arner DW 3:185     | FINTECH 12:249                         |     1 |
| 13 | Buckley RP 3:185   | FINTECH 12:249                         |     1 |
| 14 | Butler T/1 2:041   | FINTECH 12:249                         |     2 |
| 17 | Brennan R 2:014    | COMPLIANCE 07:030                      |     2 |
| 22 | Butler T/1 2:041   | REGULATION 05:164                      |     1 |
| 23 | Grassi L 2:002     | REGULATION 05:164                      |     2 |
| 24 | Lanfranchi D 2:002 | REGULATION 05:164                      |     2 |
| 25 | Arner DW 3:185     | FINANCIAL_SERVICES 04:168              |     1 |
| 26 | Buckley RP 3:185   | FINANCIAL_SERVICES 04:168              |     1 |
| 27 | Barberis JN 2:161  | FINANCIAL_SERVICES 04:168              |     1 |
| 28 | Arner DW 3:185     | FINANCIAL_REGULATION 04:035            |     2 |
| 29 | Buckley RP 3:185   | FINANCIAL_REGULATION 04:035            |     2 |
| 30 | Barberis JN 2:161  | FINANCIAL_REGULATION 04:035            |     1 |
| 31 | Hamdan A 2:018     | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |     2 |
| 41 | Butler T/1 2:041   | RISK_MANAGEMENT 03:014                 |     1 |
| 42 | Grassi L 2:002     | RISK_MANAGEMENT 03:014                 |     1 |
| 43 | Lanfranchi D 2:002 | RISK_MANAGEMENT 03:014                 |     1 |
| 44 | Grassi L 2:002     | INNOVATION 03:012                      |     1 |
| 46 | Grassi L 2:002     | REGULATORY_TECHNOLOGY 03:007           |     1 |
| 47 | Lanfranchi D 2:002 | REGULATORY_TECHNOLOGY 03:007           |     1 |
| 48 | Grassi L 2:002     | SUPTECH 03:004                         |     1 |
| 49 | Lanfranchi D 2:002 | SUPTECH 03:004                         |     1 |
| 50 | Arman AA 2:000     | SUPTECH 03:004                         |     1 |
| 51 | Arner DW 3:185     | DATA_PROTECTION 02:027                 |     1 |
| 52 | Buckley RP 3:185   | DATA_PROTECTION 02:027                 |     1 |
| 60 | Brennan R 2:014    | DATA_PROTECTION_OFFICER 02:014         |     2 |
| 61 | Crane M 2:014      | DATA_PROTECTION_OFFICER 02:014         |     2 |
| 63 | Brennan R 2:014    | GDPR 02:014                            |     2 |
| 64 | Crane M 2:014      | GDPR 02:014                            |     2 |
| 66 | Arner DW 3:185     | SANDBOXES 02:012                       |     1 |
| 67 | Buckley RP 3:185   | SANDBOXES 02:012                       |     1 |
| 68 | Barberis JN 2:161  | SANDBOXES 02:012                       |     1 |
| 69 | Arman AA 2:000     | TECHNOLOGY 02:010                      |     1 |
| 72 | Grassi L 2:002     | REPORTING 02:001                       |     1 |
| 73 | Lanfranchi D 2:002 | REPORTING 02:001                       |     1 |
<BLANKLINE>
<BLANKLINE>

Example: Visulization of a co-occurrence matrix.
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-1.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    row_top_n=10,
...    root_dir=root_dir,
... )
>>> vantagepoint.analyze.list_cells_in_matrix(co_occ_matrix).cells_list_.head()
                         row          column  OCC
0             REGTECH 28:329  REGTECH 28:329   28
1             FINTECH 12:249  REGTECH 28:329   12
2          COMPLIANCE 07:030  REGTECH 28:329    7
3          REGULATION 05:164  REGTECH 28:329    4
4  FINANCIAL_SERVICES 04:168  REGTECH 28:329    3



>>> chart = vantagepoint.analyze.matrix_viewer(
...     co_occ_matrix,
...     nx_k=0.1,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-1.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below, which contains the the co-occurrence values for author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row                            | column                                 |   OCC |
|---:|:-------------------------------|:---------------------------------------|------:|
|  1 | FINTECH 12:249                 | REGTECH 28:329                         |    12 |
|  2 | COMPLIANCE 07:030              | REGTECH 28:329                         |     7 |
|  4 | FINANCIAL_SERVICES 04:168      | REGTECH 28:329                         |     3 |
|  5 | FINANCIAL_REGULATION 04:035    | REGTECH 28:329                         |     2 |
|  6 | ARTIFICIAL_INTELLIGENCE 04:023 | REGTECH 28:329                         |     2 |
|  7 | ANTI_MONEY_LAUNDERING 04:023   | REGTECH 28:329                         |     1 |
| 11 | COMPLIANCE 07:030              | FINTECH 12:249                         |     2 |
| 13 | FINANCIAL_SERVICES 04:168      | FINTECH 12:249                         |     2 |
| 14 | FINANCIAL_REGULATION 04:035    | FINTECH 12:249                         |     1 |
| 15 | ARTIFICIAL_INTELLIGENCE 04:023 | FINTECH 12:249                         |     1 |
| 21 | ARTIFICIAL_INTELLIGENCE 04:023 | COMPLIANCE 07:030                      |     1 |
| 23 | REGTECH 28:329                 | REGULATION 05:164                      |     4 |
| 24 | FINTECH 12:249                 | REGULATION 05:164                      |     4 |
| 25 | COMPLIANCE 07:030              | REGULATION 05:164                      |     1 |
| 27 | FINANCIAL_SERVICES 04:168      | REGULATION 05:164                      |     1 |
| 33 | FINANCIAL_REGULATION 04:035    | FINANCIAL_SERVICES 04:168              |     2 |
| 39 | ANTI_MONEY_LAUNDERING 04:023   | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |     1 |
| 44 | ANTI_MONEY_LAUNDERING 04:023   | ARTIFICIAL_INTELLIGENCE 04:023         |     1 |
| 50 | REGTECH 28:329                 | RISK_MANAGEMENT 03:014                 |     2 |
| 51 | FINTECH 12:249                 | RISK_MANAGEMENT 03:014                 |     2 |
| 52 | COMPLIANCE 07:030              | RISK_MANAGEMENT 03:014                 |     1 |
| 53 | REGULATION 05:164              | RISK_MANAGEMENT 03:014                 |     2 |
| 54 | ARTIFICIAL_INTELLIGENCE 04:023 | RISK_MANAGEMENT 03:014                 |     1 |
<BLANKLINE>
<BLANKLINE>




Example: Visulization of a radial diagram (T-LAB).
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-2.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items='REGTECH',
... )
>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.1,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-2.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['REGTECH'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   REGTECH 28:329 |
|:-------------------------------|-----------------:|
| FINTECH 12:249                 |               12 |
| COMPLIANCE 07:030              |                7 |
| REGULATION 05:164              |                4 |
| FINANCIAL_SERVICES 04:168      |                3 |
| FINANCIAL_REGULATION 04:035    |                2 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |
| ANTI_MONEY_LAUNDERING 04:023   |                1 |
| RISK_MANAGEMENT 03:014         |                2 |
| INNOVATION 03:012              |                1 |
| REGULATORY_TECHNOLOGY 03:007   |                2 |
| BLOCKCHAIN 03:005              |                2 |
| SUPTECH 03:004                 |                3 |
<BLANKLINE>
<BLANKLINE>




Example: Comparison between pairs of keywords (T-LAB).
-------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-3.html"

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items=['REGTECH', 'REGULATORY_TECHNOLOGY'],
... )

>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.1,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__matrix_viewer-3.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['REGTECH', 'REGULATORY_TECHNOLOGY'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   REGTECH 28:329 |   REGULATORY_TECHNOLOGY 03:007 |
|:-------------------------------|-----------------:|-------------------------------:|
| FINTECH 12:249                 |               12 |                              1 |
| COMPLIANCE 07:030              |                7 |                              1 |
| REGULATION 05:164              |                4 |                              1 |
| FINANCIAL_SERVICES 04:168      |                3 |                              0 |
| FINANCIAL_REGULATION 04:035    |                2 |                              0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                              1 |
| ANTI_MONEY_LAUNDERING 04:023   |                1 |                              0 |
| RISK_MANAGEMENT 03:014         |                2 |                              2 |
| INNOVATION 03:012              |                1 |                              0 |
| BLOCKCHAIN 03:005              |                2 |                              0 |
| SUPTECH 03:004                 |                3 |                              1 |
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
...    custom_items='REGTECH',
...    is_ego_matrix=True,
... )

>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.1,
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
| row                            |   REGTECH 28:329 |   FINTECH 12:249 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |   ANTI_MONEY_LAUNDERING 04:023 |   RISK_MANAGEMENT 03:014 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------------:|-------------------------:|
| REGTECH 28:329                 |               28 |               12 |                   7 |                   4 |                           3 |                             2 |                                2 |                              1 |                        2 |
| FINTECH 12:249                 |               12 |               12 |                   2 |                   4 |                           2 |                             1 |                                1 |                              0 |                        2 |
| COMPLIANCE 07:030              |                7 |                2 |                   7 |                   1 |                           0 |                             0 |                                1 |                              0 |                        1 |
| REGULATION 05:164              |                4 |                4 |                   1 |                   5 |                           1 |                             0 |                                0 |                              0 |                        2 |
| FINANCIAL_SERVICES 04:168      |                3 |                2 |                   0 |                   1 |                           4 |                             2 |                                0 |                              0 |                        0 |
| FINANCIAL_REGULATION 04:035    |                2 |                1 |                   0 |                   0 |                           2 |                             4 |                                0 |                              0 |                        0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                1 |                   1 |                   0 |                           0 |                             0 |                                4 |                              1 |                        1 |
| ANTI_MONEY_LAUNDERING 04:023   |                1 |                0 |                   0 |                   0 |                           0 |                             0 |                                1 |                              4 |                        0 |
| RISK_MANAGEMENT 03:014         |                2 |                2 |                   1 |                   2 |                           0 |                             0 |                                1 |                              0 |                        3 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
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
    n_labels=None,
    nx_k=0.1,
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

    if isinstance(obj, MatrixSubset):
        graph = set_node_colors(graph, obj.custom_items_, "#556f81")

    graph = compute_spring_layout(graph, nx_k, nx_iterations, random_state)

    fig = network_viewer(
        graph=graph,
        n_labels=n_labels,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        random_state=random_state,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )

    matrix_viewer_ = MatrixViewer()
    matrix_viewer_.plot_ = fig
    matrix_viewer_.graph_ = graph
    matrix_viewer_.table_ = matrix_list.cells_list_

    if isinstance(obj, MatrixSubset):
        matrix_viewer_.prompt_ = obj.prompt_
    else:
        matrix_viewer_.prompt_ = matrix_list.prompt_

    return matrix_viewer_
