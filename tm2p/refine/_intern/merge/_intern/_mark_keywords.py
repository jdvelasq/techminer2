import pandas as pd  # type: ignore

from tm2p import Field
from tm2p._intern import Params
from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import ThField

CHANGED = ThField.CHANGED.value
IS_KEYWORD = ThField.IS_KEYWORD.value
OCC = ThField.OCC.value
OLD = ThField.OLD.value
PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


def mark_keywords(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    data_df = load_main_csv_zip(
        root_directory=params.root_directory,
    )

    keywords = _extract_keywords_from_data(data_df)

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[IS_KEYWORD] = thesaurus_df[PREFERRED].apply(lambda x: x in keywords)

    return thesaurus_df


def _extract_keywords_from_data(data_df):

    keywords = set()
    for col in [
        Field.AUTHKW_RAW.value,
        Field.IDXKW_RAW.value,
    ]:
        series = data_df[col].dropna().str.split("; ").explode().str.strip()
        keywords.update(series.drop_duplicates().to_list())

    return keywords
