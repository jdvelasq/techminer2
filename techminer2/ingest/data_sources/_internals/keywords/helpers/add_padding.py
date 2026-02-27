import pandas as pd  # type: ignore

from techminer2 import CorpusField


def add_padding(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
    ]:
        dataframe[col] = dataframe[col].apply(lambda x: f" {x} " if pd.notna(x) else x)

    return dataframe
