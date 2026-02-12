import pandas as pd

#
# Remove common stopwords to find semantic matches that differ
# only by articles, prepositions, and other "noise" words.
#
# STOPWORDS = ["a", "an", "the", "of", "in", "on", "at", "to", "for",
#              "with", "by", "from", "as", "is", "was", "are", "were"]
#
# For each key in thesaurus:
#   1. Tokenize into words
#
#   2. Remove stopwords:
#      "analysis of data" → ["analysis", "data"]
#      "the neural network" → ["neural", "network"]
#
#   3. Create stopword-free signature:
#      "analysis of data" → signature: "analysis data"
#      "data analysis" → signature: "analysis data" (after sorting)
#
#   4. Group keys by signature
#
#   5. For each group with multiple keys:
#      Present to user for review
#      User selects preferred form
#      Merge variants under preferred
#


def stopwords_removal_match(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
