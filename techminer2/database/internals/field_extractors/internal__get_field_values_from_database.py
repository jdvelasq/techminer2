# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Dict, List, Optional, Tuple

from ...load import load__filtered_database


def internal__get_field_values_from_database(
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
    """Returns a DataFrame with the content of the field in all databases."""

    dataframe = load__filtered_database(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        record_years_range=record_years_range,
        record_citations_range=record_citations_range,
        records_order_by=records_order_by,
        records_match=records_match,
    )

    df = dataframe[[source_field]].dropna()

    df[source_field] = df[source_field].str.split("; ")
    df = df.explode(source_field)
    df[source_field] = df[source_field].str.strip()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    df = df.rename(columns={source_field: "term"})

    return df
