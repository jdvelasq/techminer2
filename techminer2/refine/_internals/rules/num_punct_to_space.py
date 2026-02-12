import pandas as pd

# For each key in thesaurus:
#   1. Get first character of key
#   2. If first character is:
#      - Number (0-9) → Mark for removal
#      - Punctuation (.,;:!?-) → Mark for removal
#      - Alphabetic (a-z, A-Z) → Keep
#   3. Remove marked keys from thesauruss
#
# Before:
#
# 3d printing
#     3d printing
# machine learning
#     machine learning
# -based methods
#     -based methods
# neural networks
#     neural networks
# (artificial intelligence)
#     (artificial intelligence)
#
# After:
#
# machine learning
#     machine learning
# neural networks
#     neural networks


def num_punct_to_space(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
