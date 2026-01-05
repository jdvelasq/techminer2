# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods


def internal__check_required_bool(value, param_name: str) -> bool:

    if not isinstance(value, bool):
        raise ValueError(f"{param_name} must be a boolean, got {type(value).__name__}")
    return value
