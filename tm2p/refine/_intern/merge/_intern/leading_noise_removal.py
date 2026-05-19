# pylint: disable=unused-argument

import ahocorasick  # type: ignore
import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import ThField

IS_KEYWORD = ThField.IS_KEYWORD.value
PREFERRED = ThField.PREFERRED.value
OLD = ThField.OLD.value


def _initialize_ahocorasick_automaton():

    automaton = ahocorasick.Automaton()  # type: ignore  # pylint: disable=c-extension-no-member

    for file in [
        "stopwords.txt",
        "determiners.txt",
        "common_initial_words.txt",
    ]:
        for phrase in load_builtin_word_list(file):
            automaton.add_word(phrase.lower(), phrase)

    automaton.make_automaton()

    return automaton


AHOCORASICK = _initialize_ahocorasick_automaton()


def _extract_scaffolding(text):
    text_lower = text.lower()
    seen_positions = {}
    for end_idx, phrase in AHOCORASICK.iter(text_lower):
        start_idx = end_idx - len(phrase) + 1
        if start_idx not in seen_positions or len(phrase) > len(
            seen_positions[start_idx][0]
        ):
            seen_positions[start_idx] = (phrase, end_idx)
    result = []
    last_end = -1
    for start in sorted(seen_positions):
        phrase, end_idx = seen_positions[start]
        if start >= last_end:
            result.append(phrase)
            last_end = end_idx + 1
    return result


def _process(term):

    scaffolding_phrases = _extract_scaffolding(term)
    words = term.split(" ")
    selected_index = 0

    for index, word in enumerate(words[:-1]):
        if word in scaffolding_phrases:
            selected_index = index + 1
        else:
            break

    words = words[selected_index:]
    term = " ".join(words)

    assert term.strip() != ""

    return term


def apply_leading_noise_removal_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[OLD] = thesaurus_df[PREFERRED]
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(_process)
    # is_keyword = thesaurus_df[IS_KEYWORD]
    # thesaurus_df.loc[is_keyword, PREFERRED] = thesaurus_df.loc[is_keyword, OLD]

    thesaurus_df.pop(OLD)

    return thesaurus_df
