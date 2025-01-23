# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance Metrics DataFrame
===============================================================================

>>> from techminer2.database.metrics.performance_metrics import DataFrame
>>> (
...     DataFrame()
...     #
...     .with_source_field("author_keywords")
...     .select_top_n_terms(20)
...     .order_terms_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... ).head(10)
                      rank_occ  rank_gcs  rank_lcs  ...  h_index  g_index  m_index
author_keywords                                     ...                           
FINTECH                      1         1         1  ...       31       12     7.75
INNOVATION                   2         2         2  ...        7        7     1.75
FINANCIAL_SERVICES           3         4        15  ...        4        4     1.00
FINANCIAL_INCLUSION          4         5         3  ...        3        3     0.75
FINANCIAL_TECHNOLOGY         5        15        45  ...        3        3     1.00
CROWDFUNDING                 6        23        16  ...        3        3     1.00
MARKETPLACE_LENDING          7        25        51  ...        3        3     1.50
BUSINESS_MODELS              8         3        14  ...        2        2     1.00
CYBER_SECURITY               9        21         9  ...        2        2     1.00
CASE_STUDY                  10        22        10  ...        2        2     0.67
<BLANKLINE>
[10 rows x 16 columns]


"""
from ....internals.mixins import InputFunctionsMixin
from ...load import load__filtered_database
from .internals.internal__add_rank_field_by_metrics import (
    internal__add_rank_field_by_metrics,
)
from .internals.internal__check_field_types import internal__check_field_types
from .internals.internal__compute_basic_metrics_per_term_fields import (
    internal__compute_basic_metrics_per_term_fields,
)
from .internals.internal__compute_impact_metrics import internal__compute_impact_metrics
from .internals.internal__explode_terms_in_field import internal__explode_terms_in_field
from .internals.internal__remove_stopwords_from_axis import (
    internal__remove_stopwords_from_axis,
)
from .internals.internal__select_fields import internal__select_fields


class DataFrame(
    InputFunctionsMixin,
):
    def build(self):

        database = load__filtered_database(
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=self.params.records_order_by,
            records_match=self.params.records_match,
        )

        metrics = internal__select_fields(
            records=database,
            field=self.params.source_field,
        )

        metrics = internal__explode_terms_in_field(
            records=metrics,
            field=self.params.source_field,
        )

        metrics = internal__compute_basic_metrics_per_term_fields(
            records=metrics,
            field=self.params.source_field,
        )

        metrics = internal__compute_impact_metrics(
            database,
            metrics,
            field=self.params.source_field,
        )

        metrics = internal__remove_stopwords_from_axis(
            dataframe=metrics,
            root_dir=self.params.root_dir,
            axis=0,
        )

        metrics = internal__add_rank_field_by_metrics(
            records=metrics,
        )

        metrics = internal__check_field_types(
            records=metrics,
        )

        return metrics


# def performance_metrics_frame(
#     #
#     # ITEMS PARAMS:
#     field,
#     #
#     # FILTER PARAMS:
#     metric="OCCGC",
#     top_n=20,
#     occ_range=(None, None),
#     gc_range=(None, None),
#     custom_terms=None,
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
#     database="main",
#     year_filter=(None, None),
#     cited_by_filter=(None, None),
#     **filters,
# ):
#     """:meta private:"""

#     records = _mt_calculate_global_performance_metrics(
#         #
#         # ITEMS PARAMS:
#         field=field,
#         #
#         # DATABASE PARAMS:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     filtered_records = _mt_filter_records_by_metric(
#         records=records,
#         metric=metric,
#         top_n=top_n,
#         occ_range=occ_range,
#         gc_range=gc_range,
#         custom_items=custom_terms,
#     )

#     selected_records = _mt_select_record_columns_by_metric(
#         filtered_records,
#         metric,
#     )

#     if metric == "OCCGC":
#         metric = "OCC"

#     return selected_records
