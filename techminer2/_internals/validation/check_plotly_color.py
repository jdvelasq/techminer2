# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

import numbers
from typing import Any, Sequence, Union


def internal__check_plotly_color(
    value: Any,
    param_name: str,
) -> Union[str, float, Sequence[float]]:

    if isinstance(value, str):
        return value
    if isinstance(value, numbers.Real):
        return float(value)
    if (
        isinstance(value, Sequence)
        and not isinstance(value, str)
        and 3 <= len(value) <= 4
        and all(isinstance(x, numbers.Real) for x in value)
    ):
        return tuple(float(x) for x in value)
    raise ValueError(
        f"Parameter '{param_name}' must be a valid Plotly color (str, float, or sequence of 3 or 4 floats)."
    )
