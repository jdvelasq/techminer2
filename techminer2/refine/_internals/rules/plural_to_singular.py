import pandas as pd  # type: ignore
from textblob import Word  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import Params

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


# For each key in thesaurus:
#   1. Detect if key is plural (English rules):
#      - Ends in "s" (but not "ss", "us", "is")
#      - Ends in "ies" → singular ends in "y"
#      - Ends in "es" → check if singular form valid
#      - Irregular: "data" → "datum", "criteria" → "criterion"
#
#   2. If plural detected:
#      a. Generate singular form:
#         - "networks" → "network"
#         - "studies" → "study"
#         - "analyses" → "analysis"
#
#      b. Search thesaurus for singular form
#
#      c. If singular exists:
#         - Merge plural under singular (preferred: singular)
#
#      d. If singular doesn't exist:
#         - Keep plural as-is (might be only form in corpus)
#
#   3. If singular:
#      a. Generate plural form
#      b. Search thesaurus for plural
#      c. If plural exists:
#         - Merge plural under singular


def apply_plural_to_singular_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[SIGNATURE] = thesaurus_df[VARIANT].copy()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split("; ")
    thesaurus_df[PREFERRED] = thesaurus_df.apply(_prefer_singular_over_plural, axis=1)
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df


def _prefer_singular_over_plural(row):

    preferred = row[PREFERRED]
    preferred = preferred.split(" ")
    last_word = preferred[-1]
    singular_last_word = Word(last_word).singularize()
    singular_preferred = " ".join(preferred[:-1] + [singular_last_word])
    if singular_preferred in row[VARIANT].split("; "):
        return singular_preferred

    return row[PREFERRED]
