import pandas as pd

# Consolidate stopwords and common terms under single header
#
# Load COMMON_AND_BASIC_THESAURUS:
#   Structure:
#     #COMMON_AND_BASIC
#         the
#         a
#         an
#         of
#         in
#         on
#         at
#         to
#         for
#         with
#         by
#         ... (hundreds of entries)
#
# For each key in descriptor thesaurus:
#   1. Search in common/basic thesaurus
#
#   2. If key is listed as variant under #COMMON_AND_BASIC:
#      a. Remove key from descriptor thesaurus
#      b. Add to variants under "#COMMON_AND_BASIC" consolidated header
#
#   3. If not found:
#      - Keep key as-is
#
#
# Before:
#
# the
#     the
# machine learning
#     machine learning
# of
#     of
# neural networks
#     neural networks
# a
#     a
# in
#     in
# deep learning
#     deep learning
#
# After:
#
# #COMMON_AND_BASIC
#     the
#     of
#     a
#     in
# machine learning
#     machine learning
# neural networks
#     neural networks
# deep learning
#     deep learning


def common_and_basic(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
