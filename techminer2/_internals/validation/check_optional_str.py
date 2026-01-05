# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

from typing import Optional

from techminer2._internals.validation.check_required_str import (
    internal__check_required_str,
)


def internal__check_optional_str(
    value: Optional[str], param_name: str
) -> Optional[str]:
    if value is None:
        return None
    return internal__check_required_str(value=value, param_name=param_name)
