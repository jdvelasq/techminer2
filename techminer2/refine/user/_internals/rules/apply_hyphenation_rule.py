import pandas as pd  # type: ignore

from techminer2 import ThesaurusField

# from ..match.find_rule_matches import xxx_find_rule_matches
from ..match.xxx_apply_matches import xxx_apply_matches


def _normalize_key_temp_column(dataframe: pd.DataFrame) -> pd.DataFrame:

    preferred_term = ThesaurusField.PREFERRED_TEMP.value
    key = ThesaurusField.OLD.value

    dataframe = dataframe.copy()

    dataframe[key] = dataframe[preferred_term]
    dataframe[key] = dataframe[key].str.lower()
    dataframe[key] = dataframe[key].str.replace("-", "", regex=False)
    dataframe[key] = dataframe[key].str.strip()

    return dataframe


def apply_hyphenation_rule(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()
    dataframe = _normalize_key_temp_column(dataframe)
    matches = xxx_find_rule_matches(dataframe)
    dataframe = xxx_apply_matches(matches=matches, dataframe=dataframe)

    return dataframe
