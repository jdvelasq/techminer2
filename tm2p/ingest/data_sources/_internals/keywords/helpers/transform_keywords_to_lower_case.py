import pandas as pd  # type: ignore

from tm2p import CorpusField


def transform_keywords_to_lower_case(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.lower()

    return dataframe
