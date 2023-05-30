# flake8: noqa
"""
Ego Network --- ChatGPT
===============================================================================


It can be obtained directly using functions in the **VantagePoint** module as
is explained in the following example.


>>> # Step 1: Define the root directory.
>>> root_dir = "data/regtech/"
>>> # Step 1: Compute the co-occurrence matrix.
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topics_length=10,
...    root_dir=root_dir,
... )
>>> # Step 2: Extracts the topics for the desired term.
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics='fintech',
...    is_ego_matrix=True,
... )
>>> # Step 3: Visualize the network using the matrix viewer.
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
| row                            |   regtech 28:329 |   fintech 12:249 |   regulatory technology 07:037 |   compliance 07:030 |   regulation 05:164 |   financial services 04:168 |   financial regulation 04:035 |   artificial intelligence 04:023 |   risk management 03:014 |   fintech 12:249 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------:|-----------------:|
| regtech 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                           3 |                             2 |                                2 |                        2 |               12 |
| fintech 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                           2 |                             1 |                                1 |                        2 |               12 |
| regulatory technology 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                           0 |                             0 |                                1 |                        2 |                1 |
| compliance 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                           0 |                             0 |                                1 |                        1 |                2 |
| regulation 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                           1 |                             0 |                                0 |                        2 |                4 |
| financial services 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                           4 |                             2 |                                0 |                        0 |                2 |
| financial regulation 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                           2 |                             4 |                                0 |                        0 |                1 |
| artificial intelligence 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                           0 |                             0 |                                4 |                        1 |                1 |
| risk management 03:014         |                2 |                2 |                              2 |                   1 |                   2 |                           0 |                             0 |                                1 |                        3 |                2 |
| fintech 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                           2 |                             1 |                                1 |                        2 |               12 |
<BLANKLINE>
<BLANKLINE>



"""
