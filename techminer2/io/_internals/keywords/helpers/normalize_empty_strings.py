import pandas as pd  # type: ignore

from techminer2 import CorpusField


def normalize_empty_strings(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:
        dataframe[col] = dataframe[col].map(
            lambda x: pd.NA if isinstance(x, str) and x.strip() == "" else x
        )

    return dataframe
