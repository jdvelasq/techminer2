# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Dict, List, Optional, Tuple

from .get_field_values_from_database import internal__get_field_values_from_database


def internal__fields_difference(
    #
    # FIELDS:
    field,
    other_field,
    #
    # DATABASE:
    root_dir: str,
    database: str,
    record_years_range: Tuple[Optional[int], Optional[int]],
    record_citations_range: Tuple[Optional[int], Optional[int]],
    records_order_by: Optional[str],
    records_match: Optional[Dict[str, List[str]]],
):

    set_a = internal__get_field_values_from_database(
        #
        # FIELD:
        field=field,
        #
        # DATABASE:
        root_dir=root_dir,
        database=database,
        record_years_range=record_years_range,
        record_citations_range=record_citations_range,
        records_order_by=records_order_by,
        records_match=records_match,
    )
    set_a = set_a.term.tolist()
    set_a = set(set_a)

    set_b = internal__get_field_values_from_database(
        #
        # FIELD:
        field=other_field,
        root_dir=root_dir,
        #
        # DATABASE:
        database=database,
        record_years_range=record_years_range,
        record_citations_range=record_citations_range,
        records_order_by=records_order_by,
        records_match=records_match,
    )
    set_b = set_b.term.tolist()
    set_b = set(set_b)

    common_terms = set_a.difference(set_b)
    common_terms = list(sorted(common_terms))

    return common_terms
