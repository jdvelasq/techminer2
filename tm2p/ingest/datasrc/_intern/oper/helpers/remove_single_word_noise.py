import pandas as pd  # type: ignore

from tm2p._intern.packag_data.word_lists.load_builtin_word_list import (
    load_builtin_word_list,
)

WORDS = load_builtin_word_list("single_word_noise.txt")


def remove_single_word_noise(text) -> str:

    if pd.isna(text):
        return ""
    text = str(text)

    for unit in WORDS:
        text = text.replace(f" {unit.upper()} ", f" {unit.lower()} ")
        text = text.replace(f" {unit.upper()}_", f" {unit.lower()} ")
        text = text.replace(f"_{unit.upper()} ", f" {unit.lower()} ")

    return text
