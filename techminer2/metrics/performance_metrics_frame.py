# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance Metrics Frame
===============================================================================

## >>> from techminer2.metrics import performance_metrics_frame
## >>> performance_metrics_frame(
## ...     field='author_keywords',
## ...     #
## ...     # FILTER PARAMS:
## ...     metric='OCCGC',
## ...     top_n=20,
## ...     occ_range=(None, None),
## ...     gc_range=(None, None),
## ...     custom_terms=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=None,
## ...     cited_by_filter=None,
## ... ).head()
                      rank_occ  rank_gcs  rank_lcs  ...  h_index  g_index  m_index
author_keywords                                     ...                           
FINTECH                      1         1         1  ...       31       12     7.75
INNOVATION                   2         2         2  ...        7        7     1.75
FINANCIAL_SERVICES           3         4        36  ...        4        4     1.00
FINANCIAL_INCLUSION          4         5         3  ...        3        3     0.75
FINANCIAL_TECHNOLOGY         5        15        37  ...        3        3     1.00
<BLANKLINE>
[5 rows x 9 columns]


"""
from .._core.metrics.calculate_global_performance_metrics import calculate_global_performance_metrics
from .._core.metrics.filter_records_by_metric import filter_records_by_metric
from .._core.metrics.select_record_columns_by_metric import select_record_columns_by_metric


def performance_metrics_frame(
    #
    # ITEMS PARAMS:
    field,
    #
    # FILTER PARAMS:
    metric="OCCGC",
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    records = calculate_global_performance_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    filtered_records = filter_records_by_metric(
        records=records,
        metric=metric,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_terms,
    )

    selected_records = select_record_columns_by_metric(
        filtered_records,
        metric,
    )

    if metric == "OCCGC":
        metric = "OCC"

    return selected_records
