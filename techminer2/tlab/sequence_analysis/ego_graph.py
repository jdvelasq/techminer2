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
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> # Step 2: Extracts the custom items for the desired term.
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items='FINTECH',
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
Analyze the table below which contains values of co-occurrence (OCC) for the ['FINTECH'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   FINTECH 12:249 |
|:-------------------------------|-----------------:|
| REGTECH 28:329                 |               12 |
| COMPLIANCE 07:030              |                2 |
| REGULATION 05:164              |                4 |
| FINANCIAL_SERVICES 04:168      |                2 |
| FINANCIAL_REGULATION 04:035    |                1 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                1 |
| RISK_MANAGEMENT 03:014         |                2 |
| INNOVATION 03:012              |                1 |
| REGULATORY_TECHNOLOGY 03:007   |                1 |
| BLOCKCHAIN 03:005              |                1 |
| SUPTECH 03:004                 |                2 |
| DATA_PROTECTION 02:027         |                1 |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
