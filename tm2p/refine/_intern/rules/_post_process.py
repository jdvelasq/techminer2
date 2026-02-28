import pandas as pd  # type: ignore

from tm2p import ThesaurusField

from ..operations import explode_and_merge

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
VARIANT = ThesaurusField.VARIANT.value


def _post_process(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df[CHANGED] = thesaurus_df[PREFERRED] != thesaurus_df[OLD]
    thesaurus_df = explode_and_merge(thesaurus_df=thesaurus_df)

    return thesaurus_df
