# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines what to load from database files."""

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class DatabaseParams:
    """:meta private:"""

    root_dir: str = "./"
    database: str = "main"
    year_filter: Tuple[Optional[int], Optional[int]] = (None, None)
    cited_by_filter: Tuple[Optional[int], Optional[int]] = (None, None)
    sort_by: Optional[str] = None


class DatabaseParamsMixin:
    """:meta private:"""

    def set_database_params(self, **kwargs):
        """Set database parameters."""
        for key, value in kwargs.items():
            # if hasattr(self.database_params, key):
            #     setattr(self.database_params, key, value)
            # else:
            #     raise ValueError(f"Invalid parameter for DatabaseParams: {key}")
            setattr(self.database_params, key, value)
        return self
