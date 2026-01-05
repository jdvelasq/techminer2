# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods

from typing import Optional

from sklearn.base import BaseEstimator  # type: ignore


def internal__check_optional_base_estimator(
    value: Optional[BaseEstimator], param_name: str
) -> Optional[BaseEstimator]:
    if value is not None and not isinstance(value, BaseEstimator):
        raise TypeError(
            f"{param_name} must be a scikit-learn BaseEstimator or None, got {type(value).__name__}"
        )
    return value
