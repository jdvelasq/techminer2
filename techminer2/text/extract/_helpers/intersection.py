# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
from techminer2.text.extract._helpers.get_values_from_field import (
    internal__get_values_from_field,
)


def internal__intersection(params):

    # Build the set of terms of first field
    set_a = internal__get_values_from_field(params)
    set_a = set_a.term.tolist()
    set_a = set(set_a)

    # Build the set of terms of second field
    set_b = internal__get_values_from_field(params.update(field=params.other_field))
    set_b = set_b.term.tolist()
    set_b = set(set_b)

    # Get the intersection between the two sets
    common_terms = set_a.intersection(set_b)
    common_terms = list(sorted(common_terms))

    return common_terms

    return common_terms
