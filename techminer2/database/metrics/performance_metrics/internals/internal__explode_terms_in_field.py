# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Explode records by a field to obtain a term per record."""


def internal__explode_terms_in_field(
    records,
    field,
):
    """:meta private:"""

    records = records.copy()
    records[field] = records[field].str.split("; ")
    records = records.explode(field)

    return records
