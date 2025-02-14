# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Dict, List, Optional, Tuple

from .get_field_values_from_database import internal__get_field_values_from_database


def internal__fields_difference(params):

    # Build the set of terms of first field
    set_a = internal__get_field_values_from_database(params)
    set_a = set_a.term.tolist()
    set_a = set(set_a)

    # Build the set of terms of second field
    set_b = internal__get_field_values_from_database(
        params.update_params(field=params.other_field)
    )
    set_b = set_b.term.tolist()
    set_b = set(set_b)

    # Get the difference between the two sets
    common_terms = set_a.difference(set_b)
    common_terms = list(sorted(common_terms))

    return common_terms
