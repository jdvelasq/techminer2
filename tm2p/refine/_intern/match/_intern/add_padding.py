import pandas as pd  # type: ignore

from tm2p.enum import ThField

SIGNATURE = ThField.SIGNATURE.value


def add_padding(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[SIGNATURE] = " " + thesaurus_df[SIGNATURE] + " "

    return thesaurus_df
