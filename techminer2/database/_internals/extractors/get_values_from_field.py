# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ..io import internal__load_filtered_records_from_database


def internal__get_values_from_field(params):
    """Returns a DataFrame with the content of the field in all databases."""

    field = params.field
    data_frame = internal__load_filtered_records_from_database(params)
    data_frame = data_frame[[field]].dropna()
    data_frame[field] = data_frame[field].str.split("; ")
    data_frame = data_frame.explode(field)
    data_frame[field] = data_frame[field].str.strip()
    data_frame = data_frame.drop_duplicates()
    data_frame = data_frame.reset_index(drop=True)
    data_frame = data_frame.rename(columns={field: "term"})

    return data_frame
