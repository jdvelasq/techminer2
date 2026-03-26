import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern.packag_data import load_builtin_word_list

SIGNATURE = ThField.SIGNATURE.value


def remove_builtin_stopwords(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()

    stopwords = load_builtin_word_list("stopwords.txt")
    for stopword in stopwords:
        thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
            f" {stopword} ", " "
        )
        thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
            f" {stopword} ", " "
        )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
        r"\s+", " ", regex=True
    )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df = thesaurus_df[thesaurus_df[SIGNATURE].str.len() > 0]  # type: ignore

    return thesaurus_df
