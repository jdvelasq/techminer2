# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines what to load from database files."""

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class DatabaseFilters:
    """:meta private:"""

    database: str = "main"
    year_filter: Tuple[Optional[int], Optional[int]] = (None, None)
    cited_by_filter: Tuple[Optional[int], Optional[int]] = (None, None)
    sort_by: Optional[str] = None


class SetDatabaseFiltersMixin:
    """:meta private:"""

    def set_database_filters(self, **kwargs):
        """Set database parameters."""

        for key, value in kwargs.items():
            setattr(self.database_filters, key, value)

        return self
