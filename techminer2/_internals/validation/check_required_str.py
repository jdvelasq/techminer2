# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods


def internal__check_required_str(value: str, param_name: str) -> str:

    if not isinstance(value, str):
        raise ValueError(f"{param_name} must be a string, got {type(value).__name__}")
    return value
