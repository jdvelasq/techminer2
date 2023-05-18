"""
Occurrence Matrix List (GPT)
===============================================================================


>>> directory = "data/regtech/"

**Item selection by occurrence.**

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.matrix.occ_matrix_list(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topic_min_occ=3,
...    directory=directory,
... )
>>> r.matrix_list_
                row                       column  OCC
0    Arner DW 3:185               regtech 28:329    2
1    Arner DW 3:185               fintech 12:249    1
2    Arner DW 3:185    financial services 04:168    1
3    Arner DW 3:185  financial regulation 04:035    2
4  Buckley RP 3:185               regtech 28:329    2
5  Buckley RP 3:185               fintech 12:249    1
6  Buckley RP 3:185    financial services 04:168    1
7  Buckley RP 3:185  financial regulation 04:035    2


>>> print(r.prompt_)
Analyze the table below, which contains the the metric OCC for author_keywords and authors. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row              | column                      |   OCC |
|---:|:-----------------|:----------------------------|------:|
|  0 | Arner DW 3:185   | regtech 28:329              |     2 |
|  1 | Arner DW 3:185   | fintech 12:249              |     1 |
|  2 | Arner DW 3:185   | financial services 04:168   |     1 |
|  3 | Arner DW 3:185   | financial regulation 04:035 |     2 |
|  4 | Buckley RP 3:185 | regtech 28:329              |     2 |
|  5 | Buckley RP 3:185 | fintech 12:249              |     1 |
|  6 | Buckley RP 3:185 | financial services 04:168   |     1 |
|  7 | Buckley RP 3:185 | financial regulation 04:035 |     2 |
<BLANKLINE>
<BLANKLINE>

**Seleccition of top terms.**

>>> vantagepoint.analyze.matrix.occ_matrix_list(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topics_length=5,
...    directory=directory,
... ).matrix_list_
                 row                        column  OCC
0     Arner DW 3:185                regtech 28:329    2
1     Arner DW 3:185                fintech 12:249    1
2   Buckley RP 3:185                regtech 28:329    2
3   Buckley RP 3:185                fintech 12:249    1
4  Barberis JN 2:161                regtech 28:329    1
5   Butler T/1 2:041                regtech 28:329    2
6   Butler T/1 2:041                fintech 12:249    2
7   Butler T/1 2:041             regulation 05:164    1
8     Hamdan A 2:018  regulatory technology 07:037    2


"""
from dataclasses import dataclass

from .... import chatgpt, techminer
from ...._items2counters import items2counters
from ...._load_stopwords import load_stopwords
from ...._read_records import read_records


@dataclass(init=False)
class _MatrixListResult:
    matrix_list_: None
    prompt_: None
    metric_: None
    criterion_for_columns_: None
    criterion_for_rows_: None


def occ_matrix_list(
    criterion_for_columns,
    criterion_for_rows,
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
    results = _MatrixListResult()

    results.criterion_for_columns_ = criterion_for_columns
    results.criterion_for_rows_ = criterion_for_rows
    results.metric_ = "OCC"
    results.matrix_list_ = _make_matrix_list(
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

    results.prompt_ = chatgpt.generate_prompt_for_matrix_list(results)

    return results


def _make_matrix_list(
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
    matrix_list = _create_matrix_list(
        column=criterion_for_columns,
        row=criterion_for_rows,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    matrix_list = _remove_stopwords(directory, matrix_list)

    matrix_list = _select_topics_by_occ_and_citations_and_topic_length(
        matrix_list=matrix_list,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        topics_length=topics_length,
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    for criterion, name in [
        (criterion_for_columns, "column"),
        (criterion_for_rows, "row"),
    ]:
        matrix_list = _add_counters_to_items(
            column=criterion,
            name=name,
            directory=directory,
            database=database,
            matrix_list=matrix_list,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

    matrix_list = _sort_matrix_list(matrix_list)

    matrix_list = matrix_list.reset_index(drop=True)

    return matrix_list


def _add_counters_to_items(
    column,
    name,
    directory,
    database,
    matrix_list,
    start_year,
    end_year,
    **filters,
):
    new_column_names = items2counters(
        column=column,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    matrix_list[name] = matrix_list[name].map(new_column_names)
    return matrix_list


def _sort_matrix_list(matrix_list):
    matrix_list = matrix_list.copy()

    for col in ["row", "column"]:
        col_upper = col.upper()
        matrix_list[col_upper] = matrix_list[col]
        matrix_list[col_upper] = matrix_list[col_upper].str.split()
        matrix_list[col_upper] = matrix_list[col_upper].map(lambda x: x[-1])

    matrix_list = matrix_list.sort_values(
        ["ROW", "row", "COLUMN", "column"], ascending=[False, True, False, True]
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
            directory=directory,
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
            indicators = indicators[indicators.global_citations >= topic_min_citations]
        if topic_max_citations is not None:
            indicators = indicators[indicators.global_citations <= topic_max_citations]

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


def _create_matrix_list(
    column,
    row,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    records = read_records(
        directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = records[[column]].copy()
    matrix_list = matrix_list.rename(columns={column: "column"})
    matrix_list = matrix_list.assign(row=records[[row]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    return matrix_list
