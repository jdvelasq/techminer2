# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


from .internal__get_field_values_from_database import (
    internal__get_field_values_from_database,
)


def internal__fields_difference(
    compare_field,
    to_field,
    #
    # DATABASE PARAMS:
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    sort_by: str,
    **filters,
):

    set_a = internal__get_field_values_from_database(
        field=compare_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )
    set_a = set_a.term.tolist()
    set_a = set(set_a)

    set_b = internal__get_field_values_from_database(
        field=to_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )
    set_b = set_b.term.tolist()
    set_b = set(set_b)

    common_terms = set_a.difference(set_b)
    common_terms = list(sorted(common_terms))

    return common_terms
