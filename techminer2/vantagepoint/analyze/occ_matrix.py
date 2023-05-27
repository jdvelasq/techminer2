"""
Occurrence Matrix
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> occ_matrix = vantagepoint.analyze.occ_matrix(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topic_min_occ=2,
...    root_dir=root_dir,
... )
>>> occ_matrix.matrix_
column              regtech 28:329  ...  technology 02:010
row                                 ...                   
Arner DW 3:185                   2  ...                  0
Buckley RP 3:185                 2  ...                  0
Arman AA 2:000                   2  ...                  1
Barberis JN 2:161                1  ...                  0
Brennan R 2:014                  2  ...                  0
Butler T/1 2:041                 2  ...                  0
Crane M 2:014                    2  ...                  0
Grassi L 2:002                   2  ...                  0
Hamdan A 2:018                   0  ...                  0
Lanfranchi D 2:002               2  ...                  0
Lin W 2:017                      2  ...                  0
Ryan P 2:014                     2  ...                  0
Sarea A 2:012                    0  ...                  0
Singh C 2:017                    2  ...                  0
Turki M 2:018                    0  ...                  0
<BLANKLINE>
[15 rows x 24 columns]

>>> print(occ_matrix.prompt_)
Analyze the table below which contains values for the metric OCC. The columns of the table correspond to author_keywords, and the rows correspond to authors. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                |   regtech 28:329 |   fintech 12:249 |   compliance 07:030 |   regulatory technology 07:037 |   regulation 05:164 |   artificial intelligence 04:023 |   financial regulation 04:035 |   financial services 04:168 |   anti-money laundering 03:021 |   innovation 03:012 |   risk management 03:014 |   suptech 03:004 |   accountability 02:014 |   anti money laundering (aml) 02:013 |   charitytech 02:017 |   data protection 02:027 |   data protection officer 02:014 |   english law 02:017 |   finance 02:001 |   gdpr 02:014 |   reporting 02:001 |   sandbox 02:012 |   semantic technologies 02:041 |   technology 02:010 |
|:-------------------|-----------------:|-----------------:|--------------------:|-------------------------------:|--------------------:|---------------------------------:|------------------------------:|----------------------------:|-------------------------------:|--------------------:|-------------------------:|-----------------:|------------------------:|-------------------------------------:|---------------------:|-------------------------:|---------------------------------:|---------------------:|-----------------:|--------------:|-------------------:|-----------------:|-------------------------------:|--------------------:|
| Arner DW 3:185     |                2 |                1 |                   0 |                              0 |                   0 |                                0 |                             2 |                           1 |                              0 |                   0 |                        0 |                0 |                       0 |                                    0 |                    0 |                        1 |                                0 |                    0 |                0 |             0 |                  0 |                1 |                              0 |                   0 |
| Buckley RP 3:185   |                2 |                1 |                   0 |                              0 |                   0 |                                0 |                             2 |                           1 |                              0 |                   0 |                        0 |                0 |                       0 |                                    0 |                    0 |                        1 |                                0 |                    0 |                0 |             0 |                  0 |                1 |                              0 |                   0 |
| Arman AA 2:000     |                2 |                0 |                   0 |                              0 |                   0 |                                0 |                             0 |                           0 |                              0 |                   0 |                        0 |                1 |                       0 |                                    0 |                    0 |                        0 |                                0 |                    0 |                0 |             0 |                  0 |                0 |                              0 |                   1 |
| Barberis JN 2:161  |                1 |                0 |                   0 |                              0 |                   0 |                                0 |                             1 |                           1 |                              0 |                   0 |                        0 |                0 |                       0 |                                    0 |                    0 |                        0 |                                0 |                    0 |                0 |             0 |                  0 |                1 |                              0 |                   0 |
| Brennan R 2:014    |                2 |                0 |                   2 |                              0 |                   0 |                                0 |                             0 |                           0 |                              0 |                   0 |                        0 |                0 |                       2 |                                    0 |                    0 |                        0 |                                2 |                    0 |                0 |             2 |                  0 |                0 |                              0 |                   0 |
| Butler T/1 2:041   |                2 |                2 |                   0 |                              0 |                   1 |                                0 |                             0 |                           0 |                              0 |                   0 |                        1 |                0 |                       0 |                                    0 |                    0 |                        0 |                                0 |                    0 |                0 |             0 |                  0 |                0 |                              2 |                   0 |
| Crane M 2:014      |                2 |                0 |                   2 |                              0 |                   0 |                                0 |                             0 |                           0 |                              0 |                   0 |                        0 |                0 |                       2 |                                    0 |                    0 |                        0 |                                2 |                    0 |                0 |             2 |                  0 |                0 |                              0 |                   0 |
| Grassi L 2:002     |                2 |                2 |                   1 |                              1 |                   2 |                                0 |                             0 |                           0 |                              0 |                   1 |                        1 |                1 |                       0 |                                    0 |                    0 |                        0 |                                0 |                    0 |                1 |             0 |                  1 |                0 |                              0 |                   0 |
| Hamdan A 2:018     |                0 |                0 |                   0 |                              2 |                   0 |                                0 |                             0 |                           0 |                              1 |                   0 |                        0 |                0 |                       0 |                                    1 |                    0 |                        0 |                                0 |                    0 |                0 |             0 |                  0 |                0 |                              0 |                   0 |
| Lanfranchi D 2:002 |                2 |                2 |                   1 |                              1 |                   2 |                                0 |                             0 |                           0 |                              0 |                   1 |                        1 |                1 |                       0 |                                    0 |                    0 |                        0 |                                0 |                    0 |                1 |             0 |                  1 |                0 |                              0 |                   0 |
| Lin W 2:017        |                2 |                0 |                   0 |                              0 |                   0 |                                1 |                             0 |                           0 |                              1 |                   0 |                        0 |                0 |                       0 |                                    0 |                    2 |                        0 |                                0 |                    2 |                0 |             0 |                  0 |                0 |                              0 |                   0 |
| Ryan P 2:014       |                2 |                0 |                   2 |                              0 |                   0 |                                0 |                             0 |                           0 |                              0 |                   0 |                        0 |                0 |                       2 |                                    0 |                    0 |                        0 |                                2 |                    0 |                0 |             2 |                  0 |                0 |                              0 |                   0 |
| Sarea A 2:012      |                0 |                0 |                   0 |                              1 |                   0 |                                1 |                             0 |                           0 |                              0 |                   0 |                        0 |                0 |                       0 |                                    1 |                    0 |                        0 |                                0 |                    0 |                0 |             0 |                  0 |                0 |                              0 |                   0 |
| Singh C 2:017      |                2 |                0 |                   0 |                              0 |                   0 |                                1 |                             0 |                           0 |                              1 |                   0 |                        0 |                0 |                       0 |                                    0 |                    2 |                        0 |                                0 |                    2 |                0 |             0 |                  0 |                0 |                              0 |                   0 |
| Turki M 2:018      |                0 |                0 |                   0 |                              2 |                   0 |                                0 |                             0 |                           0 |                              1 |                   0 |                        0 |                0 |                       0 |                                    1 |                    0 |                        0 |                                0 |                    0 |                0 |             0 |                  0 |                0 |                              0 |                   0 |
<BLANKLINE>
<BLANKLINE>

"""


