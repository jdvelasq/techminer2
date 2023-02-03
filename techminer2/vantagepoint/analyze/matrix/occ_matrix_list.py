"""
Occurrence Matrix List
===============================================================================


>>> directory = "data/regtech/"

**Item selection by occurrence.**

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.occ_matrix_list(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topic_min_occ=2,
...    directory=directory,
... )
                   row                       column  OCC
0       Arner DW 3:185               regtech 28:329    2
1       Arner DW 3:185               fintech 12:249    1
2       Arner DW 3:185    financial services 04:168    1
3       Arner DW 3:185  financial regulation 04:035    2
4       Arner DW 3:185       data protection 02:027    1
..                 ...                          ...  ...
73  Lanfranchi D 2:002               finance 02:001    1
74  Lanfranchi D 2:002             reporting 02:001    1
75      Arman AA 2:000               regtech 28:329    2
76      Arman AA 2:000               suptech 03:004    1
77      Arman AA 2:000            technology 02:010    1
<BLANKLINE>
[78 rows x 3 columns]


**Seleccition of top terms.**

>>> vantagepoint.analyze.matrix.occ_matrix_list(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topics_length=5,
...    directory=directory,
... )
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
from ...._items2counters import items2counters
from ...._load_stopwords import load_stopwords
from ...._read_records import read_records
from ....techminer.indicators.indicators_by_topic import indicators_by_topic
from .co_occ_matrix_list import _sort_matrix_list


def occ_matrix_list(
    criterion_for_columns,
    criterion_for_rows,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a list of the cells of a co-occurrence matrix."""

    if criterion_for_rows == criterion_for_columns:
        raise ValueError("The criterion for row and column must be different.")

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
        topic_min_citations=topic_min_citations,
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


# def _select_top_n_items(top_n, matrix_list, column):

#     table = pd.DataFrame({"term": matrix_list[column].drop_duplicates()})
#     table["ranking"] = table.term.str.split()
#     table["ranking"] = table["ranking"].map(lambda x: x[-1])
#     table["name"] = table.term.str.split()
#     table["name"] = table["name"].map(lambda x: x[:-1])
#     table["name"] = table["name"].str.join(" ")
#     table = table.sort_values(["ranking", "name"], ascending=[False, True])
#     table = table.head(top_n)
#     terms = table.term.tolist()

#     matrix_list = matrix_list[matrix_list[column].isin(terms)]
#     return matrix_list


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


def _select_topics_by_occ_and_citations_and_topic_length(
    matrix_list,
    topic_min_occ,
    topic_min_citations,
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

        indicators = indicators_by_topic(
            criterion=criterion,
            directory=directory,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

        if topic_min_occ is not None:
            indicators = indicators[indicators.OCC >= topic_min_occ]
        if topic_min_citations is not None:
            indicators = indicators[indicators.global_citations >= topic_min_citations]

        indicators = indicators.sort_values(
            ["OCC", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )

        if topics_length is not None:
            indicators = indicators.head(topics_length)

        topics = indicators.index.to_list()

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
