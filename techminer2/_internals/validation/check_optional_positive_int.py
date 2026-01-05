# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

from typing import Optional


def internal__check_optional_positive_int(
    value: Optional[int], param_name: str
) -> Optional[int]:
    if value is None:
        return value
    if not isinstance(value, int):
        raise TypeError(f"{param_name} must be int, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"{param_name} must be positive, got {value}")
    return value
