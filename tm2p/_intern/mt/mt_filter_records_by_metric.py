"""
This function filters a dataframe of performance metrics by an specific metric.

"""

from tm2p._intern.mt.mt_extract_top_n_terms_by_metric import (
    _mt_extract_top_n_terms_by_metric,
)
from tm2p._intern.mt.mt_sort_records_by_metric import _mt_sort_records_by_metric


def _mt_filter_records_by_metric(
    records,
    metric,
    #
    # FILTER PARAMS:
    top_n,
    occ_range,
    gc_range,
    custom_items,
):
    """:meta private:"""

    records = records.copy()

    if custom_items is None:
        #
        if metric == "OCCGC":
            #
            # In this case not is possibe to use trend_analysis
            #
            # Selects the top_n items by OCC
            custom_items_occ = _mt_extract_top_n_terms_by_metric(
                indicators=records,
                metric="OCC",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            #
            # Selects the top_n items by GCS
            custom_items_gc = _mt_extract_top_n_terms_by_metric(
                indicators=records,
                metric="global_citations",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items = custom_items_occ[:]
            custom_items += [
                item for item in custom_items_gc if item not in custom_items_occ
            ]

        else:
            #
            # Default custom items selection
            custom_items = _mt_extract_top_n_terms_by_metric(
                indicators=records,
                metric=metric,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    records = records[records.index.isin(custom_items)]
    records = _mt_sort_records_by_metric(records, metric)

    return records
