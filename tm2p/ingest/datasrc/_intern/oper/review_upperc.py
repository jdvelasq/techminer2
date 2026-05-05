import re
import sys
from typing import Optional

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from tm2p._intern import stdout_to_stderr
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import Field

from ._file_dispatch import get_file_operations
from .helpers import (
    extract_urls,
    join_consecutive_descriptors,
    mark_abstract_headings,
    mark_copyright,
    mark_discursive_patterns,
    mark_scaffolding,
    remove_single_academic_terms,
    remove_single_word_noise,
    repair_abstract_headings,
    repair_apostrophes,
    repair_emails,
    repair_et_al,
    repair_lowercase_text,
    repair_measurement_units,
    repair_roman_numbers,
    repair_strange_cases,
    repair_urls,
)

# ----------------------------------------------------------------------------


def review_upperc(
    source: Field,
    target: Field,
    root_directory: str,
    na_action: Optional[str] = None,
) -> int:

    load_data, save_data, get_path = get_file_operations()

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        if na_action == "ignore":
            return 0
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    dataframe[target.value] = dataframe[source.value].copy()
    dataframe[target.value] = dataframe[target.value].map(
        lambda x: f" {x} " if pd.notna(x) else x
    )

    uppercase_terms = (
        dataframe[target.value]
        .str.extractall(r" ([A-Z_]+) ")[0]
        .drop_duplicates()
        .to_list()
    )

    for term in uppercase_terms:
        term_upper = term.strip()
        term_lower = term_upper.lower().replace("_", " ")
        dataframe[target.value] = dataframe[target.value].str.replace(
            rf" {term_lower} ", f" {term_upper} "
        )

    dataframe[target.value] = dataframe[target.value].str.strip()

    save_data(df=dataframe, root_directory=root_directory)

    return int(dataframe[target.value].notna().sum())
