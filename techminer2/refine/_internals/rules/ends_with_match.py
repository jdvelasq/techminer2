import pandas as pd

# User provides suffix pattern (similar to begins with)
#
# For each key in thesaurus:
#   If key ends with pattern:
#     Add to candidate list
#
# Present candidates to user


def ends_with_match(dataframe: pd.DataFrame, pattern: str) -> pd.DataFrame:
    return dataframe
