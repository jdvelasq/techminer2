import pandas as pd  # type: ignore

from tm2p import CorpusField


def fix_parenthesis_spacing(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
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
