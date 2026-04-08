import pandas as pd  # type: ignore

from tm2p.enum import ThField

SIGNATURE = ThField.SIGNATURE.value


def words_to_string(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join(" ")
    return thesaurus_df
