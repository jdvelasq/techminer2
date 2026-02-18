import pandas as pd  # type: ignore

from techminer2 import ThesaurusField

from ...._internals.operations import explode_and_merge

PREFERRED = ThesaurusField.PREFERRED.value
KEY = ThesaurusField.OLD.value


def apply_exact_match_rule(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    dataframe[KEY] = dataframe[PREFERRED]
    dataframe[KEY] = dataframe[KEY].str.replace(r"\r\n|\r", "", regex=True)
    dataframe[KEY] = dataframe[KEY].str.strip()
    dataframe[KEY] = dataframe[KEY].map(
        lambda x: " ".join(x.split()), na_action="ignore"
    )
    dataframe[KEY] = dataframe[KEY].str.lower()

    dataframe = explode_and_merge(thesaurus_df=dataframe)

    return dataframe
