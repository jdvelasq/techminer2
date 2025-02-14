# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Dict, List, Optional, Tuple

from ...internals.io import internal__load_filtered_database


def internal__get_field_values_from_database(
    #
    # FIELD:
    field: str,
    #
    # DATABASE:
    root_dir: str,
    database: str,
    record_years_range: Tuple[Optional[int], Optional[int]],
    record_citations_range: Tuple[Optional[int], Optional[int]],
    records_order_by: Optional[str],
    records_match: Optional[Dict[str, List[str]]],
):
    """Returns a DataFrame with the content of the field in all databases."""

    data_frame = (
        internal__load_filtered_database()
        .where_directory_is(root_dir)
        .where_database_is(database)
        .where_record_years_between(
            record_years_range[0],
            record_years_range[1],
        )
        .where_record_citations_between(
            record_citations_range[0],
            record_citations_range[1],
        )
        .where_records_ordered_by(records_order_by)
        .where_records_match(records_match)
        .build()
    )

    df = data_frame[[field]].dropna()

    df[field] = df[field].str.split("; ")
    df = df.explode(field)
    df[field] = df[field].str.strip()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    df = df.rename(columns={field: "term"})

    return df
