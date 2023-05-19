"""
Occurrence Matrix (GPT)
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.occ_matrix(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topic_min_occ=2,
...    directory=directory,
... )
>>> r.matrix_
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

>>> print(r.prompt_)
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
from dataclasses import dataclass

from ... import chatgpt
from .occ_matrix_list import occ_matrix_list


@dataclass(init=False)
class _MatrixResult:
    matrix_: None
    prompt_: None
    metric_: None
    criterion_for_columns_: None
    criterion_for_rows_: None


def occ_matrix(
    criterion_for_columns,
    criterion_for_rows=None,
    topics_length=None,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a co-occurrence matrix."""

    results = _MatrixResult()

    results.criterion_for_columns_ = criterion_for_columns
    results.criterion_for_rows_ = criterion_for_rows
    results.metric_ = "OCC"
    results.matrix_ = _create_matrix(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.prompt_ = chatgpt.generate_prompt_for_matrix(results)

    return results


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
    matrix_list = occ_matrix_list(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    ).matrix_list_

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    matrix = matrix.astype(int)

    columns = sorted(
        matrix.columns.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    )
    indexes = sorted(
        matrix.index.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    )
    matrix = matrix.loc[indexes, columns]

    return matrix
