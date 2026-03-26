import pandas as pd  # type: ignore

from tm2p import ThField

SIGNATURE = ThField.SIGNATURE.value


def string_to_words(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split(" ")

    return thesaurus_df
