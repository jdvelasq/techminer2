# flake8: noqa
"""
Matrix Subset (*) --- ChatGPT
===============================================================================



Example: Matrix subset for a occurrence matrix.
-------------------------------------------------------------------------------


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    other_criterion='authors',
...    topic_occ_min=2,
...    topics_length=10,
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics=['regtech', 'fintech'],
... )
>>> matrix_subset.matrix_
column             regtech 28:329  fintech 12:249
row                                              
Arner DW 3:185                  2               1
Buckley RP 3:185                2               1
Barberis JN 2:161               1               0
Butler T/1 2:041                2               2
Lin W 2:017                     2               0
Singh C 2:017                   2               0
Brennan R 2:014                 2               0
Crane M 2:014                   2               0

>>> print(matrix_subset.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['regtech', 'fintech'] and 'authors' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row               |   regtech 28:329 |   fintech 12:249 |
|:------------------|-----------------:|-----------------:|
| Arner DW 3:185    |                2 |                1 |
| Buckley RP 3:185  |                2 |                1 |
| Barberis JN 2:161 |                1 |                0 |
| Butler T/1 2:041  |                2 |                2 |
| Lin W 2:017       |                2 |                0 |
| Singh C 2:017     |                2 |                0 |
| Brennan R 2:014   |                2 |                0 |
| Crane M 2:014     |                2 |                0 |
<BLANKLINE>
<BLANKLINE>



Example: Matrix subset for a co-occurrence matrix.
-------------------------------------------------------------------------------


>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics=['regtech', 'fintech', "compliance", 'regulation', 
...        'financial services'],
... )
>>> matrix_subset.matrix_
column                          regtech 28:329  ...  financial services 04:168
row                                             ...                           
regulatory technology 07:037                 2  ...                          0
financial regulation 04:035                  2  ...                          2
artificial intelligence 04:023               2  ...                          0
anti-money laundering 03:021                 1  ...                          0
risk management 03:014                       2  ...                          0
innovation 03:012                            1  ...                          0
blockchain 03:005                            2  ...                          0
suptech 03:004                               3  ...                          0
<BLANKLINE>
[8 rows x 5 columns]


>>> print(matrix_subset.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['regtech', 'fintech', 'compliance', 'regulation', 'financial services'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   compliance 07:030 |   regulation 05:164 |   financial services 04:168 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|
| regulatory technology 07:037   |                2 |                1 |                   1 |                   1 |                           0 |
| financial regulation 04:035    |                2 |                1 |                   0 |                   0 |                           2 |
| artificial intelligence 04:023 |                2 |                1 |                   1 |                   0 |                           0 |
| anti-money laundering 03:021   |                1 |                0 |                   0 |                   0 |                           0 |
| risk management 03:014         |                2 |                2 |                   1 |                   2 |                           0 |
| innovation 03:012              |                1 |                1 |                   0 |                   1 |                           0 |
| blockchain 03:005              |                2 |                1 |                   1 |                   1 |                           0 |
| suptech 03:004                 |                3 |                2 |                   1 |                   1 |                           0 |
<BLANKLINE>
<BLANKLINE>

Example: Matrix subset for an ego matrix.
-------------------------------------------------------------------------------


>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics=['regtech', 'fintech', "compliance", 'regulation',
...        'financial services'],
...    is_ego_matrix=True,
... )
>>> matrix_subset.matrix_
column                          regtech 28:329  ...  financial services 04:168
row                                             ...                           
regtech 28:329                              28  ...                          3
fintech 12:249                              12  ...                          2
regulatory technology 07:037                 2  ...                          0
compliance 07:030                            7  ...                          0
regulation 05:164                            4  ...                          1
financial services 04:168                    3  ...                          4
financial regulation 04:035                  2  ...                          2
artificial intelligence 04:023               2  ...                          0
anti-money laundering 03:021                 1  ...                          0
risk management 03:014                       2  ...                          0
innovation 03:012                            1  ...                          0
blockchain 03:005                            2  ...                          0
suptech 03:004                               3  ...                          0
regtech 28:329                              28  ...                          3
fintech 12:249                              12  ...                          2
compliance 07:030                            7  ...                          0
regulation 05:164                            4  ...                          1
financial services 04:168                    3  ...                          4
<BLANKLINE>
[18 rows x 18 columns]

>>> print(matrix_subset.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   regulatory technology 07:037 |   compliance 07:030 |   regulation 05:164 |   financial services 04:168 |   financial regulation 04:035 |   artificial intelligence 04:023 |   anti-money laundering 03:021 |   risk management 03:014 |   innovation 03:012 |   blockchain 03:005 |   suptech 03:004 |   regtech 28:329 |   fintech 12:249 |   compliance 07:030 |   regulation 05:164 |   financial services 04:168 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------------:|-------------------------:|--------------------:|--------------------:|-----------------:|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|
| regtech 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                           3 |                             2 |                                2 |                              1 |                        2 |                   1 |                   2 |                3 |               28 |               12 |                   7 |                   4 |                           3 |
| fintech 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                           2 |                             1 |                                1 |                              0 |                        2 |                   1 |                   1 |                2 |               12 |               12 |                   2 |                   4 |                           2 |
| regulatory technology 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                           0 |                             0 |                                1 |                              1 |                        2 |                   1 |                   0 |                1 |                2 |                1 |                   1 |                   1 |                           0 |
| compliance 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                           0 |                             0 |                                1 |                              0 |                        1 |                   0 |                   1 |                1 |                7 |                2 |                   7 |                   1 |                           0 |
| regulation 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                           1 |                             0 |                                0 |                              0 |                        2 |                   1 |                   1 |                1 |                4 |                4 |                   1 |                   5 |                           1 |
| financial services 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                           4 |                             2 |                                0 |                              0 |                        0 |                   0 |                   0 |                0 |                3 |                2 |                   0 |                   1 |                           4 |
| financial regulation 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                           2 |                             4 |                                0 |                              0 |                        0 |                   1 |                   0 |                0 |                2 |                1 |                   0 |                   0 |                           2 |
| artificial intelligence 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                           0 |                             0 |                                4 |                              1 |                        1 |                   0 |                   1 |                0 |                2 |                1 |                   1 |                   0 |                           0 |
| anti-money laundering 03:021   |                1 |                0 |                              1 |                   0 |                   0 |                           0 |                             0 |                                1 |                              3 |                        0 |                   0 |                   0 |                0 |                1 |                0 |                   0 |                   0 |                           0 |
| risk management 03:014         |                2 |                2 |                              2 |                   1 |                   2 |                           0 |                             0 |                                1 |                              0 |                        3 |                   0 |                   0 |                1 |                2 |                2 |                   1 |                   2 |                           0 |
| innovation 03:012              |                1 |                1 |                              1 |                   0 |                   1 |                           0 |                             1 |                                0 |                              0 |                        0 |                   3 |                   0 |                0 |                1 |                1 |                   0 |                   1 |                           0 |
| blockchain 03:005              |                2 |                1 |                              0 |                   1 |                   1 |                           0 |                             0 |                                1 |                              0 |                        0 |                   0 |                   3 |                0 |                2 |                1 |                   1 |                   1 |                           0 |
| suptech 03:004                 |                3 |                2 |                              1 |                   1 |                   1 |                           0 |                             0 |                                0 |                              0 |                        1 |                   0 |                   0 |                3 |                3 |                2 |                   1 |                   1 |                           0 |
| regtech 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                           3 |                             2 |                                2 |                              1 |                        2 |                   1 |                   2 |                3 |               28 |               12 |                   7 |                   4 |                           3 |
| fintech 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                           2 |                             1 |                                1 |                              0 |                        2 |                   1 |                   1 |                2 |               12 |               12 |                   2 |                   4 |                           2 |
| compliance 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                           0 |                             0 |                                1 |                              0 |                        1 |                   0 |                   1 |                1 |                7 |                2 |                   7 |                   1 |                           0 |
| regulation 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                           1 |                             0 |                                0 |                              0 |                        2 |                   1 |                   1 |                1 |                4 |                4 |                   1 |                   5 |                           1 |
| financial services 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                           4 |                             2 |                                0 |                              0 |                        0 |                   0 |                   0 |                0 |                3 |                2 |                   0 |                   1 |                           4 |
<BLANKLINE>
<BLANKLINE>


>>> matrix_subset.topics_
['regtech 28:329', 'fintech 12:249', 'compliance 07:030', 'regulation 05:164', \
'financial services 04:168']

# pylint: disable=line-too-long
"""
from ...classes import MatrixSubset