from ... import chatgpt, classes, techminer
from ...add_counters import add_counters
from ...load_utils import load_stopwords
from ...record_utils import read_records


def occ_matrix(
    column_criterion,
    row_criterion=None,
    topics_length=None,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a co-occurrence matrix."""

    matrix_ = _create_matrix(
        criterion_for_columns=column_criterion,
        criterion_for_rows=row_criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        directory=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    occurrenceMatrix = classes.OccurrenceMatrix()

    occurrenceMatrix.column_criterion_ = column_criterion
    occurrenceMatrix.row_criterion_ = row_criterion
    occurrenceMatrix.metric_ = "OCC"
    occurrenceMatrix.matrix_ = matrix_

    occurrenceMatrix.prompt_ = chatgpt.generate_prompt_for_matrix(
        occurrenceMatrix
    )

    return occurrenceMatrix


def _create_matrix(
    criterion_for_columns,
    criterion_for_rows,
    topics_length,
    topic_min_occ,
    topic_max_occ,
    topic_min_citations,
    topic_max_citations,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    matrix_list = _create_occ_matrix_list(
        column_criterion=criterion_for_columns,
        row_criterion=criterion_for_rows,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        root_directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    matrix = matrix.astype(int)

    columns = sorted(
        matrix.columns.tolist(),
        key=lambda x: x.split()[-1].split(":")[0],
        reverse=True,
    )
    indexes = sorted(
        matrix.index.tolist(),
        key=lambda x: x.split()[-1].split(":")[0],
        reverse=True,
    )
    matrix = matrix.loc[indexes, columns]

    return matrix


def _create_occ_matrix_list(
    column_criterion,
    row_criterion,
    topics_length,
    topic_min_occ,
    topic_max_occ,
    topic_min_citations,
    topic_max_citations,
    root_directory,
    database,
    start_year,
    end_year,
    **filters,
):
    matrix_list = techminer.indicators.occ_matrix_list(
        column_criterion=column_criterion,
        row_criterion=column_criterion,
        directory=root_directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    matrix_list = _remove_stopwords(root_directory, matrix_list)

    matrix_list = _select_topics_by_occ_and_citations_and_topic_length(
        matrix_list=matrix_list,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        topics_length=topics_length,
        criterion_for_columns=column_criterion,
        criterion_for_rows=row_criterion,
        directory=root_directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    for criterion, name in [
        (column_criterion, "column"),
        (row_criterion, "row"),
    ]:
        matrix_list = add_counters(
            column=criterion,
            name=name,
            directory=root_directory,
            database=database,
            table=matrix_list,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

    matrix_list = _sort_matrix_list(matrix_list)

    matrix_list = matrix_list.reset_index(drop=True)

    return matrix_list


def _sort_matrix_list(matrix_list):
    matrix_list = matrix_list.copy()

    for col in ["row", "column"]:
        col_upper = col.upper()
        matrix_list[col_upper] = matrix_list[col]
        matrix_list[col_upper] = matrix_list[col_upper].str.split()
        matrix_list[col_upper] = matrix_list[col_upper].map(lambda x: x[-1])

    matrix_list = matrix_list.sort_values(
        ["ROW", "row", "COLUMN", "column"],
        ascending=[False, True, False, True],
    )

    matrix_list = matrix_list.drop(columns=["ROW", "COLUMN"])
    matrix_list = matrix_list.reset_index(drop=True)

    return matrix_list


def _select_topics_by_occ_and_citations_and_topic_length(
    matrix_list,
    topic_min_occ,
    topic_max_occ,
    topic_min_citations,
    topic_max_citations,
    topics_length,
    criterion_for_columns,
    criterion_for_rows,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    for criterion in [criterion_for_columns, criterion_for_rows]:
        indicators = techminer.indicators.indicators_by_topic(
            criterion=criterion,
            root_dir=directory,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

        if topic_min_occ is not None:
            indicators = indicators[indicators.OCC >= topic_min_occ]
        if topic_max_occ is not None:
            indicators = indicators[indicators.OCC <= topic_max_occ]
        if topic_min_citations is not None:
            indicators = indicators[
                indicators.global_citations >= topic_min_citations
            ]
        if topic_max_citations is not None:
            indicators = indicators[
                indicators.global_citations <= topic_max_citations
            ]

        indicators = indicators.sort_values(
            ["OCC", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )

        if topics_length is not None:
            indicators = indicators.head(topics_length)

        topics = indicators.index.to_list()

        if criterion_for_columns == criterion_for_rows:
            matrix_list = matrix_list[matrix_list.column.isin(topics)]
            matrix_list = matrix_list[matrix_list.row.isin(topics)]
            break
        else:
            if criterion == criterion_for_columns:
                matrix_list = matrix_list[matrix_list.column.isin(topics)]
            else:
                matrix_list = matrix_list[matrix_list.row.isin(topics)]

    return matrix_list


def _remove_stopwords(directory, matrix_list):
    stopwords = load_stopwords(directory)
    matrix_list = matrix_list[~matrix_list["column"].isin(stopwords)]
    matrix_list = matrix_list[~matrix_list["row"].isin(stopwords)]
    return matrix_list
