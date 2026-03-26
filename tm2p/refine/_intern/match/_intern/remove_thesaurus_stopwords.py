import pandas as pd  # type: ignore

from tm2p import ThField

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value


def remove_thesaurus_stopwords(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    return thesaurus_df[~thesaurus_df[PREFERRED].str.startswith("#").values].copy()  # type: ignore
