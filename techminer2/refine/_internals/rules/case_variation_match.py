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
#   1. Create lowercase version of key
#
#   2. Search thesaurus for other keys with same lowercase form
#
#   3. If multiple keys with same lowercase:
#      a. Select preferred form:
#         - Prefer lowercase version
#         - Unless key is likely acronym (all uppercase, ≤4 chars)
#
#      b. Merge all variants under preferred form
#
#   4. If only one key with this lowercase:
#      - Keep as-is
#
# Before:
#
# Machine Learning
#     Machine Learning
# machine learning
#     machine learning
# MACHINE LEARNING
#     MACHINE LEARNING
# ML
#     ML
# Neural Networks
#     Neural Networks
# neural networks
#     neural networks
#
# After:
#
# machine learning
#     machine learning
#     Machine Learning
#     MACHINE LEARNING
# ML
#     ML
# neural networks
#     neural networks
#     Neural Networks


def apply_case_variation_match_rule(
    thesaurus_df: pd.DataFrame, params: Params
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    #

    #
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