def matrix_subset(
    obj,
    topics,
    is_ego_matrix=False,
):
    """Extracts a subset of columns and associated rows from a matrix.

    Args:
        obj (Matrix): A co-occurrnce matrix object.
        topics (list): A list of topics to extract.
        is_ego_matrix (bool): Whether the matrix is an ego matrix.

    Returns:
        MatrixSubset: A MatrixSubset object.

    """

    def extract_topic_positions(candidate_topics, topics):
        """Obtains the positions of topics in a list."""

        topic_positions = []
        candidate_topics = [col.split(" ")[:-1] for col in candidate_topics]
        candidate_topics = [" ".join(col) for col in candidate_topics]
        for topic in topics:
            if topic in candidate_topics:
                topic_positions.append(candidate_topics.index(topic))
        topic_positions = sorted(topic_positions)

        return topic_positions

    def select_columns(matrix, topic_positions):
        """Selects columns from a matrix."""

        return matrix.iloc[:, topic_positions]

    def select_no_zero_rows(matrix):
        """selects the rows with row sum > 0"""

        return matrix.loc[matrix.sum(axis=1) > 0, :]

    def generate_default_prompt(matrix, topics, other_criterion):
        """Generates a ChatGPT prompt for a occurrence matrix."""

        return (
            "Analyze the table below which contains values of co-occurrence "
            f"(OCC) for the {repr(topics)} and '{other_criterion}' fields "
            "in a bibliographic dataset. Identify any notable patterns, "
            "trends, or outliers in the data, and discuss their implications "
            "for the research field. Be sure to provide a concise summary of "
            "your findings in no more than 150 words."
            f"\n\n{matrix.to_markdown()}\n\n"
        )

    def generate_prompt_for_ego_matrix(matrix, other_criterion):
        """Generates a ChatGPT prompt for a occurrence matrix."""

        return (
            "Analyze the table below which contains values of co-occurrence "
            f"(OCC) for the '{other_criterion}' fields "
            "in a bibliographic dataset. Identify any notable patterns, "
            "trends, or outliers in the data, and discuss their implications "
            "for the research field. Be sure to provide a concise summary of "
            "your findings in no more than 150 words."
            f"\n\n{matrix.to_markdown()}\n\n"
        )

    #
    # Main:
    #

    if isinstance(topics, str):
        topics = [topics]

    matrix = obj.matrix_.copy()

    topic_positions = extract_topic_positions(
        candidate_topics=matrix.columns.tolist(), topics=topics
    )
    topics_ = [matrix.columns[pos] for pos in topic_positions]
    matrix = select_columns(matrix, topic_positions)
    matrix = select_no_zero_rows(matrix)

    augmented_topics = None
    if is_ego_matrix:
        augmented_topics = matrix.index.tolist() + matrix.columns.tolist()
        augmented_topics = [
            topic
            for topic in augmented_topics
            if topic in obj.matrix_.columns.tolist()
        ]
        matrix = obj.matrix_.loc[augmented_topics, augmented_topics]
    else:
        matrix = matrix.drop(
            labels=matrix.columns.tolist(), axis=0, errors="ignore"
        )

    if is_ego_matrix:
        prompt = generate_prompt_for_ego_matrix(matrix, obj.other_criterion_)
    else:
        prompt = generate_default_prompt(matrix, topics, obj.other_criterion_)

    # if obj.criterion_ == obj.other_criterion_:
    #     prompt = generate_prompt_for_co_occ_matrix(matrix, obj.criterion_)
    # else:
    #     prompt = generate_prompt_for_occ_matrix(
    #         matrix, obj.criterion_, obj.other_criterion_
    #     )

    matrix_subset_ = MatrixSubset()

    if is_ego_matrix:
        matrix_subset_.criterion_ = obj.criterion_
    else:
        matrix_subset_.criterion_ = repr(topics)
        matrix_subset_.criterion_ = obj.criterion_

    matrix_subset_.is_ego_matrix_ = is_ego_matrix
    matrix_subset_.matrix_ = matrix
    matrix_subset_.metric_ = obj.metric_
    matrix_subset_.other_criterion_ = obj.other_criterion_
    matrix_subset_.prompt_ = prompt
    matrix_subset_.topics_ = topics_

    return matrix_subset_
