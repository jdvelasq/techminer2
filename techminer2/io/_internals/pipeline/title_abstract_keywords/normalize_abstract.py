from pathlib import Path

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from techminer2._internals import stdout_to_stderr
from techminer2.io._internals.operators import copy_column

from .helpers import (
    extract_urls,
    join_consecutive_descriptors,
    mark_abstract_headings,
    mark_connectors,
    mark_copyright,
    mark_discursive_patterns,
    normalize_descriptors,
    repair_abstract_headings,
    repair_apostrophes,
    repair_emails,
    repair_et_al,
    repair_isbn_issn,
    repair_lowercase_text,
    repair_measurement_units,
    repair_roman_numbers,
    repair_strange_cases,
)


def _normalize_text(text: str) -> str:

    urls = extract_urls(text)

    text = mark_copyright(text)
    text = mark_abstract_headings(text)
    text = mark_discursive_patterns(text)
    text = mark_connectors(text)
    text = normalize_descriptors(text)
    text = repair_apostrophes(text)
    text = join_consecutive_descriptors(text)
    text = repair_measurement_units(text)
    text = repair_lowercase_text(text)
    text = repair_abstract_headings(text)
    text = repair_et_al(text)
    text = mark_connectors(text)
    text = repair_roman_numbers(text)
    text = repair_emails(text)
    text = repair_isbn_issn(text)
    text = repair_strange_cases(text)

    return text


def normalize_abstract(source: str, target: str, root_directory: str) -> int:
    """Run authors importer."""

    copy_column(
        source=source,
        target=target,
        root_directory=root_directory,
    )

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return 0

    with stdout_to_stderr():
        pandarallel.initialize(progress_bar=True)
        dataframe[target] = dataframe[source].parallel_apply(_normalize_text)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())
