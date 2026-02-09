import pandas as pd  # type: ignore

from techminer2 import CorpusField


def remove_empty_terms(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.split("; ")
        dataframe[col] = dataframe[col].apply(
            lambda x: [z for z in x if z.strip() != ""] if isinstance(x, list) else x
        )
        dataframe[col] = dataframe[col].str.join("; ")

    return dataframe
