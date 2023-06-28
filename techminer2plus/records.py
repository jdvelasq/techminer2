# flake8: noqa
"""
Records
==============================================================================




>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> tm2p.Records(root_dir=root_dir)
Records(root_dir='data/regtech/', database='main')


"""

import os.path

import pandas as pd

from .coverage import Coverage
from .field import Field


class Records(Field, Coverage):
    """loads and filter records of main database text files."""

    def __init__(
        self,
        root_dir="./",
        database="main",
        year_filter=None,
        cited_by_filter=None,
        **filters,
    ):
        super(Field, self).__init__()

        self.database = database
        self.year_filter = year_filter
        self.root_dir = root_dir
        self.filters = filters
        self.cited_by_filter = cited_by_filter
        self.records = None

    def __repr__(self):
        text = "Records("
        text += f"root_dir='{self.root_dir}'"
        text += f", database='{self.database}'"
        text += (
            f", year_filter={self.year_filter}"
            if self.year_filter is not None
            else ""
        )
        text += (
            f", cited_by_filter={self.cited_by_filter}"
            if self.cited_by_filter is not None
            else ""
        )
        text += f", filters={self.filters}" if len(self.filters) > 0 else ""
        text += ")"
        return text

    def read_records(self):
        """loads and filter records of main database text files."""

        self.__get_records_from_file()
        self.__filter_records_by_year()
        self.__filter_records_by_citations()
        self.__apply_filters_to_records()

        return self.records

    def __get_records_from_file(self):
        """Read raw records from a file."""

        file_name = {
            "main": "_main.csv",
            "references": "_references.csv",
            "cited_by": "_cited_by.csv",
        }[self.database]

        file_path = os.path.join(self.root_dir, "databases", file_name)
        self.records = pd.read_csv(file_path, sep=",", encoding="utf-8")
        self.records = self.records.drop_duplicates()

    def __filter_records_by_year(self):
        """Filter records by year."""

        if self.year_filter is None:
            return

        if not isinstance(self.year_filter, tuple):
            raise TypeError(
                "The year_range parameter must be a tuple of two values."
            )

        if len(self.year_filter) != 2:
            raise ValueError(
                "The year_range parameter must be a tuple of two values."
            )

        start_year, end_year = self.year_filter

        if start_year is not None:
            self.records = self.records[self.records.year >= start_year]

        if end_year is not None:
            self.records = self.records[self.records.year <= end_year]

    def __filter_records_by_citations(self):
        """Filter records by year."""

        if self.cited_by_filter is None:
            return

        if not isinstance(self.cited_by_filter, tuple):
            raise TypeError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        if len(self.cited_by_filter) != 2:
            raise ValueError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        cited_by_min, cited_by_max = self.cited_by_filter

        if cited_by_min is not None:
            self.records = self.records[
                self.records.global_citations >= cited_by_min
            ]

        if cited_by_max is not None:
            self.records = self.records[
                self.records.global_citations <= cited_by_max
            ]

    def __apply_filters_to_records(self):
        """Apply user filters in order."""

        for filter_name, filter_value in self.filters.items():
            # Split the filter value into a list of strings
            database = self.records[["article", filter_name]]
            database[filter_name] = database[filter_name].str.split(";")

            # Explode the list of strings into multiple rows
            database = database.explode(filter_name)

            # Remove leading and trailing whitespace from the strings
            database[filter_name] = database[filter_name].str.strip()

            # Keep only records that match the filter value
            database = database[database[filter_name].isin(filter_value)]
            self.records = self.records[
                self.records["article"].isin(database["article"])
            ]
