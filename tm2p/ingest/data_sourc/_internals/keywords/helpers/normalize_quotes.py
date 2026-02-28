import pandas as pd  # type: ignore

from tm2p import CorpusField


def normalize_quotes(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.replace("ʿ", "'", regex=False)
        dataframe[col] = dataframe[col].str.replace('"', "'", regex=False)

    return dataframe
