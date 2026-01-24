import re

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from techminer2._internals import stdout_to_stderr
from techminer2._internals.package_data.text_processing import (
    load_text_processing_terms,
)

with stdout_to_stderr():
    pandarallel.initialize(progress_bar=True)


_COMPILED_PATTERNS: list[tuple[str, re.Pattern]] = []


def _get_compiled_patterns() -> list[tuple[str, re.Pattern]]:
    if not _COMPILED_PATTERNS:
        patterns = load_text_processing_terms("discursive_patterns.txt")
        _COMPILED_PATTERNS.extend(
            (phrase, re.compile(r"\b(" + re.escape(phrase) + r")\b"))
            for phrase in patterns
        )
    return _COMPILED_PATTERNS


def mark_discursive_patterns(text):
    if pd.isna(text):
        return text
    text = str(text)
    for phrase, pattern in _get_compiled_patterns():
        if phrase in text:
            text = pattern.sub(lambda m: m.group().lower().replace(" ", "_"), text)
    return text
