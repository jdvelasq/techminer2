import pandas as pd  # type: ignore

from techminer2 import CorpusField


def fix_parenthesis_spacing(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:

        dataframe[col] = dataframe[col].str.replace(
            r"([A-Za-z0-9])([\(\[\{])",
            r"\1 \2",
            regex=True,
        )
        dataframe[col] = dataframe[col].str.replace(
            r"([A-Za-z0-9])([\)\]\}])",
            r"\1 \2",
            regex=True,
        )

        dataframe[col] = dataframe[col].str.replace(
            r"([\)\]\}])([A-Za-z0-9])",
            r"\1 \2",
            regex=True,
        )
        dataframe[col] = dataframe[col].str.replace(
            r"([\(\[\{])([A-Za-z0-9])",
            r"\1 \2",
            regex=True,
        )

    return dataframe
