import pandas as pd  # type: ignore

from techminer2 import CorpusField


def normalize_quotes(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.replace("ʿ", "'", regex=False)
        dataframe[col] = dataframe[col].str.replace('"', "'", regex=False)

    return dataframe
