import pandas as pd  # type: ignore

from tm2p._intern.packag_data.word_lists.load_builtin_word_list import (
    load_builtin_word_list,
)

WORDS = [
    t
    for t in load_builtin_word_list("scientific_and_academic.txt")
    if len(t.split(" ")) == 1
]


def remove_single_academic_terms(text) -> str:

    if pd.isna(text):
        return ""
    text = str(text)

    for unit in WORDS:
        text = text.replace(f" {unit.upper()} ", f" {unit.lower()} ")

    return text
