import pandas as pd

from techminer2._internals import Params
from techminer2._internals.package_data.word_lists import load_builtin_word_list
from techminer2.enums import ThesaurusField

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


def apply_hyphenation_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    valid_hyphenated_words = load_builtin_word_list("valid_hyphenated_words.txt")

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
        r"\s+", " ", regex=True
    )
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(lambda x: f" {x} ")
    for valid_word in valid_hyphenated_words:
        pattern = f" {valid_word.replace('-', ' ')} "
        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            pattern, f" {valid_word} ", regex=True
        )
        pattern = f" {valid_word.replace('-', '')} "
        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            pattern, f" {valid_word} ", regex=True
        )
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
