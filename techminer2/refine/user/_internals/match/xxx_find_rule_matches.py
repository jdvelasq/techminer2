import pandas as pd

from techminer2 import ThesaurusField


def xxx_find_rule_matches(dataframe: pd.DataFrame) -> dict[str, list[str]]:

    dataframe = dataframe.copy()

    counting = dataframe[ThesaurusField.OLD.value].value_counts()
    counting = counting[counting > 1]
    duplicated_items = counting.index.to_list()
    dataframe = dataframe[dataframe[ThesaurusField.OLD.value].isin(duplicated_items)]

    dataframe = dataframe[
        [
            ThesaurusField.PREFERRED_TEMP.value,
            ThesaurusField.OLD.value,
        ]
    ]

    matches_df = dataframe.groupby(ThesaurusField.OLD.value, as_index=False).agg(list)

    matches = {}
    for _, row in matches_df.iterrows():
        key = row[ThesaurusField.PREFERRED_TEMP.value][0]
        preferred_terms = row[ThesaurusField.PREFERRED_TEMP.value][1:]
        matches[key] = preferred_terms

    return matches
