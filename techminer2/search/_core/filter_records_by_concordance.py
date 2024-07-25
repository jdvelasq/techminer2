# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

import pandas as pd  #  type: ignore


def _filter_records_by_concordance(
    search_for: str,
    records: pd.DataFrame,
):
    #
    # Returns the abstract phrases containing the searched text
    #
    records = records.copy()
    found = records["abstract"].astype(str).str.contains(r"\b" + search_for + r"\b", regex=True)
    records = records[found]
    return records
