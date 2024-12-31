# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

import pandas as pd  # type: ignore


def _get_context_phrases_from_records(
    search_for: str,
    records: pd.DataFrame,
):
    #
    # Returns the abstract phrases containing the searched text
    #
    records = records.set_index(pd.Index(records.article + " / " + records.raw_document_title))
    sorted_records = records.sort_values(
        ["global_citations", "local_citations", "year"],
        ascending=[False, False, True],
    )
    sorted_records["_found_"] = sorted_records["abstract"].astype(str).str.contains(r"\b" + search_for + r"\b", regex=True)
    sorted_records = sorted_records[sorted_records["_found_"]]
    abstracts = sorted_records["abstract"]
    phrases = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
    context_phrases = phrases[phrases.map(lambda x: search_for in x)]

    return context_phrases
