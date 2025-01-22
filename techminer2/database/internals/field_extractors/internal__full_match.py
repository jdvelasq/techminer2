# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Dict, List, Optional, Tuple

from .internal__get_field_values_from_database import (
    internal__get_field_values_from_database,
)


def internal__full_match(
    term_pattern: str,
    case_sensitive: bool,
    regex_flags: int,
    source_field: str,
    #
    # DATABASE PARAMS:
    root_dir: str,
    database: str,
    record_years_range: Tuple[Optional[int], Optional[int]],
    record_citations_range: Tuple[Optional[int], Optional[int]],
    records_order_by: Optional[str],
    records_match: Optional[Dict[str, List[str]]],
):

    dataframe = internal__get_field_values_from_database(
        source_field=source_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        record_years_range=record_years_range,
        record_citations_range=record_citations_range,
        records_order_by=records_order_by,
        records_match=records_match,
    )

    dataframe = dataframe[
        dataframe.term.str.fullmatch(
            pat=term_pattern,
            case=case_sensitive,
            flags=regex_flags,
        )
    ]

    dataframe = dataframe.dropna()
    dataframe = dataframe.sort_values("term", ascending=True)
    terms = dataframe.term.tolist()

    return terms
