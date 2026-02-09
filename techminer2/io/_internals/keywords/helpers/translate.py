import pandas as pd  # type: ignore

from techminer2 import CorpusField
from techminer2._constants import BRITISH_TO_AMERICAN


def translate(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.replace("; ", " ; ", regex=False)

        for british, american in BRITISH_TO_AMERICAN.items():
            dataframe[col] = dataframe[col].str.replace(
                f" {british} ",
                f" {american} ",
                regex=False,
            )

        dataframe[col] = dataframe[col].str.replace(" ; ", "; ", regex=False)

    return dataframe
