"""
Column viewer
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__analyze__column_viewer.html"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     criterion='author_keywords',
...     topic_min_occ=3,
...     directory=directory,
... )

>>> chart = vantagepoint.analyze.column_viewer(
...     matrix=co_occ_matrix,
...     topic="regtech",
...     xaxes_range=(-2.5, 2.5),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__analyze__column_viewer.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> chart.table_.head()
                         row          column  OCC
0             fintech 12:249  regtech 28:329   12
1          compliance 07:030  regtech 28:329    7
2          regulation 05:164  regtech 28:329    4
3  financial services 04:168  regtech 28:329    3
4             suptech 03:004  regtech 28:329    3

>>> print(chart.prompt_)
The following table contains de occurrences of the term 'regtech' with the \
terms specified in the rows of the table of the table. The table is sorted \
by the number of occurrences. Identify any notable patterns, trends, or \
outliers in the data, and discuss their implications for the relationships \
among the terms. Be sure to provide a concise summary of your findings in \
no more than 30 words.
<BLANKLINE>
|    | row                            | column         |   OCC |
|---:|:-------------------------------|:---------------|------:|
|  0 | fintech 12:249                 | regtech 28:329 |    12 |
|  1 | compliance 07:030              | regtech 28:329 |     7 |
|  2 | regulation 05:164              | regtech 28:329 |     4 |
|  3 | financial services 04:168      | regtech 28:329 |     3 |
|  4 | suptech 03:004                 | regtech 28:329 |     3 |
|  5 | artificial intelligence 04:023 | regtech 28:329 |     2 |
|  6 | blockchain 03:005              | regtech 28:329 |     2 |
|  7 | financial regulation 04:035    | regtech 28:329 |     2 |
|  8 | regulatory technology 07:037   | regtech 28:329 |     2 |
|  9 | risk management 03:014         | regtech 28:329 |     2 |
| 10 | anti-money laundering 03:021   | regtech 28:329 |     1 |
| 11 | innovation 03:012              | regtech 28:329 |     1 |
<BLANKLINE>
<BLANKLINE>

# noqa: E501

"""

from ... import network_utils
from ...classes import ColumnViewer
from .list_cells_in_matrix import list_cells_in_matrix


def column_viewer(
    matrix,
    topic,
    nx_k=0.5,
    nx_iterations=10,
    node_min_size=15,
    node_max_size=70,
    textfont_size_min=7,
    textfont_size_max=20,
    show_axes=False,
    xaxes_range=None,
    yaxes_range=None,
    seed=0,
):
    """Creates a radial diagram of term associations from a (co) occurrence matrix."""

    def filter_matrix(matrix, topic):
        """Returns a matrix with the column specified by the topic."""

        # obtains the position of the topic in the columns
        columns = matrix.matrix_.columns.tolist()
        columns = [metric.split(" ")[:-1] for metric in columns]
        columns = [" ".join(metric) for metric in columns]
        topic_position = columns.index(topic)

        # selects the column with the topic
        matrix.matrix_ = matrix.matrix_.iloc[:, [topic_position]]
        matrix.criterion_for_columns_ = topic

        # obtains the position of the topic in the rows
        rows = matrix.matrix_.index.tolist()
        rows = [metric.split(" ")[:-1] for metric in rows]
        rows = [" ".join(metric) for metric in rows]
        topic_position = rows.index(topic)

        # drop the row with the topic
        matrix.matrix_ = matrix.matrix_.drop(
            matrix.matrix_.index[topic_position], axis=0
        )

        return matrix

    def extract_column_from_matrix(matrix):
        """Returns a matrix list with the column specified by the topic and value > 0."""

        matrix_list = list_cells_in_matrix(matrix)
        matrix_list.matrix_list_ = matrix_list.matrix_list_[
            matrix_list.matrix_list_["OCC"] > 0
        ]
        return matrix_list

    def generate_chatgpt_prompt(matrix_list, topic):
        text = (
            "The following table contains de occurrences of the term "
            f"'{topic}' with the terms specified in the rows of the table "
            "of the table. The table is sorted by the number of occurrences. "
            "Identify any notable patterns, trends, or outliers in the data, "
            "and discuss their implications for the relationships among the "
            "terms. Be sure to provide a concise summary of your findings "
            "in no more than 30 words."
            f"\n\n{matrix_list.matrix_list_.to_markdown()}\n\n"
        )
        return text

    #
    #
    # Main:
    #
    #

    matrix = filter_matrix(matrix, topic)

    matrix_list = extract_column_from_matrix(matrix)

    graph = network_utils.create_graph(
        matrix_list,
        node_min_size,
        node_max_size,
        textfont_size_min,
        textfont_size_max,
    )

    graph = network_utils.compute_spring_layout(
        graph, nx_k, nx_iterations, seed
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

    obj = ColumnViewer()
    obj.table_ = matrix_list.matrix_list_
    obj.plot_ = fig
    obj.prompt_ = generate_chatgpt_prompt(matrix_list, topic)
    obj.topic_ = topic

    return obj
