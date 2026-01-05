# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

from typing import Optional, Union


def internal__check_optional_str_or_dict(
    value: Optional[Union[str, dict]], param_name: str
) -> Optional[Union[str, dict]]:
    if value is None:
        return None
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        raise TypeError(
            f"{param_name} must be a string or a dictionary, got {type(value).__name__}"
        )
    return value
