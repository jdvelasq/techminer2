"""
Radial Diagram
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_associations__radial_diagram.html"

>>> from techminer2 import tlab
>>> chart = tlab.word_associations.radial_diagram(
...     criterion='author_keywords',
...     topic="regtech",
...     topic_min_occ=3,
...     xaxes_range=(-2.5, 2.5),
...     directory=directory,
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/tlab__word_associations__radial_diagram.html" height="600px" width="100%" frameBorder="0"></iframe>

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
from ... import vantagepoint


def radial_diagram(
    criterion,
    topic,
    topics_length=None,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
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
    **filters,
):
    """Creates a radial diagram of term associations from a (co) occurrence matrix."""

    co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        root_dir=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    return vantagepoint.analyze.column_viewer(
        matrix=co_occ_matrix,
        topic=topic,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        node_min_size=node_min_size,
        node_max_size=node_max_size,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        show_axes=show_axes,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        seed=seed,
    )
