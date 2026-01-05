# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

from typing import Optional, Tuple


def internal__check_required_open_ended_int_range(
    range_tuple: Tuple[Optional[int], Optional[int]],
    param_name: str,
) -> Tuple[Optional[int], Optional[int]]:

    min_val, max_val = range_tuple

    for val, bound in zip((min_val, max_val), ("min", "max")):
        if val is not None and not isinstance(val, int):
            raise TypeError(
                f"{param_name} {bound} value ({val}) must be an int or None."
            )

    if min_val is not None and max_val is not None:
        if min_val > max_val:
            raise ValueError(
                f"{param_name} min ({min_val}) > max ({max_val}). Did you swap them?"
            )

    return range_tuple
