# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines nx param filters."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class NxSpringLayoutParams:
    """:meta private:"""

    nx_k: Optional[float] = None
    nx_iterations: int = 30
    nx_seed: int = 0


class NxSpringLayoutParamsMixin:
    """:meta private:"""

    def set_nx_spring_layout_params(self, **kwargs):
        """:meta private:"""

        for key, value in kwargs.items():
            if hasattr(self.nx_sprint_layout_params, key):
                setattr(self.nx_sprint_layout_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for NxSpringLayoutParams: {key}")
        return self
