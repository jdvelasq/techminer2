import pandas as pd  # type: ignore

from techminer2 import CorpusField


def remove_html_tags(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.replace(r"<[^>]+>", "", regex=True)

    return dataframe
