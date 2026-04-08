import pandas as pd  # type: ignore

from tm2p.enum import ThField

SIGNATURE = ThField.SIGNATURE.value


def remove_padding(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()

    return thesaurus_df
