import pandas as pd  # type: ignore

from tm2p import CorpusField


def remove_accents(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.normalize("NFKD")
        dataframe[col] = dataframe[col].str.encode("ascii", errors="ignore")
        dataframe[col] = dataframe[col].str.decode("utf-8")
        dataframe[col] = dataframe[col].str.replace("<.*?>", "", regex=True)

    return dataframe
