import re

import pandas as pd  # type: ignore

from techminer2 import CorpusField


def remove_leading_articles(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for col in [
        CorpusField.AUTH_KEY_TOK.value,
        CorpusField.IDX_KEY_TOK.value,
    ]:

        for article in ["and", "an", "a", "the"]:

            dataframe[col] = dataframe[col].apply(
                lambda x, art=article: (
                    [re.sub(f"^ {art} ", " ", z) for z in x]
                    if isinstance(x, list)
                    else x
                )
            )

            dataframe[col] = dataframe[col].apply(
                lambda x, art=article: (
                    [re.sub(f"; {art} ", "; ", z) for z in x]
                    if isinstance(x, list)
                    else x
                )
            )

    return dataframe
