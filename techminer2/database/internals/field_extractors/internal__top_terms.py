# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-few-public-methods

from ...load import load__filtered_database


def internal__top_terms(
    field: str,
    metric: str,
    top_n: int,
    occ_range: tuple,
    gc_range: tuple,
    custom_terms: list,
    #
    # DATABASE PARAMS:
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    sort_by: str,
    **filters,
):
    def build_records_df(
        root_dir: str,
        database: str,
        year_filter: tuple,
        cited_by_filter: tuple,
        sort_by: str,
        **filters,
    ):
        records = load__filtered_database(
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            sort_by=sort_by,
            **filters,
        )

        records = records[[field, "global_citations", "local_citations"]].copy()
        records["OCC"] = 1
        records[field] = records[field].str.split("; ")
        records = records.explode(field)

        records = (
            records.gruupby([field], as_index=False)
            .agg({"OCC": "sum", "global_citations": "sum", "local_citations": "sum"})
            .reset_index()
        )

        return records

    def sort_records_by_metric(records, metric):
        if metric == "OCC":
            records = records.sort_values(
                ["OCC", "global_citations", "local_citations", field],
                ascending=[False, False, False, True],
            )
        elif metric == "global_citations":
            records = records.sort_values(
                ["global_citations", "OCC", "local_citations", field],
                ascending=[False, False, False, True],
            )
        else:
            raise ValueError("Invalid metric")

        return records

    def filter_by_top_n(records, top_n):
        if top_n is not None:
            records = records.head(top_n)
        return records

    def filter_by_occ_range(records, occ_range):
        if occ_range is not None:
            if occ_range[0] is not None:
                records = records[records["OCC"] >= occ_range[0]]
            if occ_range[1] is not None:
                records = records[records["OCC"] <= occ_range[1]]
        return records

    def filter_by_gc_range(records, gc_range):
        if gc_range is not None:
            if gc_range[0] is not None:
                records = records[records["global_citations"] >= gc_range[0]]
            if gc_range[1] is not None:
                records = records[records["global_citations"] <= gc_range[1]]
        return records

    def filter_by_custom_terms(records, custom_terms):
        if custom_terms is not None:
            records = records[records[field].isin(custom_terms)]
        return records

    #
    # MAIN CODE
    #
    records = build_records_df(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    records = filter_by_gc_range(records, gc_range)
    records = filter_by_occ_range(records, occ_range)
    records = sort_records_by_metric(records, metric)
    records = filter_by_custom_terms(records, custom_terms)
    records = filter_by_top_n(records, top_n)

    return records
