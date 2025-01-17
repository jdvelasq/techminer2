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
    root_dir,
):

    set_a = internal__get_field_values_from_database(root_dir, compare_field)
    set_a = set_a.term.tolist()
    set_a = set(set_a)

    set_b = internal__get_field_values_from_database(root_dir, to_field)
    set_b = set_b.term.tolist()
    set_b = set(set_b)

    common_terms = set_a.difference(set_b)

    return list(sorted(common_terms))
