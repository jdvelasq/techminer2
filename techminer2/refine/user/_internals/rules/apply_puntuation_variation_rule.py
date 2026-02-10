import pandas as pd  # type: ignore

from techminer2 import ThesaurusField

from ..match.apply_matches import apply_matches
from ..match.find_rule_matches import find_rule_matches


def _normalize_key_temp_column(dataframe: pd.DataFrame) -> pd.DataFrame:

    preferred_term = ThesaurusField.PREFERRED_TEMP.value
    key = ThesaurusField.KEY.value

    dataframe = dataframe.copy()

    dataframe[key] = dataframe[preferred_term]
    dataframe[key] = dataframe[key].str.lower()
    dataframe[key] = dataframe[key].str.replace(r"[^\w\s]", " ", regex=True)
    dataframe[key] = dataframe[key].str.strip()

    return dataframe


def apply_puntuation_variation_rule(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()
    dataframe = _normalize_key_temp_column(dataframe)
    matches = find_rule_matches(dataframe)
    dataframe = apply_matches(matches=matches, dataframe=dataframe)

    return dataframe
