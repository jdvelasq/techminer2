import pandas as pd  # type: ignore

from tm2p import ThField

from ....refine000._intern.oper import explode_and_merge

CHANGED = ThField.CHANGED.value
IS_KEYWORD = ThField.IS_KEYWORD.value
OCC = ThField.OCC.value
OLD = ThField.OLD.value
PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


def _post_process(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df[CHANGED] = thesaurus_df[PREFERRED] != thesaurus_df[OLD]
    thesaurus_df = explode_and_merge(thesaurus_df=thesaurus_df)

    return thesaurus_df
