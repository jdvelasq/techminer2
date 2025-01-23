# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__select_fields(
    records,
    field,
):
    """:meta private:"""

    records = records[
        [
            field,
            "global_citations",
            "local_citations",
            "year",
        ]
    ].copy()

    return records
