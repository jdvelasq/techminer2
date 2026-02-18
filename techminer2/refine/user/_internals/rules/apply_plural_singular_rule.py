import pandas as pd  # type: ignore

from techminer2 import ThesaurusField

# from ..match.find_rule_matches import xxx_find_rule_matches
from ..match.xxx_apply_matches import xxx_apply_matches


def _normalize_key_temp_column(dataframe: pd.DataFrame) -> pd.DataFrame:

    preferred_term = ThesaurusField.PREFERRED_TEMP.value
    key = ThesaurusField.OLD.value

    dataframe = dataframe.copy()

    dataframe[key] = dataframe[preferred_term]
    dataframe[key] = dataframe[key].str.split()
    dataframe[key] = dataframe[key].apply(
        lambda x: (
            [Word(y).singularize().singularize().singularize() for y in x]
            if isinstance(x, list)
            else x
        ),
    )
    dataframe[key] = dataframe[key].str.join(" ")

    return dataframe


def apply_plural_singular_rule(dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()
    dataframe = _normalize_key_temp_column(dataframe)
    matches = xxx_find_rule_matches(dataframe)
    dataframe = xxx_apply_matches(matches=matches, dataframe=dataframe)

    return dataframe
