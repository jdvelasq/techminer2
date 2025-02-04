# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Data Frame
===============================================================================


>>> from techminer2.database.metrics.tfidf import DataFrame
>>> (
...     DataFrame()
...     #
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # TFIDF:
...     .using_binary_term_frequencies(False)
...     .using_row_normalization(None)
...     .using_idf_reweighting(False)
...     .using_idf_weights_smoothing(False)
...     .using_sublinear_tf_scaling(False)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
author_keywords                                 FINTECH 31:5168  ...  CASE_STUDY 2:340
record_id                                                        ...                  
Anagnostopoulos I., 2018, J ECON BUS, V100, P7                1  ...                 0
Anshari M., 2019, ENERGY PROCEDIA, V156, P234                 0  ...                 0
Buchak G., 2018, J FINANC ECON, V130, P453                    1  ...                 0
Cai C.W., 2018, ACCOUNT FINANC, V58, P965                     1  ...                 0
Chen L./1, 2016, CHINA ECON J, V9, P225                       1  ...                 0
<BLANKLINE>
[5 rows x 10 columns]




"""
import pandas as pd  # type: ignore
from sklearn.feature_extraction.text import TfidfTransformer  # type: ignore

from ....internals.mixins import InputFunctionsMixin, SortAxesMixin
from ...load import DatabaseLoader
from ..performance.data_frame import DataFrame as PerformanceMetricsDataFrame


class DataFrame(
    InputFunctionsMixin,
    SortAxesMixin,
):
    """:meta private:"""

    def _step_1_load_the_database(self):
        return DatabaseLoader().update_params(**self.params.__dict__).build()

    def step_2_explode_data_frame(self, data_frame):

        field = self.params.field

        data_frame = data_frame.reset_index()
        data_frame = data_frame[[field, "record_id", "global_citations"]].copy()
        data_frame = data_frame.dropna()
        data_frame["OCC"] = 1
        data_frame[field] = data_frame[field].str.split(";")
        data_frame = data_frame.explode(field)
        data_frame[field] = data_frame[field].str.strip()

        return data_frame

    def step_3_get_terms_mapping(self, data_frame):

        field = self.params.field

        data_frame = data_frame[[field, "global_citations", "OCC"]].copy()
        data_frame = data_frame.groupby(field).agg(
            {"OCC": "sum", "global_citations": "sum"}
        )

        data_frame["counters"] = data_frame.index.astype(str)

        n_zeros = len(str(data_frame["OCC"].max()))
        data_frame["counters"] += " " + data_frame["OCC"].map(
            lambda x: f"{x:0{n_zeros}d}"
        )

        n_zeros = len(str(data_frame["global_citations"].max()))
        data_frame["counters"] += ":" + data_frame["global_citations"].map(
            lambda x: f"{x:0{n_zeros}d}"
        )

        mapping = data_frame["counters"].to_dict()

        return mapping

    def step_4_create_df_matrix(self, data_frame):

        field = self.params.field

        data_frame = data_frame[[field, "record_id", "OCC"]].copy()
        data_frame = data_frame.dropna()

        grouped = data_frame.groupby(["record_id", field], as_index=False).agg(
            {"OCC": "sum"}
        )

        matrix = pd.pivot(
            index="record_id",
            data=grouped,
            columns=field,
            values="OCC",
        )
        matrix = matrix.fillna(0)

        if self.params.binary_term_frequencies is True:
            matrix = matrix.map(lambda w: 1 if w > 0 else 0)

        return matrix

    def step_5_filter_terms_in_df_matrix(self, matrix):
        performance_metrics = (
            PerformanceMetricsDataFrame().update_params(**self.params.__dict__).build()
        )
        selected_terms = performance_metrics.index.tolist()
        matrix = matrix[selected_terms]
        return matrix

    def step_6_remove_rows_of_zeros(self, df_matrix):
        df_matrix = df_matrix.loc[(df_matrix != 0).any(axis=1)]
        return df_matrix

    def step_7_apply_tfidf_transformations(self, matrix):

        norm = self.params.row_normalization
        use_idf = self.params.use_idf
        smooth_idf = self.params.smooth_idf_weights
        sublinear_tf = self.params.sublinear_tf_scaling

        if norm is not None or use_idf or smooth_idf or sublinear_tf:

            transformer = TfidfTransformer(
                norm=norm,
                use_idf=use_idf,
                smooth_idf=smooth_idf,
                sublinear_tf=sublinear_tf,
            )
            matrix = transformer.fit_transform(matrix)
        else:
            matrix = matrix.astype(int)

        return matrix

    def step_8_append_counters_to_axis(self, data_frame, mapping):
        data_frame.columns = data_frame.columns.map(mapping)
        return data_frame

    def step_9_sort_columns(self, data_frame):
        return self.sort_columns(data_frame)

    def step_10_remove_counters_from_axes(self, data_frame):
        if self.params.term_counters is False:
            data_frame.columns = [" ".join(x.split()[:-1]) for x in data_frame.columns]
        return data_frame

    def build(self):

        data_frame = self._step_1_load_the_database()
        data_frame = self.step_2_explode_data_frame(data_frame)
        mapping = self.step_3_get_terms_mapping(data_frame)
        df_matrix = self.step_4_create_df_matrix(data_frame)
        df_matrix = self.step_5_filter_terms_in_df_matrix(df_matrix)
        df_matrix = self.step_6_remove_rows_of_zeros(df_matrix)
        df_matrix = self.step_7_apply_tfidf_transformations(df_matrix)
        df_matrix = self.step_8_append_counters_to_axis(df_matrix, mapping)
        df_matrix = self.step_9_sort_columns(df_matrix)
        df_matrix = self.step_10_remove_counters_from_axes(df_matrix)

        return df_matrix
