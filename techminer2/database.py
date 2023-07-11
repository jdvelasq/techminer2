# flake8: noqa
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
"""
Database
==============================================================================

Represents the databasef files in disk.

>>> import techminer2 as tm2




>>> root_dir = "data/regtech/"

>>> tm2.records(root_dir=root_dir)
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={})

    
>>> tm2.records(root_dir=root_dir, filters={
...     "countries": ['Australia', 'United Kingdom', 'United States']
... })
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={'countries': ['Australia', 'United
    Kingdom', 'United States']})


"""
from dataclasses import dataclass

from ._read_records import read_records
from .filter.filter import Filter
from .vantagepoint.summary_sheet import summary_sheet


@dataclass
class Database:
    root_dir: str  # path to main folder of database
    database: str = "main"

    def __repr__(self):
        return f"Database(root_dir='{self.root_dir}')"

    def filter(
        self,
        year_filter: tuple = (None, None),
        cited_by_filter: tuple = (None, None),
        **filters,
    ):
        return Filter(
            root_dir=self.root_dir,
            database=self.database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    def summary_sheet(self):
        """Return a summary of the columns of the database.

        >>> import techminer2 as tm2
        >>> root_dir = "data/regtech/"
        >>> tm2.Database(root_dir).summary_sheet().head()
                         column  number of terms coverage (%)
        0              abstract               52         1.0%
        1  abstract_nlp_phrases               47         0.9%
        2          affiliations               52         1.0%
        3                art_no                8        0.15%
        4               article               52         1.0%

        """
        return summary_sheet(
            read_records(root_dir=self.root_dir, database=self.database)
        )
