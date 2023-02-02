"""
Coupling Matrix List
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix__coupling_matrix_list
>>> bibliometrix__coupling_matrix_list(
...     criterion='article',
...     coupling_measured_by='local_references',
...     topics_length=15,
...     metric='local_references',
...     directory=directory,
... ).head()
                                                 row  ... OCC
0  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...  31
1  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   1
2  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   2
3  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   1
4  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   1
<BLANKLINE>
[5 rows x 3 columns]



"""
from ..._lib._read_records import read_records
from ...vantagepoint.analyze.matrix.co_occ_matrix_list import _add_counters_to_items

# from .records2documents import records2documents


# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name

#
# unit_of_analysis = {article, author, source, organization, country}
#
# coupling_measured_by = {references, author_keywords, index_keywords, abstract_words, title_words, words}
#


def bibliometrix__coupling_matrix_list(
    criterion,
    coupling_measured_by,
    topics_length=250,
    metric="local_citations",
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Coupling matrix list."""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    records = records[
        [
            criterion,
            coupling_measured_by,
            "local_citations",
            "global_citations",
        ]
    ]
    records = records.dropna()

    for col in [criterion, coupling_measured_by]:
        records[col] = records[col].str.split(";")
        records = records.explode(col)
        records[col] = records[col].str.strip()

    # Filter unit-of-analysis by metric
    records = records.groupby(criterion, as_index=False).agg(
        {
            "local_citations": sum,
            "global_citations": sum,
            coupling_measured_by: list,
        }
    )
    if metric == "local_references":
        selected_columns = ["local_citations", "global_citations", criterion]
    else:
        selected_columns = ["global_citations", "local_citations", criterion]
    records = records.sort_values(selected_columns, ascending=[False, False, True])
    records = records.head(topics_length)
    records = records.explode(coupling_measured_by)

    # Gruoup by
    records = records.groupby(coupling_measured_by, as_index=False).agg(
        {criterion: list, "local_citations": sum, "global_citations": sum}
    )
    records[criterion] = records[criterion].map(set)
    records[criterion] = records[criterion].map(sorted)
    records[criterion] = records[criterion].str.join("; ")

    # Compute co-occurrence matrix list
    matrix_list = records[[criterion]].copy()
    matrix_list = matrix_list.rename(columns={criterion: "column"})
    matrix_list = matrix_list.assign(row=records[[criterion]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    for column_name in ["row", "column"]:
        matrix_list = _add_counters_to_items(
            matrix_list=matrix_list,
            column_name=column_name,
            criterion=criterion,
            directory=directory,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

    return matrix_list
