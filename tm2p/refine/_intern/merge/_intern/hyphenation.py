# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import ThField

PREFERRED = ThField.PREFERRED.value


def apply_hyphenation_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = _add_padding(thesaurus_df[PREFERRED])

    thesaurus_df[PREFERRED] = _replace_hyphen_by_space(thesaurus_df[PREFERRED])

    thesaurus_df[PREFERRED] = _replace_with_valid_hyphenated_words(
        thesaurus_df[PREFERRED]
    )

    thesaurus_df[PREFERRED] = _replace_with_valid_individual_words(
        thesaurus_df[PREFERRED]
    )

    thesaurus_df[PREFERRED] = _remove_padding(thesaurus_df[PREFERRED])

    return thesaurus_df


def _add_padding(series):
    return series.str.replace(r"\s+", " ", regex=True).apply(lambda x: f" {x} ")


def _remove_padding(series):
    return series.str.replace(r"\s+", " ", regex=True).str.strip()


def _replace_hyphen_by_space(series):
    return series.str.replace("-", " ", regex=False)


def _replace_with_valid_hyphenated_words(series):

    valid_hyphenated_words = load_builtin_word_list("hyphen_corect_words.txt")

    for valid_word in valid_hyphenated_words:
        pattern = f" {valid_word.replace('-', '')} "
        replacement = f" {valid_word} "
        series = series.str.replace(pattern, replacement, regex=False)

    return series


def _replace_with_valid_individual_words(series):

    valid_individual_words = load_builtin_word_list("hyphen_individual_words.txt")

    for valid_word in valid_individual_words:
        pattern = f" {valid_word.replace('-', '')} "
        replacement = f" {valid_word.replace('-', ' ')} "
        series = series.str.replace(pattern, replacement, regex=False)

    return series
