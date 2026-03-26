import pandas as pd  # type: ignore

from tm2p import ThField

SIGNATURE = ThField.SIGNATURE.value


def remove_punctuation(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
        r"[^\w\s]", "", regex=True
    )

    return thesaurus_df
