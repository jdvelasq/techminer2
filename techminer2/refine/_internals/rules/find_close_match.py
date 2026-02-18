import pandas as pd

from techminer2._internals import Params
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

# User selects target string from thesaurus
# User sets similarity threshold (e.g., 80%)
#
# For each other key in thesaurus:
#   Calculate similarity to target
#   If similarity >= threshold:
#     Add to candidates
#
# Present candidates to user for review
#
# User selects: "machine learning" Threshold: 80%
#
# machine learning (target)
#   vs machine learing → 94% similar [TYPO]
#   vs machine learining → 88% similar [TYPO]
#   vs machinelearning → 88% similar [SPACING ERROR]
#   vs machine-learning → already merged by HyphenationMatch
#
# For each pair of keys (i, j):
#   Calculate Levenshtein distance (character-level)
#   Similarity = (1 - distance / max_length) × 100
#
#   If similarity >= CUTOFF (e.g., 85%):
#     Add to candidates
#
# What it catches:
#
# TYPOS AND MINOR VARIATIONS:
#
# "machine learning" vs "machine learing"
#   → Distance: 1 character
#   → Similarity: 94%
#   → Above 85% cutoff → MATCH
#
# "neural network" vs "nueral network"
#   → Distance: 2 characters (transposition)
#   → Similarity: 87%
#   → Above 85% cutoff → MATCH
#
# "deep learning" vs "deep lerning"
#   → Distance: 1 character
#   → Similarity: 92%
#   → Above 85% cutoff → MATCH
#
# What it MISSES:
#
# MULTI-WORD REORDERING:
#
# "machine learning deep" vs "deep machine learning"
#   → Character distance: very high
#   → Similarity: ~60%
#   → Below 85% cutoff → NO MATCH
#
# (This is caught by WordOrderMatch instead)
#
# SINGLE WORD DIFFERENCES IN MULTI-WORD PHRASES:
#
# "support vector machine" vs "support vector machines"
#   → Distance: 1 character (just 's')
#   → Length: 23 characters
#   → Similarity: 96%
#   → Above 85% → MATCH ✓
#
# BUT:
#
# "neural network model" vs "neural network system"
#   → Different last word entirely
#   → Distance: 5-6 characters
#   → Length: ~20 characters
#   → Similarity: ~70%
#   → Below 85% cutoff → NO MATCH ✗
#


def apply_find_close_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #

    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
