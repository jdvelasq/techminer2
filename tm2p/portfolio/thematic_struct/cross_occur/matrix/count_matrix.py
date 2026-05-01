"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.cross_occurrence.matrix import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COLUMNS:
    ...     .with_column_analysis_unit(AnalysisUnit.AUTHKW)
    ...     .having_column_units_in_top(10)
    ...     .having_column_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_column_unit_occurrence_between(None, None)
    ...     .having_column_unit_citation_between(None, None)
    ...     .having_column_units_in(None)
    ...     #
    ...     # ROWS:
    ...     .with_index_analysis_unit(AnalysisUnit.AUTH)
    ...     .having_index_units_in_top(None)
    ...     .having_index_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_index_unit_occurrence_between(2, None)
    ...     .having_index_unit_citation_between(None, None)
    ...     .having_index_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> df.head(10)
    columns                        fintech 117:25478  ...  financial services 007:01673
    rows                                              ...
    Julapa A. Jagtiani 005:01156                   5  ...                             0
    Douglas W. Arner 003:00911                     2  ...                             0
    Lars Hornuf 003:00904                          3  ...                             0
    Janos N. Barberis 003:00445                    1  ...                             0
    Gerhard Schwabe 003:00330                      3  ...                             0
    Liudmila Zavolokina 003:00330                  3  ...                             0
    Mateusz Dolata 003:00330                       3  ...                             0
    Peter Gomber 002:02579                         1  ...                             0
    Robert J. Kauffman 002:01445                   0  ...                             0
    Victor Murinde 002:01022                       1  ...                             0
    <BLANKLINE>
    [10 rows x 10 columns]



    >>> from tm2p.portfolio.thematic_struct.cross_occurrence.matrix import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COLUMNS:
    ...     .with_column_analysis_unit(AnalysisUnit.AUTHKW)
    ...     .having_column_units_in_top(10)
    ...     .having_column_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_column_unit_occurrence_between(None, None)
    ...     .having_column_unit_citation_between(None, None)
    ...     .having_column_units_in(None)
    ...     #
    ...     # ROWS:
    ...     .with_index_analysis_unit(AnalysisUnit.AUTH)
    ...     .having_index_units_in_top(10)
    ...     .having_index_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_index_unit_occurrence_between(None, None)
    ...     .having_index_unit_citation_between(None, None)
    ...     .having_index_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(
    ...         {
    ...             Field.AUTHKW_RAW: ["fintech", "innovation", "financial services"],
    ...         },
    ...     )
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> df.head(10)
                         fintech  financial inclusion  ...  financial services  regtech
    Julapa A. Jagtiani         5                    0  ...                   0        1
    Lars Hornuf                3                    0  ...                   0        0
    Gerhard Schwabe            3                    0  ...                   0        0
    Liudmila Zavolokina        3                    0  ...                   0        0
    Mateusz Dolata             3                    0  ...                   0        0
    Chichuan Lee               2                    0  ...                   0        0
    Chinhsien Yu               2                    0  ...                   0        0
    Jinsong Zhao               2                    0  ...                   0        0
    Huaping Sun                2                    0  ...                   0        1
    Linnan Yan                 2                    0  ...                   0        1
    <BLANKLINE>
    [10 rows x 10 columns]



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field
from tm2p.portfolio.perform_metr.unit import Metrics


