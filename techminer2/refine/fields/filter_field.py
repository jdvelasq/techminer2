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

>>> from techminer2.refine.fields import filter_field, delete_field
>>> filter_field(
...     src_field="author_keywords",
...     dst_field="author_keywords_filtered",
...     #
...     # FILTERS:
...     metric="OCC",
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='author_keywords_filtered',
...     metric='OCC',
...     root_dir="example/", 
... ).df_['OCC']
author_keywords_filtered
REGTECH                    28
FINTECH                    12
REGULATORY_TECHNOLOGY       7
COMPLIANCE                  7
ANTI_MONEY_LAUNDERING       6
REGULATORS                  5
FINANCIAL_SERVICES          4
DATA_PROTECTION             4
FINANCIAL_REGULATION        4
ARTIFICIAL_INTELLIGENCE     4
Name: OCC, dtype: int64

>>> delete_field(
...     field="author_keywords_filtered",
...     root_dir="example",
... )




>>> filter_field(
...     src_field="author_keywords",
...     dst_field="author_keywords_filtered",
...     #
...     # FILTERS:
...     metric="OCC",
...     top_n=10,
...     occ_range=(5, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='author_keywords_filtered',
...     metric='OCC',
...     root_dir="example/", 
... ).df_['OCC']
author_keywords_filtered
REGTECH                  28
FINTECH                  12
REGULATORY_TECHNOLOGY     7
COMPLIANCE                7
ANTI_MONEY_LAUNDERING     6
REGULATORS                5
Name: OCC, dtype: int64

>>> delete_field(
...     field="author_keywords_filtered",
...     root_dir="example",
... )





>>> filter_field(
...     src_field="author_keywords",
...     dst_field="author_keywords_filtered",
...     #
...     # FILTERS:
...     metric="OCC",
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
...     year_filter=(2019, 2022),
...     cited_by_filter=(None, None),
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='author_keywords_filtered',
...     metric='OCC',
...     root_dir="example/", 
... ).df_['OCC']
author_keywords_filtered
REGTECH                    21
FINTECH                    10
REGULATORY_TECHNOLOGY       7
ANTI_MONEY_LAUNDERING       6
COMPLIANCE                  6
DATA_PROTECTION             4
ARTIFICIAL_INTELLIGENCE     4
FINANCIAL_REGULATION        3
INNOVATION                  3
NEW_TECHNOLOGIES            3
Name: OCC, dtype: int64

>>> delete_field(
...     field="author_keywords_filtered",
...     root_dir="example",
... )



"""
import glob
import os.path

import pandas as pd

from ...analyze import performance_metrics
from .protected_fields import PROTECTED_FIELDS


def filter_field(
    src_field,
    dst_field,
    #
    # FILTERS:
    metric=None,
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """
    :meta private:
    """
    if dst_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dst_field}` is protected")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # If src_field is not in the database, continue with the next database
        data_full = pd.read_csv(file, encoding="utf-8", compression="zip")
        if src_field not in data_full.columns:
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

        data_frame = performance_metrics(
            #
            # PERFORMANCE PARAMS:
            field=src_field,
            metric=metric,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        valid_items = data_frame.df_.index.tolist()

        #
        # Filter by year
        data_filtered = data_full.copy()
        if year_filter is not None:
            start_year, end_year = year_filter
            if start_year is not None:
                data_filtered = data_filtered[data_filtered.year >= start_year]
            if end_year is not None:
                data_filtered = data_filtered[data_filtered.year <= end_year]

        #
        # Filter by citations
        if cited_by_filter is not None:
            cited_by_min, cited_by_max = cited_by_filter
            if cited_by_min is not None:
                data_filtered = data_filtered[data_filtered.global_citations >= cited_by_min]
            if cited_by_max is not None:
                data_filtered = data_filtered[data_filtered.global_citations <= cited_by_max]

        #
        # Filter by other fields
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
                data_filtered = data_filtered[data_filtered["article"].isin(database["article"])]

        #
        # Extracts valida values for the new field
        data_full[dst_field] = pd.NA

        idx = data_filtered.index.copy()
        data_full.loc[idx, dst_field] = data_full.loc[idx, src_field].copy()
        data_full.loc[idx, dst_field] = data_full.loc[idx, dst_field].map(
            lambda w: w.split("; "), na_action="ignore"
        )
        data_full.loc[idx, dst_field] = data_full.loc[idx, dst_field].map(
            lambda ws: [w for w in ws if w in valid_items], na_action="ignore"
        )
        data_full.loc[idx, dst_field] = data_full.loc[idx, dst_field].map(
            lambda ws: "; ".join(ws) if isinstance(ws, list) else ws,
            na_action="ignore",
        )

        #
        # Saves the database with the new field
        data_full.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
