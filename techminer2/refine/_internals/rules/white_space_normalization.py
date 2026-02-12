import pandas as pd

# For each key in thesaurus:
#   Trim leading/trailing whitespace
#   Replace multiple consecutive whitespace with single space
#
#   If key changed:
#     Search for normalized version
#     If exists: merge
#     If not: update key


def white_space_normalization(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
