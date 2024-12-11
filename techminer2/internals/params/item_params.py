# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines item param filters."""

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class ItemParams:
    """:meta private:"""

    field: str = ""
    top_n: Optional[int] = None
    occ_range: Tuple[Optional[int], Optional[int]] = (None, None)
    gc_range: Tuple[Optional[int], Optional[int]] = (None, None)
    custom_terms: Optional[list] = None


class ItemParamsMixin:
    """:meta private:"""

    def set_item_params(self, **kwargs):
        """Set database parameters."""
        for key, value in kwargs.items():
            if hasattr(self.item_params, key):
                setattr(self.item_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ItemParams: {key}")
        return self
