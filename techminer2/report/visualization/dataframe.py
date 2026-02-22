"""
Data Frame
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2 import CorpusField
    >>> from techminer2.report.visualization import DataFrame
    >>> df = (
    ...     DataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df  # doctest: +SKIP
                           rank_occ  ...                       counters
    AUTH_KEY_NORM                    ...
    fintech                       1  ...                fintech 14:1031
    innovation                    2  ...             innovation 03:0673
    technology                    3  ...             technology 03:0643
    content analysis              4  ...       content analysis 02:0279
    digitalization                5  ...         digitalization 02:0279
    popular press                 6  ...          popular press 02:0279
    financial technology          7  ...   financial technology 02:0019
    banking                       8  ...                banking 01:0394
    financial institution         9  ...  financial institution 01:0394
    financial services           10  ...     financial services 01:0394
    <BLANKLINE>
    [10 rows x 17 columns]


"""

import pandas as pd  # type: ignore

from techminer2 import CorpusField, ItemsOrderBy
from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_filtered_main_data

SELECTED_COLUMNS = {
    ItemsOrderBy.OCC.value: [
        ItemsOrderBy.OCC.value,
        CorpusField.CIT_COUNT_GLOBAL.value,
        CorpusField.CIT_COUNT_LOCAL.value,
        "_name_",
    ],
    #
    CorpusField.CIT_COUNT_GLOBAL.value: [
        CorpusField.CIT_COUNT_GLOBAL.value,
        CorpusField.CIT_COUNT_LOCAL.value,
        ItemsOrderBy.OCC.value,
        "_name_",
    ],
    # -------------------------------------------
    CorpusField.CIT_COUNT_LOCAL.value: [
        CorpusField.CIT_COUNT_LOCAL.value,
        CorpusField.CIT_COUNT_GLOBAL.value,
        ItemsOrderBy.OCC.value,
        "_name_",
    ],
}


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_load_filtered_main_data(self) -> pd.DataFrame:

        df = load_filtered_main_data(params=self.params)
        df = (
            df[
                [
                    self.params.source_field.value,
                    CorpusField.CIT_COUNT_GLOBAL.value,
                    CorpusField.CIT_COUNT_LOCAL.value,
                    CorpusField.PUBYEAR.value,
                ]
            ]
            .dropna()
            .copy()
        )

        return df

    # -------------------------------------------------------------------------
    def step_02_explode_source_field(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()
        source_field = self.params.source_field.value
        df[source_field] = df[source_field].str.split("; ")
        df = df.explode(source_field)

        return df

    # -------------------------------------------------------------------------
    def step_03_compute_primary_performance_metrics(self, df):

        source_field = self.params.source_field.value
        cit_count_global = CorpusField.CIT_COUNT_GLOBAL.value
        cit_count_local = CorpusField.CIT_COUNT_LOCAL.value
        pubyear = CorpusField.PUBYEAR.value

        df = df.sort_values(
            [
                source_field,
                cit_count_global,
                cit_count_local,
            ],
            ascending=[
                True,
                False,
                False,
            ],
        )

        df = df.assign(position=df.groupby(source_field).cumcount() + 1)
        df = df.assign(position2=df.position.map(lambda w: w * w))
        df = df.reset_index(drop=True)

        df["OCC"] = 1
        grouped_df = df.groupby(source_field).agg(
            {
                "OCC": "sum",
                cit_count_global: "sum",
                cit_count_local: "sum",
                pubyear: "min",
            }
        )
        grouped_df = grouped_df.rename(columns={pubyear: "first_publication_year"})
        grouped_df["last_year"] = df[pubyear].max()

        return df, grouped_df

    # -------------------------------------------------------------------------
    def step_04_compute_derived_performance_metrics(self, grouped_df):

        cit_count_global = CorpusField.CIT_COUNT_GLOBAL.value
        cit_count_local = CorpusField.CIT_COUNT_LOCAL.value
        occ = ItemsOrderBy.OCC.value

        grouped_df = grouped_df.copy()
        grouped_df["age"] = (
            grouped_df["last_year"] - grouped_df["first_publication_year"] + 1
        )
        grouped_df["global_citations_per_year"] = (
            grouped_df[cit_count_global] / grouped_df["age"]
        )
        grouped_df["local_citations_per_year"] = (
            grouped_df[cit_count_local] / grouped_df["age"]
        )

        grouped_df["global_citations_per_document"] = (
            grouped_df[cit_count_global] / grouped_df[occ]
        )
        grouped_df["local_citations_per_document"] = (
            grouped_df[cit_count_local] / grouped_df[occ]
        )
        return grouped_df

    # -------------------------------------------------------------------------
    def step_05_compute_impact_metrics(self, df, grouped_df):

        source_field = self.params.source_field.value
        cit_count_global = CorpusField.CIT_COUNT_GLOBAL.value
        # cit_count_local = CorpusField.CIT_COUNT_LOCAL.value

        df = df.copy()
        grouped_df = grouped_df.copy()

        # H-index
        h_indexes = df.query(f"{cit_count_global} >= position")
        h_indexes = h_indexes.groupby(source_field, as_index=True).agg(
            {"position": "max"}
        )
        h_indexes = h_indexes.rename(columns={"position": "h_index"})
        grouped_df.loc[h_indexes.index, "h_index"] = h_indexes.astype(int)
        grouped_df["h_index"] = grouped_df["h_index"].fillna(0)

        # G-index
        g_indexes = df.query(f"{cit_count_global} >= position2")
        g_indexes = g_indexes.groupby(source_field, as_index=True).agg(
            {"position": "max"}
        )
        g_indexes = g_indexes.rename(columns={"position": "g_index"})
        grouped_df.loc[g_indexes.index, "g_index"] = g_indexes.astype(int)
        grouped_df["g_index"] = grouped_df["g_index"].fillna(0)

        # M-index
        grouped_df = grouped_df.assign(m_index=grouped_df.h_index / grouped_df.age)
        grouped_df["m_index"] = grouped_df.m_index.round(decimals=2)

        return grouped_df

    # -------------------------------------------------------------------------
    def sort_data_frame_by_metric(self, df, metric):

        df = df.copy()
        df["_name_"] = df.index.tolist()

        columns = SELECTED_COLUMNS[metric]
        ascending = [False] * (len(columns) - 1) + [True]

        df = df.sort_values(columns, ascending=ascending)
        df = df.drop(columns=["_name_"])

        return df

    # -------------------------------------------------------------------------
    def step_06_add_rank_columns(self, grouped_df):

        cit_count_global = CorpusField.CIT_COUNT_GLOBAL.value
        cit_count_local = CorpusField.CIT_COUNT_LOCAL.value
        occ = ItemsOrderBy.OCC.value

        grouped_df = grouped_df.copy()

        grouped_df = self.sort_data_frame_by_metric(grouped_df, cit_count_local)
        grouped_df.insert(0, "rank_lcs", range(1, len(grouped_df) + 1))

        grouped_df = self.sort_data_frame_by_metric(grouped_df, cit_count_global)
        grouped_df.insert(0, "rank_gcs", range(1, len(grouped_df) + 1))

        grouped_df = self.sort_data_frame_by_metric(grouped_df, occ)
        grouped_df.insert(0, "rank_occ", range(1, len(grouped_df) + 1))

        return grouped_df

    # -------------------------------------------------------------------------
    def step_07_filter_by_term_occurrences_range(self, grouped_df):

        occ = ItemsOrderBy.OCC.value

        grouped_df = grouped_df.copy()

        if self.params.item_occurrences_range is None:
            return grouped_df

        min_value, max_value = self.params.item_occurrences_range

        if min_value is not None:
            grouped_df = grouped_df[grouped_df[occ] >= min_value]
        if max_value is not None:
            grouped_df = grouped_df[grouped_df[occ] <= max_value]

        return grouped_df

    # -------------------------------------------------------------------------
    def step_08_filter_by_term_citations_range(self, grouped_df):

        cit_count_global = CorpusField.CIT_COUNT_GLOBAL.value
        # cit_count_local = CorpusField.CIT_COUNT_LOCAL.value

        grouped_df = grouped_df.copy()

        if self.params.item_citations_range is None:
            return grouped_df

        min_value, max_value = self.params.item_citations_range

        if min_value is not None:
            grouped_df = grouped_df[grouped_df[cit_count_global] >= min_value]
        if max_value is not None:
            grouped_df = grouped_df[grouped_df[cit_count_global] <= max_value]

        return grouped_df

    # -------------------------------------------------------------------------
    def step_09_filter_by_terms_in(self, grouped_df):

        grouped_df = grouped_df.copy()

        if self.params.items_in is None:
            return grouped_df

        if self.params.items_in is not None:
            #
            terms_in = [t for t in self.params.items_in if t in grouped_df.index]
            #
            grouped_df = grouped_df.loc[terms_in, :]

        return grouped_df

    # -------------------------------------------------------------------------
    def step_10_filter_by_top_n_terms(self, grouped_df):

        grouped_df = self.sort_data_frame_by_metric(
            df=grouped_df.copy(),
            metric=self.params.items_order_by.value,
        )

        if self.params.top_n is not None:
            grouped_df = grouped_df.head(self.params.top_n)

        return grouped_df

    # -------------------------------------------------------------------------
    def step_11_check_field_types(self, grouped_df):

        grouped_df = grouped_df.copy()

        if "OCC" in grouped_df.columns:
            grouped_df["OCC"] = grouped_df["OCC"].astype(int)

        if CorpusField.CIT_COUNT_GLOBAL.value in grouped_df.columns:
            grouped_df[CorpusField.CIT_COUNT_GLOBAL.value] = grouped_df[
                CorpusField.CIT_COUNT_GLOBAL.value
            ].astype(int)

        if CorpusField.CIT_COUNT_LOCAL.value in grouped_df.columns:
            grouped_df[CorpusField.CIT_COUNT_LOCAL.value] = grouped_df[
                CorpusField.CIT_COUNT_LOCAL.value
            ].astype(int)

        if "h_index" in grouped_df.columns:
            grouped_df["h_index"] = grouped_df["h_index"].astype(int)

        if "g_index" in grouped_df.columns:
            grouped_df["g_index"] = grouped_df["g_index"].astype(int)

        return grouped_df

    # -------------------------------------------------------------------------
    def step_12_add_term_with_counters_column(self, grouped_df):

        cit_count_global = CorpusField.CIT_COUNT_GLOBAL.value
        # cit_count_local = CorpusField.CIT_COUNT_LOCAL.value
        occ = ItemsOrderBy.OCC.value

        grouped_df = grouped_df.copy()
        grouped_df["counters"] = grouped_df.index.astype(str)

        n_zeros_occ = len(str(grouped_df[occ].max()))
        grouped_df["counters"] += " " + grouped_df[occ].map(
            lambda x: f"{x:0{n_zeros_occ}d}"
        )

        n_zeros_citations = len(str(grouped_df[cit_count_global].max()))
        grouped_df["counters"] += ":" + grouped_df[cit_count_global].map(
            lambda x: f"{x:0{n_zeros_citations}d}"
        )

        return grouped_df

    # -------------------------------------------------------------------------
    def run(self):

        df = self.step_01_load_filtered_main_data()
        df = self.step_02_explode_source_field(df)
        df, grouped_df = self.step_03_compute_primary_performance_metrics(df)
        grouped_df = self.step_04_compute_derived_performance_metrics(grouped_df)
        grouped_df = self.step_05_compute_impact_metrics(df, grouped_df)
        grouped_df = self.step_06_add_rank_columns(grouped_df)
        grouped_df = self.step_07_filter_by_term_occurrences_range(grouped_df)
        grouped_df = self.step_08_filter_by_term_citations_range(grouped_df)
        grouped_df = self.step_09_filter_by_terms_in(grouped_df)
        grouped_df = self.step_10_filter_by_top_n_terms(grouped_df)
        grouped_df = self.step_11_check_field_types(grouped_df)
        grouped_df = self.step_12_add_term_with_counters_column(grouped_df)

        return grouped_df


#
