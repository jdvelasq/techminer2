# flake8: noqa
"""
Ego Graph --- ChatGPT
===============================================================================


It can be obtained directly using functions in the **VantagePoint** module as
is explained in the following example.


>>> # Step 1: Define the root directory.
>>> root_dir = "data/regtech/"
>>> # Step 1: Compute the co-occurrence matrix.
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topics_length=20,
...    root_dir=root_dir,
... )
>>> # Step 2: Extracts the topics for the desired term.
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics='fintech',
... )
>>> # Step 3: Visualize the radial diagram using the matrix viewer.
>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> file_name = "sphinx/_static/tlab__sequence_analysis__ego_graph.html"
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/tlab__sequence_analysis__ego_graph.html"
    height="600px" width="100%" frameBorder="0"></iframe>

* Optional: ChatGPT prompt.

>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['fintech'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   fintech 12:249 |
|:-------------------------------|-----------------:|
| regtech 28:329                 |               12 |
| regulatory technology 07:037   |                1 |
| compliance 07:030              |                2 |
| regulation 05:164              |                4 |
| financial services 04:168      |                2 |
| financial regulation 04:035    |                1 |
| artificial intelligence 04:023 |                1 |
| risk management 03:014         |                2 |
| innovation 03:012              |                1 |
| blockchain 03:005              |                1 |
| suptech 03:004                 |                2 |
| semantic technologies 02:041   |                2 |
| data protection 02:027         |                1 |
<BLANKLINE>
<BLANKLINE>




"""