class CountMatrix(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_compute_column_peformance_metrics(self):
        metrics = (
            Metrics()
            .update(**self.params.__dict__)
            #
            .with_analysis_unit(self.params.column_analysis_unit)
            #
            .having_top_n_units(self.params.top_n_column_units)
            .having_units_ordered_by(self.params.column_unit_order_by)
            .having_unit_occurrence_between(
                self.params.column_unit_occurrence_range[0],
                self.params.column_unit_occurrence_range[1],
            )
            .having_unit_global_citation_between(
                self.params.column_unit_citation_range[0],
                self.params.column_unit_citation_range[1],
            )
            .having_units_in(self.params.column_units_in)
            #
            .run()
        )
        return metrics

    # -------------------------------------------------------------------------
    def _step_02_compute_row_peformance_metrics(self):
        metrics = (
            Metrics()
            .update(**self.params.__dict__)
            .with_analysis_unit(self.params.index_analysis_unit)
            .having_top_n_units(self.params.top_n_index_units)
            .having_units_ordered_by(self.params.index_item_order_by)
            .having_unit_occurrence_between(
                self.params.index_unit_occurrence_range[0],
                self.params.index_unit_occurrence_range[1],
            )
            .having_unit_global_citation_between(
                self.params.index_unit_citation_range[0],
                self.params.index_unit_citation_range[1],
            )
            .having_units_in(self.params.index_units_in)
            .run()
        )
        return metrics

    # -------------------------------------------------------------------------
    def _step_03_load_the_database(self):
        return load_filtered_main_csv_zip(params=self.params)

    # -------------------------------------------------------------------------
    def _step_04_create_raw_matrix_list(self, records):
        #
        columns = self.params.column_analysis_unit.value
        rows = self.params.index_analysis_unit.value
        #
        raw_matrix_list = records[[columns]].copy()
        raw_matrix_list = raw_matrix_list.rename(columns={columns: "columns"})
        raw_matrix_list = raw_matrix_list.assign(rows=records[[rows]])
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_05_explode_matrix_list(self, raw_matrix_list, name, selected_terms):
        #
        raw_matrix_list[name] = raw_matrix_list[name].str.split(";")
        raw_matrix_list = raw_matrix_list.explode(name)
        raw_matrix_list[name] = raw_matrix_list[name].str.strip()
        raw_matrix_list = raw_matrix_list[raw_matrix_list[name].isin(selected_terms)]
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_06_compute_occurrences(self, raw_matrix_list):
        #
        raw_matrix_list["OCC"] = 1
        raw_matrix_list = raw_matrix_list.groupby(
            ["rows", "columns"], as_index=False
        ).aggregate("sum")
        #
        raw_matrix_list = raw_matrix_list.sort_values(
            ["OCC", "rows", "columns"], ascending=[False, True, True]
        )
        raw_matrix_list = raw_matrix_list.reset_index(drop=True)
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_07_build_mapping(self, dataframe):

        from tm2p._intern.helpers.get_zero_digit import get_zero_digits

        GCS = Field.GCS.value

        dataframe["counters"] = dataframe.index.astype(str)

        occ_digits, gcs_digits = get_zero_digits(self.params.root_directory)

        dataframe["counters"] += " " + dataframe["OCC"].map(
            lambda x: f"{x:0{occ_digits}d}"
        )

        dataframe["counters"] += ":" + dataframe[GCS].map(
            lambda x: f"{x:0{gcs_digits}d}"
        )

        mapping = dataframe["counters"].to_dict()

        return mapping

    # -------------------------------------------------------------------------
    def _step_08_rename_terms(self, raw_matrix_list, row_mapping, column_mapping):
        #
        raw_matrix_list["rows"] = raw_matrix_list["rows"].map(row_mapping)
        raw_matrix_list["columns"] = raw_matrix_list["columns"].map(column_mapping)
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_09_pivot_matrix_list(self, matrix_list):
        matrix = matrix_list.pivot(
            index=matrix_list.columns[0],
            columns=matrix_list.columns[1],
            values=matrix_list.columns[2],
        )
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)
        return matrix

    # -------------------------------------------------------------------------
    def _step_10_check_terms(self, matrix, row_mapping, col_mapping):

        for _, value in row_mapping.items():
            if value not in matrix.index:
                matrix.loc[value] = 0

        for _, value in col_mapping.items():
            if value not in matrix.columns:
                matrix[value] = 0

        return matrix

    # -------------------------------------------------------------------------
    def _step_11_sort_matrix_axis(self, matrix):
        matrix_cols = matrix.columns.tolist()
        matrix_rows = matrix.index.tolist()
        matrix_cols = sorted(matrix_cols, key=lambda x: x.split()[-1], reverse=True)
        matrix_rows = sorted(matrix_rows, key=lambda x: x.split()[-1], reverse=True)
        matrix = matrix[matrix_cols]
        matrix = matrix.loc[matrix_rows]
        return matrix

    # -------------------------------------------------------------------------
    def _step_12_remove_counters(self, matrix):
        if self.params.use_counters is False:
            matrix_cols = [" ".join(col.split()[:-1]) for col in matrix.columns]
            matrix_rows = [" ".join(row.split()[:-1]) for row in matrix.index]
            matrix.columns = matrix_cols
            matrix.index = matrix_rows
        return matrix

    # -------------------------------------------------------------------------
    def _step_13_apply_co_occurrence_threshold(self, matrix):
        matrix = matrix.where(matrix >= self.params.minimum_pair_co_occurrence, other=0)
        return matrix

    # -------------------------------------------------------------------------
    def run(self):

        col_metrics = self._step_01_compute_column_peformance_metrics()
        row_metrics = self._step_02_compute_row_peformance_metrics()

        records = self._step_03_load_the_database()

        matrix_list = self._step_04_create_raw_matrix_list(records)
        matrix_list = self._step_05_explode_matrix_list(
            matrix_list,
            "columns",
            col_metrics.index.tolist(),
        )
        matrix_list = self._step_05_explode_matrix_list(
            matrix_list,
            "rows",
            row_metrics.index.tolist(),
        )

        matrix_list = self._step_06_compute_occurrences(matrix_list)

        row_mapping = self._step_07_build_mapping(row_metrics)
        col_mapping = self._step_07_build_mapping(col_metrics)

        matrix_list = self._step_08_rename_terms(matrix_list, row_mapping, col_mapping)

        matrix = self._step_09_pivot_matrix_list(matrix_list)
        matrix = self._step_10_check_terms(matrix, row_mapping, col_mapping)
        matrix = self._step_11_sort_matrix_axis(matrix)
        matrix = self._step_12_remove_counters(matrix)
        matrix = self._step_13_apply_co_occurrence_threshold(matrix)

        return matrix
