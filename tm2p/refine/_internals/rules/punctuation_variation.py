import pandas as pd  # type: ignore

from tm2p import ThesaurusField
from tm2p._internals import Params

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


STANDARD_PUNCTUATION = ".,;:!?\"'()"


def apply_punctuation_variation_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    for char in STANDARD_PUNCTUATION:
        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            char, "", regex=False
        )
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
        r"\s+", " ", regex=True
    )
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
