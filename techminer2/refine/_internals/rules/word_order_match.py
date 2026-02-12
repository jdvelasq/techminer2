import pandas as pd

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


def word_order_match(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
