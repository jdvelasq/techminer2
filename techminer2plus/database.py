# flake8: noqa
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
"""
Database
==============================================================================

Represents the databasef files in disk.

>>> import techminer2plus as tm2p




>>> root_dir = "data/regtech/"

>>> tm2p.records(root_dir=root_dir)
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={})

    
>>> tm2p.records(root_dir=root_dir, filters={
...     "countries": ['Australia', 'United Kingdom', 'United States']
... })
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={'countries': ['Australia', 'United
    Kingdom', 'United States']})


"""
from dataclasses import dataclass

from .filter.filter import Filter


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
