# flake8: noqa
"""
Radial Diagram --- ChatGPT
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.

It can be obtained directly using functions in the **VantagePoint** module as
is explained in the following example.



>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_associations__radial_diagram.html"
>>> # Create a co-occurrence matrix
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> # Create a subset of the co-occurrence matrix with the term to be analyzed.
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items='regtech',
... )
>>> # Visualize the radial diagram using the matrix viewer.
>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/tlab__word_associations__radial_diagram.html"
    height="600px" width="100%" frameBorder="0"></iframe>

* Optional: ChatGPT prompt.

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

"""
