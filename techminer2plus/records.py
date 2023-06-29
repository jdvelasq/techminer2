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

from .counters_lib import add_counters_to_frame_axis
from .coverage import coverage
from .field import Field
from .main_information import MainInformation
from .metrics_lib import indicators_by_field, items_occ_by_year


class Records:
    """loads and filter records of main database text files."""

    def __init__(
        self,
        root_dir="./",
        database="main",
        year_filter=None,
        cited_by_filter=None,
        **filters,
    ):
        self.__root_dir = root_dir
        self.__database = database
        self.__year_filter = year_filter
        self.__cited_by_filter = cited_by_filter
        self.__filters = filters

        self.__records = None

        self.__read_records()

    #
    #
    # PROPERTIES
    #
    #
    @property
    def records_(self):
        """Returns the database records as a dataframe."""
        return self.__records.copy()

    # @property
    # def root_dir_(self):
    #     """Returns the root directory."""
    #     return self.__root_dir

    # @property
    # def database_(self):

    #     return self.__database

    # @property
    # def year_range_(self):
    #     """Returns the year range filter."""
    #     return self.__year_range

    # @property
    # def cited_by_range_(self):
    #     """Returns the cited by range filter."""
    #     return self.__cited_by_range

    #
    #
    # INTEFACE METHODS
    #
    #

    def coverage(self, column):
        """Returns a MainInformation object."""
        return coverage(parent=self, column=column)

    def main_information(self):
        """Returns a MainInformation object."""
        return MainInformation(parent=self)

    def field(
        self,
        field,
        metric="OCC",
        top_n=None,
        occ_range=None,
        gc_range=None,
        custom_items=None,
    ):
        return Field(
            records=self,
            field=field,
            metric=metric,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
        )

    #
    #
    # DATABASE COMPUTATIONS
    #
    #
    def indicators_by_field(self, field, time_window=2):
        """Returns a dataframe with indicators by field."""
        return indicators_by_field(
            field=field,
            time_window=time_window,
            #
            # Database params:
            root_dir=self.__root_dir,
            database=self.__database,
            year_filter=self.__year_filter,
            cited_by_filter=self.__cited_by_filter,
            **self.__filters,
        )

    def items_occ_by_year(self, field, cumulative=False):
        """Returns a dataframe with items by year."""
        return items_occ_by_year(
            field=field,
            cumulative=cumulative,
            #
            # Database params:
            root_dir=self.__root_dir,
            database=self.__database,
            year_filter=self.__year_filter,
            cited_by_filter=self.__cited_by_filter,
            **self.__filters,
        )

    #
    #
    # AUXILIARY METHODS
    #
    #
    def add_counters_to_frame_axis(
        self,
        dataframe,
        axis,
        field,
    ):
        return add_counters_to_frame_axis(
            dataframe=dataframe,
            axis=axis,
            field=field,
            #
            # Database params:
            root_dir=self.__root_dir,
            database=self.__database,
            year_filter=self.__year_filter,
            cited_by_filter=self.__cited_by_filter,
            **self.__filters,
        )

    #
    #
    # INTERNAL METHODS
    #
    #
    def __repr__(self):
        """String representation."""

        params = [
            f"root_dir='{self.__root_dir}'",
            f"database='{self.__database}'",
        ]

        if self.__year_filter is not None:
            params.append(f", year_filter={self.__year_filter}")

        if self.__cited_by_filter is not None:
            params.append(f", cited_by_filter={self.__cited_by_filter}")

        if self.__filters:
            params.append(f", filters={self.__filters}")

        params = ", ".join(params)

        return f"{self.__class__.__name__}({params})"

    def __read_records(self):
        """loads and filter records of main database text files."""

        self.__get_records_from_file()
        self.__filter_records_by_year_range()
        self.__filter_records_by_citations_range()
        self.__apply_filters_to_records()

    def __get_records_from_file(self):
        """Read raw records from a file."""

        file_name = {
            "main": "_main.csv",
            "references": "_references.csv",
            "cited_by": "_cited_by.csv",
        }[self.__database]

        file_path = os.path.join(self.__root_dir, "databases", file_name)
        self.__records = pd.read_csv(file_path, sep=",", encoding="utf-8")
        self.__records = self.__records.drop_duplicates()

    def __filter_records_by_year_range(self):
        """Filter records by year."""

        if self.__year_filter is None:
            return

        if not isinstance(self.__year_filter, tuple):
            raise TypeError(
                "The year_range parameter must be a tuple of two values."
            )

        if len(self.__year_filter) != 2:
            raise ValueError(
                "The year_range parameter must be a tuple of two values."
            )

        start_year, end_year = self.__year_filter

        if start_year is not None:
            self.__records = self.__records[self.__records.year >= start_year]

        if end_year is not None:
            self.__records = self.__records[self.__records.year <= end_year]

    def __filter_records_by_citations_range(self):
        """Filter records by year."""

        if self.__cited_by_filter is None:
            return

        if not isinstance(self.__cited_by_filter, tuple):
            raise TypeError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        if len(self.__cited_by_filter) != 2:
            raise ValueError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        cited_by_min, cited_by_max = self.__cited_by_filter

        if cited_by_min is not None:
            self.__records = self.__records[
                self.__records.global_citations >= cited_by_min
            ]

        if cited_by_max is not None:
            self.__records = self.__records[
                self.__records.global_citations <= cited_by_max
            ]

    def __apply_filters_to_records(self):
        """Apply user filters in order."""

        for filter_name, filter_value in self.__filters.items():
            # Split the filter value into a list of strings
            database = self.__records[["article", filter_name]]
            database[filter_name] = database[filter_name].str.split(";")

            # Explode the list of strings into multiple rows
            database = database.explode(filter_name)

            # Remove leading and trailing whitespace from the strings
            database[filter_name] = database[filter_name].str.strip()

            # Keep only records that match the filter value
            database = database[database[filter_name].isin(filter_value)]
            self.__records = self.__records[
                self.__records["article"].isin(database["article"])
            ]
