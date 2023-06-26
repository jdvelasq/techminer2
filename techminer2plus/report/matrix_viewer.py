# flake8: noqa
"""
Matrix Viewer
===============================================================================



>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/report/matrix_viewer_0.html"

>>> import techminer2plus 
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...     columns='author_keywords',
...     rows='authors',
...     col_occ_range=(2, None),
...     row_occ_range=(2, None),
...     root_dir=root_dir,
... )

>>> chart = techminer2plus.report.matrix_viewer(
...     cooc_matrix, 
...     n_labels=15,
...     node_size_min=12,
...     node_size_max=70,
...     textfont_size_min=7,
...     textfont_size_max=20,
...     xaxes_range=(-2,2)
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/report/matrix_viewer_0.html"
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.prompt_)
Analyze the table below, which contains the the occurrence values for \\
author_keywords and authors. Identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research \\
field. Be sure to provide a concise summary of your findings in no more \\
than 150 words.
<BLANKLINE>
Table:
```
|    | row                | column                         |   OCC |
|---:|:-------------------|:-------------------------------|------:|
|  0 | Arner DW 3:185     | REGTECH 28:329                 |     2 |
|  1 | Buckley RP 3:185   | REGTECH 28:329                 |     2 |
|  2 | Barberis JN 2:161  | REGTECH 28:329                 |     1 |
|  3 | Butler T 2:041     | REGTECH 28:329                 |     2 |
|  4 | Lin W 2:017        | REGTECH 28:329                 |     2 |
|  6 | Brennan R 2:014    | REGTECH 28:329                 |     2 |
|  7 | Crane M 2:014      | REGTECH 28:329                 |     2 |
|  9 | Grassi L 2:002     | REGTECH 28:329                 |     2 |
| 10 | Lanfranchi D 2:002 | REGTECH 28:329                 |     2 |
| 11 | Arman AA 2:000     | REGTECH 28:329                 |     2 |
| 12 | Arner DW 3:185     | FINTECH 12:249                 |     1 |
| 13 | Buckley RP 3:185   | FINTECH 12:249                 |     1 |
| 14 | Butler T 2:041     | FINTECH 12:249                 |     2 |
| 17 | Hamdan A 2:018     | REGULATORY_TECHNOLOGY 07:037   |     2 |
| 20 | Grassi L 2:002     | REGULATORY_TECHNOLOGY 07:037   |     1 |
| 21 | Lanfranchi D 2:002 | REGULATORY_TECHNOLOGY 07:037   |     1 |
| 22 | Brennan R 2:014    | COMPLIANCE 07:030              |     2 |
| 27 | Butler T 2:041     | REGULATION 05:164              |     1 |
| 28 | Grassi L 2:002     | REGULATION 05:164              |     2 |
| 29 | Lanfranchi D 2:002 | REGULATION 05:164              |     2 |
| 35 | Arner DW 3:185     | FINANCIAL_SERVICES 04:168      |     1 |
| 36 | Buckley RP 3:185   | FINANCIAL_SERVICES 04:168      |     1 |
| 37 | Barberis JN 2:161  | FINANCIAL_SERVICES 04:168      |     1 |
| 38 | Arner DW 3:185     | FINANCIAL_REGULATION 04:035    |     2 |
| 39 | Buckley RP 3:185   | FINANCIAL_REGULATION 04:035    |     2 |
| 40 | Barberis JN 2:161  | FINANCIAL_REGULATION 04:035    |     1 |
| 44 | Butler T 2:041     | RISK_MANAGEMENT 03:014         |     1 |
| 45 | Grassi L 2:002     | RISK_MANAGEMENT 03:014         |     1 |
| 46 | Lanfranchi D 2:002 | RISK_MANAGEMENT 03:014         |     1 |
| 47 | Grassi L 2:002     | INNOVATION 03:012              |     1 |
| 49 | Grassi L 2:002     | SUPTECH 03:004                 |     1 |
| 50 | Lanfranchi D 2:002 | SUPTECH 03:004                 |     1 |
| 51 | Arman AA 2:000     | SUPTECH 03:004                 |     1 |
| 52 | Butler T 2:041     | SEMANTIC_TECHNOLOGIES 02:041   |     2 |
| 53 | Arner DW 3:185     | DATA_PROTECTION 02:027         |     1 |
| 54 | Buckley RP 3:185   | DATA_PROTECTION 02:027         |     1 |
| 62 | Brennan R 2:014    | DATA_PROTECTION_OFFICER 02:014 |     2 |
| 63 | Crane M 2:014      | DATA_PROTECTION_OFFICER 02:014 |     2 |
| 65 | Brennan R 2:014    | GDPR 02:014                    |     2 |
| 66 | Crane M 2:014      | GDPR 02:014                    |     2 |
| 68 | Arner DW 3:185     | SANDBOXES 02:012               |     1 |
| 69 | Buckley RP 3:185   | SANDBOXES 02:012               |     1 |
| 70 | Barberis JN 2:161  | SANDBOXES 02:012               |     1 |
| 71 | Arman AA 2:000     | TECHNOLOGY 02:010              |     1 |
| 74 | Grassi L 2:002     | REPORTING 02:001               |     1 |
| 75 | Lanfranchi D 2:002 | REPORTING 02:001               |     1 |
```
<BLANKLINE>




>>> file_name = "sphinx/_static/report/matrix_viewer_1.html"

>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    row_top_n=10,
...    root_dir=root_dir,
... )


>>> chart = techminer2plus.report.matrix_viewer(
...     cooc_matrix,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/report/matrix_viewer_1.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(chart.prompt_)
Analyze the table below, which contains the the co-occurrence values for \\
author_keywords. Identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
|    | row                            | column                         |   OCC |
|---:|:-------------------------------|:-------------------------------|------:|
|  1 | FINTECH 12:249                 | REGTECH 28:329                 |    12 |
|  3 | COMPLIANCE 07:030              | REGTECH 28:329                 |     7 |
|  5 | ANTI_MONEY_LAUNDERING 05:034   | REGTECH 28:329                 |     1 |
|  6 | FINANCIAL_SERVICES 04:168      | REGTECH 28:329                 |     3 |
|  7 | FINANCIAL_REGULATION 04:035    | REGTECH 28:329                 |     2 |
|  8 | ARTIFICIAL_INTELLIGENCE 04:023 | REGTECH 28:329                 |     2 |
| 13 | COMPLIANCE 07:030              | FINTECH 12:249                 |     2 |
| 15 | FINANCIAL_SERVICES 04:168      | FINTECH 12:249                 |     2 |
| 16 | FINANCIAL_REGULATION 04:035    | FINTECH 12:249                 |     1 |
| 17 | ARTIFICIAL_INTELLIGENCE 04:023 | FINTECH 12:249                 |     1 |
| 19 | REGTECH 28:329                 | REGULATORY_TECHNOLOGY 07:037   |     2 |
| 20 | FINTECH 12:249                 | REGULATORY_TECHNOLOGY 07:037   |     1 |
| 22 | COMPLIANCE 07:030              | REGULATORY_TECHNOLOGY 07:037   |     1 |
| 23 | REGULATION 05:164              | REGULATORY_TECHNOLOGY 07:037   |     1 |
| 24 | ANTI_MONEY_LAUNDERING 05:034   | REGULATORY_TECHNOLOGY 07:037   |     2 |
| 25 | ARTIFICIAL_INTELLIGENCE 04:023 | REGULATORY_TECHNOLOGY 07:037   |     1 |
| 32 | ARTIFICIAL_INTELLIGENCE 04:023 | COMPLIANCE 07:030              |     1 |
| 34 | REGTECH 28:329                 | REGULATION 05:164              |     4 |
| 35 | FINTECH 12:249                 | REGULATION 05:164              |     4 |
| 37 | COMPLIANCE 07:030              | REGULATION 05:164              |     1 |
| 39 | FINANCIAL_SERVICES 04:168      | REGULATION 05:164              |     1 |
| 49 | FINANCIAL_REGULATION 04:035    | FINANCIAL_SERVICES 04:168      |     2 |
| 58 | ANTI_MONEY_LAUNDERING 05:034   | ARTIFICIAL_INTELLIGENCE 04:023 |     1 |
| 61 | REGTECH 28:329                 | RISK_MANAGEMENT 03:014         |     2 |
| 62 | FINTECH 12:249                 | RISK_MANAGEMENT 03:014         |     2 |
| 63 | REGULATORY_TECHNOLOGY 07:037   | RISK_MANAGEMENT 03:014         |     2 |
| 64 | COMPLIANCE 07:030              | RISK_MANAGEMENT 03:014         |     1 |
| 65 | REGULATION 05:164              | RISK_MANAGEMENT 03:014         |     2 |
| 66 | ARTIFICIAL_INTELLIGENCE 04:023 | RISK_MANAGEMENT 03:014         |     1 |
```
<BLANKLINE>





# pylint: disable=line-too-long
"""
from ..analyze.matrix.list_cells_in_matrix import list_cells_in_matrix
from ..classes import MatrixViewer
from ..network_lib import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def matrix_viewer(
    cooc_matrix,
    #
    # Figure params:
    n_labels=None,
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Makes cluster map from a ocurrence flooding matrix."""

    graph = nx_create_graph_from_matrix(
        cooc_matrix,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )

    graph = nx_compute_spring_layout(
        graph, nx_k, nx_iterations, nx_random_state
    )

    node_trace = px_create_node_trace(graph)
    edge_traces = px_create_edge_traces(graph)

    fig = px_create_network_fig(
        edge_traces,
        node_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    fig = px_add_names_to_fig_nodes(fig, graph, n_labels, is_article=False)

    matrix_viewer_ = MatrixViewer()
    matrix_viewer_.plot_ = fig
    matrix_viewer_.graph_ = graph
    matrix_viewer_.table_ = list_cells_in_matrix(cooc_matrix).cells_list_
    matrix_viewer_.prompt_ = list_cells_in_matrix(cooc_matrix).prompt_

    return matrix_viewer_
