import pandas as pd

# For each key in thesaurus:
#
#   If key contains hyphen:
#     Create space version: "machine-learning" → "machine learning"
#     Search for space version in thesaurus
#     If exists: merge hyphenated under space version
#     If not: keep hyphenated
#
#   If key contains spaces (no hyphen):
#     Create hyphen version: "machine learning" → "machine-learning"
#     Search for hyphen version in thesaurus
#     If exists: merge hyphenated under space version
#     If not: keep space version
#
# Preferred form: SPACE-SEPARATED
#
# Before:
#
# machine-learning
#     machine-learning
# machine learning
#     machine learning
# state-of-the-art
#     state-of-the-art
# co-author
#     co-author
#
# After:
#
# machine learning
#     machine learning
#     machine-learning
# state of the art
#     state of the art
#     state-of-the-art
# co author
#     co author
#     co-author
#


def hyphenation_match(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
