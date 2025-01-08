# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""
Filter a Field
===============================================================================

## >>> from techminer2.fields import filter_field
## >>> filter_field(  # doctest: +SKIP 
## ...     source="author_keywords",
## ...     dest="author_keywords_filtered",
## ...     filter_params = {
## ...         "metric": 'OCCGC',
## ...         "top_n": 10,
## ...         "occ_range": (None, None),
## ...         "gc_range": (None, None),
## ...         "custom_items": None,
## ...     },
## ...     database_params = {
## ...         "root_dir": "example/",
## ...         "database": "main",
## ...         "year_filter": (None, None),
## ...         "cited_by_filter": (None, None),
## ...     }
## ... )


"""
import glob
import os.path

import pandas as pd  # type: ignore

from ..._dtypes import DTYPES
from ...analyze.metrics import performance_metrics_frame
from .operations__protected_fields import PROTECTED_FIELDS


def operations__filter(
    source,
    dest,
    filter_params,
    database_params,
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    files = list(
        glob.glob(os.path.join(database_params["root_dir"], "databases/_*.zip"))
    )
    for file in files:
        #
        # If src_field is not in the database, continue with the next database
        data_full = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)
        if source not in data_full.columns:
            continue

        #
        # Extracts valid values for the field
        if file.endswith("_cited_by.csv.zip"):
            database = "cited_by"
        elif file.endswith("_main.csv.zip"):
            database = "main"
        elif file.endswith("_references.csv.zip"):
            database = "references"
        else:
            raise ValueError(f"Internal error: unknown database {file}")

        data_frame = performance_metrics_frame(
            field=source,
            filter_params=filter_params,
            database_params=database_params,
        )
        valid_items = data_frame.index.tolist()

        #
        # Filter by year
        data_filtered = data_full.copy()
        if database_params["year_filter"] is not None:
            start_year, end_year = database_params["year_filter"]
            if start_year is not None:
                data_filtered = data_filtered[data_filtered.year >= start_year]
            if end_year is not None:
                data_filtered = data_filtered[data_filtered.year <= end_year]

        #
        # Filter by citations
        if database_params["cited_by_filter"] is not None:
            cited_by_min, cited_by_max = database_params["cited_by_filter"]
            if cited_by_min is not None:
                data_filtered = data_filtered[
                    data_filtered.global_citations >= cited_by_min
                ]
            if cited_by_max is not None:
                data_filtered = data_filtered[
                    data_filtered.global_citations <= cited_by_max
                ]

        #
        # Filter by other fields
        filters = database_params["filters"]
        if len(filters.items()):
            for filter_name, filter_value in filters.items():
                # Split the filter value into a list of strings
                database = data_filtered[["article", filter_name]]
                database[filter_name] = database[filter_name].str.split(";")

                # Explode the list of strings into multiple rows
                database = database.explode(filter_name)

                # Remove leading and trailing whitespace from the strings
                database[filter_name] = database[filter_name].str.strip()

                # Keep only records that match the filter value
                database = database[database[filter_name].isin(filter_value)]
                data_filtered = data_filtered[
                    data_filtered["article"].isin(database["article"])
                ]

        #
        # Extracts valida values for the new field
        data_full[dest] = pd.NA

        idx = data_filtered.index.copy()
        data_full.loc[idx, dest] = data_full.loc[idx, source].copy()
        data_full.loc[idx, dest] = data_full.loc[idx, dest].map(
            lambda w: w.split("; "), na_action="ignore"
        )
        data_full.loc[idx, dest] = data_full.loc[idx, dest].map(
            lambda ws: [w for w in ws if w in valid_items], na_action="ignore"
        )
        data_full.loc[idx, dest] = data_full.loc[idx, dest].map(
            lambda ws: "; ".join(ws) if isinstance(ws, list) else ws,
            na_action="ignore",
        )

        #
        # Saves the database with the new field
        data_full.to_csv(
            file, sep=",", encoding="utf-8", index=False, compression="zip"
        )
