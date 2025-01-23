# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Load Filtered Database
===============================================================================
# doctest: +SKIP 


>>> from techminer2.database.load import load__filtered_database
>>> load__filtered_database( 
...     #
...     # DATABASE PARAMS:
...     root_dir="example/",
...     database="main",
...     record_years_range=(None, None),    
...     record_citations_range=(None, None),   
...     records_order_by=None,
...     records_match=None,
... ).head() # doctest: +ELLIPSIS
                                                   link  ...                                        descriptors
934   https://www.scopus.com/inward/record.uri?eid=2...  ...  ELABORATION_LIKELIHOOD_MODEL; FINTECH; K_PAY; ...
935   https://www.scopus.com/inward/record.uri?eid=2...  ...  ACTOR_NETWORK_THEORY; CHINESE_TELECOM; CONVERG...
1031  https://www.scopus.com/inward/record.uri?eid=2...  ...  FINANCIAL_INCLUSION; FINANCIAL_SCENARIZATION; ...
1059  https://www.scopus.com/inward/record.uri?eid=2...  ...                BANKING_INNOVATIONS; FINTECH; RISKS
1075  https://www.scopus.com/inward/record.uri?eid=2...  ...  BEHAVIOURAL_ECONOMICS; DIGITAL_TECHNOLOGIES; E...
<BLANKLINE>
[5 rows x 69 columns]

"""
import pathlib
from typing import Dict, List, Optional, Tuple

import pandas as pd  # type: ignore


def load__filtered_database(
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    record_years_range: Tuple[Optional[int], Optional[int]],
    record_citations_range: Tuple[Optional[int], Optional[int]],
    records_order_by: Optional[str],
    records_match: Optional[Dict[str, List[str]]],
):
    """:meta private:"""

    def get_records_from_file(root_dir, database):

        file_path = pathlib.Path(root_dir) / "databases/database.csv.zip"

        dataframe = pd.read_csv(
            file_path,
            encoding="utf-8",
            compression="zip",
        )

        criteria = {
            "main": "db_main",
            "references": "db_references",
            "cited_by": "db_cited_by",
        }[database]

        dataframe = dataframe[dataframe[criteria]]

        return dataframe

    def filter_records_by_year(records, year_filter):

        if year_filter is None:
            return records

        if not isinstance(year_filter, tuple):
            raise TypeError("The year_filter parameter must be a tuple of two values.")

        if len(year_filter) != 2:
            raise ValueError("The year_filter parameter must be a tuple of two values.")

        start_year, end_year = year_filter

        if start_year is not None:
            records = records[records.year >= start_year]

        if end_year is not None:
            records = records[records.year <= end_year]

        return records

    def filter_records_by_citations(records, cited_by_filter):

        if cited_by_filter is None:
            return records

        if not isinstance(cited_by_filter, tuple):
            raise TypeError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        if len(cited_by_filter) != 2:
            raise ValueError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        cited_by_min, cited_by_max = cited_by_filter

        if cited_by_min is not None:
            records = records[records.global_citations >= cited_by_min]

        if cited_by_max is not None:
            records = records[records.global_citations <= cited_by_max]

        return records

    def apply_filters_to_records(records, filters):

        if filters is None:
            return records

        for filter_name, filter_value in filters.items():

            if filter_name == "article":

                records = records[records["article"].isin(filter_value)]

            else:

                # Split the filter value into a list of strings
                database = records[["article", filter_name]]
                database.loc[:, filter_name] = database[filter_name].str.split(";")

                # Explode the list of strings into multiple rows
                database = database.explode(filter_name)

                # Remove leading and trailing whitespace from the strings
                database[filter_name] = database[filter_name].str.strip()

                # Keep only records that match the filter value
                database = database[database[filter_name].isin(filter_value)]
                records = records[records["article"].isin(database["article"])]

        return records

    def apply_sort_by(records, sort_by):
        #
        # sort_by: - date_newest
        #          - date_oldest
        #          - global_cited_by_highest
        #          - global_cited_by_lowest
        #          - local_cited_by_highest
        #          - local_cited_by_lowest
        #          - first_author_a_to_z
        #          - first_author_z_to_a
        #          - source_title_a_to_z
        #          - source_title_z_to_a

        if sort_by is None:
            return records

        if sort_by == "date_newest":
            records = records.sort_values(
                ["year", "global_citations", "local_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "date_oldest":
            records = records.sort_values(
                ["year", "global_citations", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "global_cited_by_highest":
            records = records.sort_values(
                ["global_citations", "year", "local_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "global_cited_by_lowest":
            records = records.sort_values(
                ["global_citations", "year", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "local_cited_by_highest":
            records = records.sort_values(
                ["local_citations", "year", "global_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "local_cited_by_lowest":
            records = records.sort_values(
                ["local_citations", "year", "global_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "first_author_a_to_z":
            records = records.sort_values(
                ["authors", "global_citations", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "first_author_z_to_a":
            records = records.sort_values(
                ["authors", "global_citations", "local_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "source_title_a_to_z":
            records = records.sort_values(
                ["source_title", "global_citations", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "source_title_z_to_a":
            records = records.sort_values(
                ["source_title", "global_citations", "local_citations"],
                ascending=[False, False, False],
            )

        return records

    records = get_records_from_file(root_dir, database)
    records = filter_records_by_year(records, record_years_range)
    records = filter_records_by_citations(records, record_citations_range)
    records = apply_filters_to_records(records, records_match)
    records = apply_sort_by(records, records_order_by)

    return records
