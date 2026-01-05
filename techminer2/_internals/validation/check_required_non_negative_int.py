# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods


def internal__check_required_non_negative_int(value: int, param_name: str) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{param_name} must be int, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"{param_name} must be non-negative, got {value}")
    return value
