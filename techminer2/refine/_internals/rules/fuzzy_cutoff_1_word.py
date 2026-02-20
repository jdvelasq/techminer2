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

#
# For each pair of keys (i, j):
#
#   1. Tokenize both into words
#
#   2. Check if same number of words:
#      If not: skip (different structure)
#
#   3. Align words position-by-position
#
#   4. Count differences:
#      - Exact matches: word[i] == word[j]
#      - Fuzzy matches: similarity(word[i], word[j]) >= WORD_CUTOFF
#      - Mismatches: neither exact nor fuzzy
#
#   5. If exactly ONE word differs:
#      And that word is fuzzy-similar (or completely different)
#      Add to candidates
#
# What it catches:
#
# ONE WORD DIFFERS (COMPLETELY):
#
# "neural network model" vs "neural network system"
#   → Word 1: "neural" = "neural" ✓ exact match
#   → Word 2: "network" = "network" ✓ exact match
#   → Word 3: "model" ≠ "system" ✗ DIFFERENT
#   → Exactly 1 word differs → CANDIDATE MATCH
#
# "support vector machine" vs "support vector classifier"
#   → Words 1-2: exact match
#   → Word 3: "machine" ≠ "classifier"
#   → Exactly 1 word differs → CANDIDATE MATCH
#
# "deep learning algorithm" vs "deep learning method"
#   → Words 1-2: exact match
#   → Word 3: "algorithm" ≠ "method"
#   → Exactly 1 word differs → CANDIDATE MATCH
#
# ONE WORD DIFFERS (FUZZY):
#
# "neural network model" vs "neural netowrk model"
#   → Word 1: "neural" = "neural" ✓
#   → Word 2: "network" vs "netowrk" → 85% similar → FUZZY MATCH ✓
#   → Word 3: "model" = "model" ✓
#   → Exactly 1 word fuzzy → CANDIDATE MATCH
#
# "machine learning system" vs "machine learing system"
#   → Word 1: "machine" = "machine" ✓
#   → Word 2: "learning" vs "learing" → 87% similar → FUZZY MATCH ✓
#   → Word 3: "system" = "system" ✓
#   → Exactly 1 word fuzzy → CANDIDATE MATCH
#
#
# What it MISSES:
#
# TWO OR MORE WORDS DIFFER:
#
# "neural network model" vs "deep learning system"
#   → All 3 words different
#   → Not "exactly one word differs" → NO MATCH
#
# DIFFERENT NUMBER OF WORDS:
#
# "neural network" vs "neural network model"
#   → 2 words vs 3 words
#   → Can't align → NO MATCH
#
# (This might be caught by other matchers like AbbreviationMatch)
#
# SINGLE WORD TERMS:
#
# "network" vs "netowrk"
#   → Only 1 word total
#   → Not multi-word phrase → NO MATCH
#
# (This would be caught by standard FuzzyCutoffMatch)
#
# Best for:
#
# Semantic variants with one different word
# Synonyms in multi-word phrases
# Domain-specific terminology variations
# Requires DOMAIN EXPERTISE to review
#


def apply_fuzzy_cutoff_1_word_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #

    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
