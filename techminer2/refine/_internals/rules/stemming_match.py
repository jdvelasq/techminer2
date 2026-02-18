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


# Use STEMMING_ALGORITHM (Porter Stemmer or similar)
#
# For each key in thesaurus:
#   1. Tokenize key into words
#
#   2. Stem each word:
#      - "optimization" → "optim"
#      - "optimizing" → "optim"
#      - "optimized" → "optim"
#      - "neural" → "neural"
#      - "network" → "network"
#
#   3. Create stemmed version of key:
#      - "optimization algorithm" → "optim algorithm"
#
#   4. Search thesaurus for other keys with same stem
#
#   5. If multiple keys share stem:
#      a. Select preferred form:
#         - Shortest common form
#         - Or most frequent form
#         - "optimization" preferred over "optimizing"
#
#      b. Merge all under preferred form
#
# Before:
#
# optimization
#     optimization
# optimize
#     optimize
# optimizing
#     optimizing
# optimized
#     optimized
# neural network
#     neural network
# learning
#     learning
# learned
#     learned
# learner
#     learner
#
# After:
#
# optimization
#     optimization
#     optimize
#     optimizing
#     optimized
# neural network
#     neural network
# learning
#     learning
#     learned
#     learner


def apply_stemming_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #

    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
