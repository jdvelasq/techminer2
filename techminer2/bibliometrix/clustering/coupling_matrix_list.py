"""
Coupling Matrix List
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> bibliometrix.clustering.coupling_matrix_list(
...     unit_of_analysis='article',
...     coupling_measured_by='global_references',
...     topics_length=15,
...     metric='local_citations',
...     directory=directory,
... ).matrix_list_.head()
                                                 row  ...  OCC
0  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...  142
1  Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37,...  ...   21
2       Baxter LG, 2016, DUKE LAW J, V66, P567 1:030  ...   49
3  Becker M, 2020, INTELL SYST ACCOUNT FIN MANAG,...  ...   47
4  Becker M, 2020, INTELL SYST ACCOUNT FIN MANAG,...  ...    1
<BLANKLINE>
[5 rows x 3 columns]


"""
from dataclasses import dataclass

from ...add_counters_to_items_in_table_column import (
    add_counters_to_items_in_table_column,
)
from ...record_utils import read_records

# from .records2documents import records2documents


# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name

#
# unit_of_analysis = {article, author, source, organization, country}
#
# coupling_measured_by = {references, author_keywords, index_keywords, abstract_words, title_words, words}
#


@dataclass(init=False)
class _MatrixList:
    matrix_list_: None
    prompt_: None
    metric_: None
    criterion_for_columns_: None
    criterion_for_rows_: None


def coupling_matrix_list(
    unit_of_analysis,
    coupling_measured_by,
    metric="local_citations",
    topics_length=250,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Coupling matrix list."""

    def check_unit_of_analysis(unit_of_analysis):
        if unit_of_analysis not in [
            "article",
            "author",
            "source",
            "organization",
            "country",
        ]:
            raise ValueError(
                "unit_of_analysis must be article, author, source, "
                "organization, or country"
            )

    def check_coupling_measured_by(coupling_measured_by):
        if coupling_measured_by not in [
            "global_references",
            "local_references",
            "author_keywords",
            "index_keywords",
            "keywords",
            "abstract_words",
            "title_words",
            "words",
        ]:
            raise ValueError(
                "coupling_measured_by must be global_references, "
                "local_references, author_keywords, "
                "index_keywords, abstract_words, title_words, or words"
            )

    def check_metric(metric):
        if metric not in ["local_citations", "global_citations"]:
            raise ValueError(
                "metric must be local_citations or global_citations"
            )

    def get_raw_records(
        unit_of_analysis,
        coupling_measured_by,
        directory,
        database,
        start_year,
        end_year,
        **filters,
    ):
        records = read_records(
            root_dir=directory,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )
        records = records[
            [
                unit_of_analysis,
                coupling_measured_by,
                "local_citations",
                "global_citations",
            ]
        ]
        records = records.dropna()
        return records

    def explode_column(records, column):
        records[column] = records[column].str.split(";")
        records = records.explode(column)
        records[column] = records[column].str.strip()
        return records

    def select_top_n_units_of_analysis(
        unit_of_analysis, coupling_measured_by, metric, topics_length, records
    ):
        records = records.groupby(unit_of_analysis, as_index=False).agg(
            {
                "local_citations": sum,
                "global_citations": sum,
                coupling_measured_by: list,
            }
        )

        if metric == "local_references":
            selected_columns = [
                "local_citations",
                "global_citations",
                unit_of_analysis,
            ]
        else:
            selected_columns = [
                "global_citations",
                "local_citations",
                unit_of_analysis,
            ]
        records = records.sort_values(
            selected_columns, ascending=[False, False, True]
        )
        records = records.head(topics_length)
        return records

    #
    # Main program:
    #

    # 1. Check input parameters
    check_unit_of_analysis(unit_of_analysis)
    check_coupling_measured_by(coupling_measured_by)
    check_metric(metric)

    # 2. Get raw records with columns: unit_of_analysis,
    #    coupling_measured_by, "local_citations", "global_citations",
    records = get_raw_records(
        unit_of_analysis,
        coupling_measured_by,
        directory,
        database,
        start_year,
        end_year,
        **filters,
    )

    # 3. Explode columns
    records = explode_column(records, unit_of_analysis)
    records = explode_column(records, coupling_measured_by)

    # 4. Select top n units of analysis
    records = select_top_n_units_of_analysis(
        unit_of_analysis, coupling_measured_by, metric, topics_length, records
    )

    records = records.explode(coupling_measured_by)
    records = records.groupby(coupling_measured_by, as_index=False).agg(
        {
            unit_of_analysis: list,
            "local_citations": sum,
            "global_citations": sum,
        }
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
    matrix_list = matrix_list.groupby(
        ["row", "column"], as_index=False
    ).aggregate("sum")

    for column_name in ["row", "column"]:
        matrix_list = add_counters_to_items_in_table_column(
            column=unit_of_analysis,
            name=column_name,
            directory=directory,
            database=database,
            table=matrix_list,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

    result = _MatrixList()
    result.matrix_list_ = matrix_list
    result.criterion_for_columns_ = unit_of_analysis
    result.criterion_for_rows_ = unit_of_analysis
    result.metric_ = "OCC"

    return result
