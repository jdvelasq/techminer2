# flake8: noqa
"""
Ego Network --- ChatGPT
===============================================================================


It can be obtained directly using functions in the **VantagePoint** module as
is explained in the following example.


>>> # Step 1: Define the root directory.
>>> root_dir = "data/regtech/"
>>> # Step 2: Compute the co-occurrence matrix.
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    root_dir=root_dir,
... )
>>> # Step 3: Extracts the selected items for the desired term.
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items='FINTECH',
...    is_ego_matrix=True,
... )
>>> # Step 4: Visualize the network using the matrix viewer.
>>> chart = vantagepoint.analyze.matrix_viewer(
...     matrix_subset,
...     nx_k=0.5,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> file_name = "sphinx/_static/tlab__sequence_analysis__ego_network.html"
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/tlab__sequence_analysis__ego_network.html"
    height="600px" width="100%" frameBorder="0"></iframe>

* Optional: ChatGPT prompt.

>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   REGTECH 28:329 |   FINTECH 12:249 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |   RISK_MANAGEMENT 03:014 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------:|
| REGTECH 28:329                 |               28 |               12 |                   7 |                   4 |                           3 |                             2 |                                2 |                        2 |
| FINTECH 12:249                 |               12 |               12 |                   2 |                   4 |                           2 |                             1 |                                1 |                        2 |
| COMPLIANCE 07:030              |                7 |                2 |                   7 |                   1 |                           0 |                             0 |                                1 |                        1 |
| REGULATION 05:164              |                4 |                4 |                   1 |                   5 |                           1 |                             0 |                                0 |                        2 |
| FINANCIAL_SERVICES 04:168      |                3 |                2 |                   0 |                   1 |                           4 |                             2 |                                0 |                        0 |
| FINANCIAL_REGULATION 04:035    |                2 |                1 |                   0 |                   0 |                           2 |                             4 |                                0 |                        0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                1 |                   1 |                   0 |                           0 |                             0 |                                4 |                        1 |
| RISK_MANAGEMENT 03:014         |                2 |                2 |                   1 |                   2 |                           0 |                             0 |                                1 |                        3 |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""
