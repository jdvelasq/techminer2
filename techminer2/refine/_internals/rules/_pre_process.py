import pandas as pd  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import Params

from ..operations import mark_keywords, sort_thesaurus_by_occ

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
VARIANT = ThesaurusField.VARIANT.value


def _pre_process(params: Params, thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df = sort_thesaurus_by_occ(params=params, thesaurus_df=thesaurus_df)
    thesaurus_df = mark_keywords(params=params, thesaurus_df=thesaurus_df)
    thesaurus_df[OLD] = thesaurus_df[PREFERRED]

    return thesaurus_df
