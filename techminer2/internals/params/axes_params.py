# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines nx param filters."""

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class AxesParams:
    """:meta private:"""

    xaxes_range: Tuple[Optional[float], Optional[float]] = (None, None)
    yaxes_range: Tuple[Optional[float], Optional[float]] = (None, None)
    show_axes: bool = False


class AxesParamsMixin:
    """:meta private:"""

    def set_nx_params(self, **kwargs):
        """:meta private:"""
        for key, value in kwargs.items():
            if hasattr(self.item_params, key):
                setattr(self.item_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for AxesParams: {key}")
        return self
