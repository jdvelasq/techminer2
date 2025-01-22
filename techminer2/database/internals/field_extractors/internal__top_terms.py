# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-few-public-methods

from typing import Dict, List, Optional, Tuple

from ...load import load__filtered_database


def internal__top_terms(
    source_field: str,
    terms_order_criteria: str,
    top_n_terms: int,
    term_occurrences_range: tuple,
    term_citations_range: tuple,
    terms_in: list,
    #
    # DATABASE PARAMS:
    root_dir: str,
    database: str,
    record_years_range: Tuple[Optional[int], Optional[int]],
    record_citations_range: Tuple[Optional[int], Optional[int]],
    records_order_by: Optional[str],
    records_match: Optional[Dict[str, List[str]]],
):
    def build_terms_df(
        root_dir: str,
        database: str,
        record_years_range: Tuple[Optional[int], Optional[int]],
        record_citations_range: Tuple[Optional[int], Optional[int]],
        records_order_by: Optional[str],
        records_match: Optional[Dict[str, List[str]]],
    ):
        records = load__filtered_database(
            root_dir=root_dir,
            database=database,
            record_years_range=record_years_range,
            record_citations_range=record_citations_range,
            records_order_by=records_order_by,
            records_match=records_match,
        )

        records = records[[source_field, "global_citations", "local_citations"]].copy()
        records["OCC"] = 1
        records[source_field] = records[source_field].str.split("; ")
        terms = records.explode(source_field)

        terms = (
            terms.groupby([source_field])
            .agg({"OCC": "sum", "global_citations": "sum", "local_citations": "sum"})
            .reset_index()
        )

        return terms

    def sort_terms_by_metric(records, metric):
        if metric == "OCC":
            records = records.sort_values(
                ["OCC", "global_citations", "local_citations", source_field],
                ascending=[False, False, False, True],
            )
        elif metric == "global_citations":
            records = records.sort_values(
                ["global_citations", "OCC", "local_citations", source_field],
                ascending=[False, False, False, True],
            )
        else:
            raise ValueError("Invalid metric")

        return records

    def filter_by_top_n(records, top_n):
        if top_n is not None:
            records = records.head(top_n)
        return records

    def filter_terms_by_occ_range(records, occ_range):
        if occ_range is not None:
            if occ_range[0] is not None:
                records = records[records["OCC"] >= occ_range[0]]
            if occ_range[1] is not None:
                records = records[records["OCC"] <= occ_range[1]]
        return records

    def filter_terms_by_gc_range(records, gc_range):
        if gc_range is not None:
            if gc_range[0] is not None:
                records = records[records["global_citations"] >= gc_range[0]]
            if gc_range[1] is not None:
                records = records[records["global_citations"] <= gc_range[1]]
        return records

    def filter_by_custom_terms(records, records_match):
        if records_match is not None:
            records = records[records[source_field].isin(records_match)]
        return records

    #
    # MAIN CODE
    #
    terms = build_terms_df(
        root_dir=root_dir,
        database=database,
        record_years_range=record_years_range,
        record_citations_range=record_citations_range,
        records_order_by=records_order_by,
        records_match=records_match,
    )

    terms = filter_terms_by_gc_range(terms, term_citations_range)
    terms = filter_terms_by_occ_range(terms, term_occurrences_range)
    terms = sort_terms_by_metric(terms, terms_order_criteria)
    terms = filter_by_custom_terms(terms, terms_in)
    terms = filter_by_top_n(terms, top_n_terms)

    terms = terms[source_field].tolist()

    return terms
