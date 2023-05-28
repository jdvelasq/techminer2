# flake8: noqa
"""
Radial Diagram --- ChatGPT
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.

It can be obtained directly using functions in the VantagePoint module as
is explained in the following example.

* Step 1: Import the VantagePoint module.

>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_associations__radial_diagram.html"

* Step 2: Create a co-occurrence matrix

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=3,
...    root_dir=root_dir,
... )

* Step 3: Create a subset of the co-occurrence matrix with the term to be analyzed.

>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics='regtech',
... )


* Step 4: Visualize the radial diagram using the matrix viewer.

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
Analyze the table below, which contains the the occurrence values for \
['regtech'] and author_keywords. Identify any notable patterns, trends, or \
outliers in the data, and discuss their implications for the research field. \
Be sure to provide a concise summary of your findings in no more than 150 \
words.
<BLANKLINE>
|    | row                            | column         |   OCC |
|---:|:-------------------------------|:---------------|------:|
|  0 | fintech 12:249                 | regtech 28:329 |    12 |
|  1 | compliance 07:030              | regtech 28:329 |     7 |
|  3 | financial services 04:168      | regtech 28:329 |     3 |
|  5 | artificial intelligence 04:023 | regtech 28:329 |     2 |
|  6 | blockchain 03:005              | regtech 28:329 |     2 |
|  7 | financial regulation 04:035    | regtech 28:329 |     2 |
| 10 | anti-money laundering 03:021   | regtech 28:329 |     1 |
| 11 | innovation 03:012              | regtech 28:329 |     1 |
<BLANKLINE>
<BLANKLINE>

"""
