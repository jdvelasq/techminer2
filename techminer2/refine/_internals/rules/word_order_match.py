import pandas as pd  # type: ignore

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
#
#   1. Tokenize key into words
#
#   2. Sort words alphabetically:
#      - "deep neural networks" → ["deep", "neural", "networks"]
#      - Sorted: ["deep", "neural", "networks"]
#      - Signature: "deep neural networks"
#
#   3. Create word signature (sorted word list)
#
#   4. Search thesaurus for other keys with same signature
#
#   5. If multiple keys share signature:
#      a. Select preferred form:
#         - Most frequent word order in corpus
#         - Or alphabetical order
#         - Or user-specified preference
#
#      b. Present to user for review (HIGH RISK)
#
#      c. If confirmed: merge under preferred form
#
# Before:
#
# deep neural networks
#     deep neural networks
# neural networks deep
#     neural networks deep
# networks neural deep
#     networks neural deep
# machine learning
#     machine learning
#
# After:
#
# deep neural networks
#     deep neural networks
#     neural networks deep
#     networks neural deep
#
# machine learning
#     machine learning
#
# WHY HIGH RISK:
#
# "machine learning" ≠ "learning machine" (different concepts)
# "vector support machine" ≠ "support vector machine" (one is incorrect)
# Requires user domain knowledge to confirm


def apply_word_order_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    #
    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED]
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split(" ")
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(sorted)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join(" ")
    #
    mapping_df = thesaurus_df[[SIGNATURE, PREFERRED]].copy()
    mapping_df = mapping_df.drop_duplicates()
    mapping = {
        signature: preferred
        for signature, preferred in zip(
            mapping_df[SIGNATURE].values, mapping_df[PREFERRED].values
        )
    }
    thesaurus_df[PREFERRED] = thesaurus_df[SIGNATURE].apply(lambda x: mapping.get(x, x))
    #
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
