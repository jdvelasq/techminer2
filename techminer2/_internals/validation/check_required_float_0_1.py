# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods


def internal__check_required_float_0_1(value: float, param_name: str) -> float:

    if not isinstance(value, (int, float)):
        raise TypeError(f"{param_name} must be numeric, got {type(value).__name__}")
    if not (0 <= value <= 1):
        raise ValueError(f"{param_name} must be between 0 and 1, got {value}")

    return float(value)
