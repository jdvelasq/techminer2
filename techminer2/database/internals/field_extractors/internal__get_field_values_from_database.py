# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...load import load__filtered_database


def internal__get_field_values_from_database(
    field: str,
    #
    # DATABASE PARAMS:
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    sort_by: str,
    **filters,
):
    """Returns a DataFrame with the content of the field in all databases."""

    dataframe = load__filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    df = dataframe[[field]].dropna()

    df[field] = df[field].str.split("; ")
    df = df.explode(field)
    df[field] = df[field].str.strip()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    df = df.rename(columns={field: "term"})

    return df
