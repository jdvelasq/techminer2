import pandas as pd  # type: ignore

from techminer2 import ThesaurusField
from techminer2._constants import NUMBER_TO_LETTER
from techminer2._internals import Params

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


def apply_number_to_letter_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.lower()
    for number, letter in NUMBER_TO_LETTER.items():
        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf"^{number} ", f" {letter} ", regex=True
        )
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
