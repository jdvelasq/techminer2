# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .internal__sort_records_by_metric import internal__sort_records_by_metric


def internal__add_rank_field_by_metrics(records):

    records = internal__sort_records_by_metric(records, "local_citations")
    records.insert(0, "rank_lcs", range(1, len(records) + 1))

    records = internal__sort_records_by_metric(records, "global_citations")
    records.insert(0, "rank_gcs", range(1, len(records) + 1))

    records = internal__sort_records_by_metric(records, "OCC")
    records.insert(0, "rank_occ", range(1, len(records) + 1))

    return records
