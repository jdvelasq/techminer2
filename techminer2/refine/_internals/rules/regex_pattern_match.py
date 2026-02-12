import pandas as pd

#
# User provides regex pattern
#
# For each key in thesaurus:
#   If key matches regex:
#     Add to candidate list
#
# Present candidates to user
#
# Candidates:
#
# test 1
#     test 1
# test 2
#     test 2
# test 10
#     test 10
# benchmark test 1
#     benchmark test 1
#
# User regex: \btest \d+\b (find "test" followed by number)
#


def regex_pattern_match(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
