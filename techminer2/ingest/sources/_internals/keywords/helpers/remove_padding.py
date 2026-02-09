import pandas as pd  # type: ignore

from techminer2 import CorpusField


def remove_padding(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.strip()

    return dataframe
