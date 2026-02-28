import pandas as pd  # type: ignore

from tm2p import CorpusField


def remove_empty_terms(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.split("; ")
        dataframe[col] = dataframe[col].apply(
            lambda x: [z for z in x if z.strip() != ""] if isinstance(x, list) else x
        )
        dataframe[col] = dataframe[col].str.join("; ")

    return dataframe
