# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods


def internal__check_required_int(value, param_name: str) -> int:

    if not isinstance(value, int):
        raise ValueError(f"{param_name} must be an integer, got {type(value).__name__}")
    return value
