import pandas as pd  # type: ignore

from techminer2 import CorpusField
from techminer2._internals.package_data import load_builtin_mapping


def translate(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    british_to_american = load_builtin_mapping("british_to_american.json")

    for col in [
        CorpusField.AUTHKW_TOK.value,
        CorpusField.IDXKW_TOK.value,
    ]:
        dataframe[col] = dataframe[col].str.replace("; ", " ; ", regex=False)

        for british, american in british_to_american.items():
            american_value = american[0] if isinstance(american, list) else american
            dataframe[col] = dataframe[col].str.replace(
                f" {british} ",
                f" {american_value} ",
                regex=False,
            )

        dataframe[col] = dataframe[col].str.replace(" ; ", "; ", regex=False)

    return dataframe
