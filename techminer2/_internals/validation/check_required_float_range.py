# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods


def internal__check_required_float_range(
    min_value: float, max_value: float, min_param_name: str, max_param_name: str
) -> tuple[float, float]:

    for val, name in [(min_value, min_param_name), (max_value, max_param_name)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a number, got {type(val).__name__}")
        if not 0 <= val <= 1:
            raise ValueError(f"{name} must be between 0 and 1, got {val}")

    if min_value > max_value:
        raise ValueError(
            f"{min_param_name} ({min_value}) must be less than or equal to {max_param_name} ({max_value})"
        )

    return float(min_value), float(max_value)
