# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cross co-occurrence DataFrame 
===============================================================================


## >>> from techminer2.analyze.cross_co_occurrence import CrossCoOccurrenceDataFrame
## >>> (
## ...     CrossCoOccurrenceDataFrame()
## ...     .set_columns_params(
## ...         field="author_keywords",
## ...         top_n=10,
## ...         occ_range=(2, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_rows_params(
## ...         field="authors",
## ...         top_n=None,
## ...         occ_range=(2, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_output_params(
## ...         retain_counters=True,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... ).head(10)
                 rows                      columns  OCC
0    Dolata M. 2:0181              FINTECH 31:5168    2
1    Dolata M. 2:0181           INNOVATION 07:0911    2
2       Gai K. 2:0323       CYBER_SECURITY 02:0342    1
3       Gai K. 2:0323              FINTECH 31:5168    2
4    Gomber P. 2:1065              FINTECH 31:5168    1
5    Hornuf L. 2:0358         CROWDFUNDING 03:0335    1
6    Hornuf L. 2:0358              FINTECH 31:5168    2
7  Jagtiani J. 3:0317              FINTECH 31:5168    3
8  Jagtiani J. 3:0317  MARKETPLACE_LENDING 03:0317    3
9   Lemieux C. 2:0253              FINTECH 31:5168    2


"""
from ...database.load.load__filtered_database import load__filtered_database
from ...internals.mt.mt_calculate_global_performance_metrics import (
    _mt_calculate_global_performance_metrics,
)
from ...internals.mt.mt_extract_top_n_terms_by_metric import (
    _mt_extract_top_n_terms_by_metric,
)
from ...internals.mt.mt_sort_records_by_metric import _mt_sort_records_by_metric
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams
from ...internals.stopwords.load_user_stopwords import load_user_stopwords
from ...internals.utils.utils_compute_occurrences_and_citations import (
    _utils_compute_occurrences_and_citations,
)
from .internals.output_params import OutputParams, OutputParamsMixin


class CrossCoOccurrenceDataFrame(
    ColumnsAndRowsParamsMixin,
    DatabaseParamsMixin,
    OutputParamsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.columns_params = ItemParams()
        self.database_params = DatabaseParams()
        self.rows_params = ItemParams()
        self.output_params = OutputParams()

    def build(self):

        def filter_terms(
            #
            # MATRIX PARAMS:
            raw_matrix_list,
            name,
            #
            # TERM PARAMS:
            field,
            top_n,
            occ_range,
            gc_range,
            custom_terms,
        ):
            if custom_terms is None:
                indicators = _mt_calculate_global_performance_metrics(
                    field=field,
                    **self.database_params.__dict__,
                )

                indicators = _mt_sort_records_by_metric(indicators, "OCC")

                custom_terms = _mt_extract_top_n_terms_by_metric(
                    indicators=indicators,
                    metric="OCC",
                    top_n=top_n,
                    occ_range=occ_range,
                    gc_range=gc_range,
                )

            raw_matrix_list = raw_matrix_list[raw_matrix_list[name].isin(custom_terms)]

            return raw_matrix_list

        #
        # MAIN CODE:
        #
        if self.rows_params.field is None:
            for key, value in self.columns_params.__dict__.items():
                setattr(self.rows_params, key, value)

        records = load__filtered_database(**self.database_params.__dict__)

        columns = self.columns_params.field
        rows = self.rows_params.field
        root_dir = self.database_params.root_dir

        raw_matrix_list = records[[columns]].copy()
        raw_matrix_list = raw_matrix_list.rename(columns={columns: "column"})
        raw_matrix_list = raw_matrix_list.assign(row=records[[rows]])

        stopwords = load_user_stopwords(root_dir=root_dir)

        for name in ["column", "row"]:
            raw_matrix_list[name] = raw_matrix_list[name].str.split(";")
            raw_matrix_list = raw_matrix_list.explode(name)
            raw_matrix_list[name] = raw_matrix_list[name].str.strip()
            raw_matrix_list = raw_matrix_list[~raw_matrix_list[name].isin(stopwords)]

        raw_matrix_list["OCC"] = 1
        raw_matrix_list = raw_matrix_list.groupby(
            ["row", "column"], as_index=False
        ).aggregate("sum")

        raw_matrix_list = raw_matrix_list.sort_values(
            ["OCC", "row", "column"], ascending=[False, True, True]
        )

        # Filters the terms in the 'row' column of the matrix list
        raw_filterd_matrix_list = filter_terms(
            raw_matrix_list=raw_matrix_list,
            name="row",
            **self.rows_params.__dict__,
        )

        # Filters the terms in the 'column' column of the matrix list
        filtered_matrix_list = filter_terms(
            raw_matrix_list=raw_filterd_matrix_list,
            name="column",
            #
            # COL PARAMS:
            **self.columns_params.__dict__,
        )

        # Assign counters to column 'row'
        if self.output_params.retain_counters:

            rows_map = _utils_compute_occurrences_and_citations(
                criterion=self.rows_params.field,
                **self.database_params.__dict__,
            )
            filtered_matrix_list.loc[:, "row"] = filtered_matrix_list["row"].map(
                rows_map
            )

            columns_map = _utils_compute_occurrences_and_citations(
                criterion=self.columns_params.field,
                **self.database_params.__dict__,
            )
            filtered_matrix_list.loc[:, "column"] = filtered_matrix_list["column"].map(
                columns_map
            )

        filtered_matrix_list = filtered_matrix_list.reset_index(drop=True)
        filtered_matrix_list = filtered_matrix_list.rename(
            columns={"row": "rows", "column": "columns"}
        )
        filtered_matrix_list = filtered_matrix_list.sort_values(
            ["rows", "columns", "OCC"], ascending=[True, True, False]
        )
        filtered_matrix_list = filtered_matrix_list.reset_index(drop=True)

        return filtered_matrix_list
