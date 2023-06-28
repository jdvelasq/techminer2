"""
Records
==============================================================================

>>> root_dir = "data/regtech/"

>>> import techminer2plus as tm2p

>>> tm2p.Records(root_dir=root_dir).field("authors", top_n=10).df_
             rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
authors                              ...                           
Arner DW            1        1    3  ...      3.0      3.0     0.43
Buckley RP          2        2    3  ...      3.0      3.0     0.43
Barberis JN         3        3    2  ...      2.0      2.0     0.29
Butler T            4        5    2  ...      2.0      2.0     0.33
Hamdan A            5       15    2  ...      2.0      2.0     0.50
Turki M             6       16    2  ...      2.0      2.0     0.50
Lin W               7       17    2  ...      2.0      1.0     0.50
Singh C             8       18    2  ...      2.0      1.0     0.50
Brennan R           9       19    2  ...      2.0      1.0     0.50
Crane M            10       20    2  ...      2.0      1.0     0.50
<BLANKLINE>
[10 rows x 18 columns]




"""

import os.path

import pandas as pd

from .field import Field


class Records(Field):
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

    def read_records(self):
        """loads and filter records of main database text files."""

        self._get_records_from_file()
        self._filter_records_by_year()
        self._filter_records_by_citations()
        self._apply_filters_to_records()

        return self.records

    def _get_records_from_file(self):
        """Read raw records from a file."""

        file_name = {
            "main": "_main.csv",
            "references": "_references.csv",
            "cited_by": "_cited_by.csv",
        }[self.database]

        file_path = os.path.join(self.root_dir, "databases", file_name)
        self.records = pd.read_csv(file_path, sep=",", encoding="utf-8")
        self.records = self.records.drop_duplicates()

    def _filter_records_by_year(self):
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

    def _filter_records_by_citations(self):
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

    def _apply_filters_to_records(self):
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
