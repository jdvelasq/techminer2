import pandas as pd  # type: ignore

from techminer2.enums import ThesaurusField


def apply_matches(
    matches: dict[str, list[str]],
    dataframe: pd.DataFrame,
) -> pd.DataFrame:

    dataframe = dataframe.copy()

    for preferred_term, variant_terms in matches.items():
        dataframe.loc[
            dataframe[ThesaurusField.PREFERRED_TEMP.value].isin(variant_terms),
            ThesaurusField.PREFERRED_TEMP.value,
        ] = preferred_term

    return dataframe
