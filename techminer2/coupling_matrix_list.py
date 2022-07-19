"""
Coupling Matrix List
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2.bibliometrix.clustering.coupling_matrix_list import coupling_matrix_list
>>> coupling_matrix_list(
...     unit_of_analysis='article',
...     coupling_measured_by='local_references',
...     top_n=15,
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
from ._read_records import read_records
from .co_occ_matrix_list import _add_counters_to_items

# from .records2documents import records2documents


# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name

#
# unit_of_analysis = {article, author, source, institution, country}
#
# coupling_measured_by = {references, author_keywords, index_keywords, abstract_words, title_words, words}
#


def coupling_matrix_list(
    unit_of_analysis,
    coupling_measured_by,
    top_n=250,
    metric="local_citations",
    directory="./",
):
    """Coupling matrix."""

    # if coupling_measured_by == "local_references":
    #     return _coupling_by_references(
    #         unit_of_analysis=unit_of_analysis,
    #         top_n=top_n,
    #         metric=metric,
    #         directory=directory,
    #     )
    # return _coupling_by_other_column()

    records = read_records(directory, database="documents", use_filter=True)
    records = records[
        [unit_of_analysis, coupling_measured_by, "local_citations", "global_citations"]
    ]
    records = records.dropna()

    for col in [unit_of_analysis, coupling_measured_by]:
        records[col] = records[col].str.split(";")
        records = records.explode(col)
        records[col] = records[col].str.strip()

    # Filter unit-of-analysis by metric
    records = records.groupby(unit_of_analysis, as_index=False).agg(
        {
            "local_citations": sum,
            "global_citations": sum,
            coupling_measured_by: list,
        }
    )
    if metric == "local_references":
        selected_columns = ["local_citations", "global_citations", unit_of_analysis]
    else:
        selected_columns = ["global_citations", "local_citations", unit_of_analysis]
    records = records.sort_values(selected_columns, ascending=[False, False, True])
    records = records.head(top_n)
    records = records.explode(coupling_measured_by)

    # Gruoup by
    records = records.groupby(coupling_measured_by, as_index=False).agg(
        {unit_of_analysis: list, "local_citations": sum, "global_citations": sum}
    )
    records[unit_of_analysis] = records[unit_of_analysis].map(set)
    records[unit_of_analysis] = records[unit_of_analysis].map(sorted)
    records[unit_of_analysis] = records[unit_of_analysis].str.join("; ")

    # Compute co-occurrence matrix list
    matrix_list = records[[unit_of_analysis]].copy()
    matrix_list = matrix_list.rename(columns={unit_of_analysis: "column"})
    matrix_list = matrix_list.assign(row=records[[unit_of_analysis]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    matrix_list = _add_counters_to_items(
        unit_of_analysis,
        "column",
        directory,
        "documents",
        matrix_list,
    )
    matrix_list = _add_counters_to_items(
        unit_of_analysis,
        "row",
        directory,
        "documents",
        matrix_list,
    )

    return matrix_list


# def _coupling_by_references(unit_of_analysis, top_n, metric, directory):

#     records = read_records(directory, database="documents", use_filter=True)
#     records = records[[unit_of_analysis, "local_references"]]

#     # Prepare: expands the coupling_measured_by -> references
#     records = records[records.local_references.notnull()]
#     records["local_references"] = records["local_references"].str.split(";")
#     records = records.explode("local_references")
#     records["local_references"] = records["local_references"].str.strip()

#     # Prepare: expands the unit_of_analysis
#     records[unit_of_analysis] = records[unit_of_analysis].str.split(";")
#     records = records.explode(unit_of_analysis)
#     records[unit_of_analysis] = records[unit_of_analysis].str.strip()

#     # Gruoup by references
#     records = records.groupby("local_references", as_index=False).agg(
#         {unit_of_analysis: list}
#     )
#     records[unit_of_analysis] = records[unit_of_analysis].map(set)
#     records[unit_of_analysis] = records[unit_of_analysis].map(sorted)
#     records[unit_of_analysis] = records[unit_of_analysis].str.join("; ")

#     # Filter by top references
#     selected_refs = read_records(directory, database="references", use_filter=False)
#     if metric == "local_references":
#         selected_columns = ["local_citations", "global_citations", "article"]
#     else:
#         selected_columns = ["global_citations", "local_citations", "article"]
#     selected_refs = selected_refs.sort_values(
#         selected_columns, ascending=[False, False, True]
#     )
#     selected_refs = selected_refs.article.head(top_n)
#     records = records[records.local_references.isin(selected_refs)]

#     # Compute matrix list
#     matrix_list = records[[unit_of_analysis]].copy()
#     matrix_list = matrix_list.rename(columns={unit_of_analysis: "column"})
#     matrix_list = matrix_list.assign(row=records[[unit_of_analysis]])

#     for name in ["column", "row"]:
#         matrix_list[name] = matrix_list[name].str.split(";")
#         matrix_list = matrix_list.explode(name)
#         matrix_list[name] = matrix_list[name].str.strip()

#     matrix_list["OCC"] = 1
#     matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
#         "sum"
#     )

#     matrix_list = _add_counters_to_items(
#         unit_of_analysis,
#         "column",
#         directory,
#         "documents",
#         matrix_list,
#     )
#     matrix_list = _add_counters_to_items(
#         unit_of_analysis,
#         "row",
#         directory,
#         "documents",
#         matrix_list,
#     )

#     return matrix_list


# def _coupling_by_other_column():
#     pass
