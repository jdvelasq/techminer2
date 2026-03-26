import pandas as pd  # type: ignore

from tm2p import ThField

SIGNATURE = ThField.SIGNATURE.value


def sort_words(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(set)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(sorted)
    return thesaurus_df
