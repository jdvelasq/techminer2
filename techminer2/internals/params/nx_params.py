# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines nx param filters."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class NxParams:
    """:meta private:"""

    nx_k: Optional[float] = None
    nx_iterations: int = 30
    nx_random_state: int = 0


class NxParamsMixin:
    """:meta private:"""

    def set_nx_params(self, **kwargs):
        """:meta private:"""
        for key, value in kwargs.items():
            if hasattr(self.item_params, key):
                setattr(self.item_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for NxParams: {key}")
        return self
