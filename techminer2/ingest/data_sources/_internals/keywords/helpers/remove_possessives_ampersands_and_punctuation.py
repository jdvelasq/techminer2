import pandas as pd  # type: ignore

from techminer2 import CorpusField


def remove_possessives_ampersands_and_punctuation(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.replace("'s ", " ", regex=False)
        dataframe[col] = dataframe[col].str.replace("'", "", regex=False)
        dataframe[col] = dataframe[col].str.replace('"', "", regex=False)
        dataframe[col] = dataframe[col].str.replace("&", " and ", regex=False)
        dataframe[col] = dataframe[col].str.replace(".", "", regex=False)
        dataframe[col] = dataframe[col].str.replace(",", "", regex=False)
        dataframe[col] = dataframe[col].str.replace(":", "", regex=False)
        dataframe[col] = dataframe[col].str.replace(" - ", "", regex=False)
        dataframe[col] = dataframe[col].str.replace("\u2013", "-", regex=False)

    return dataframe
