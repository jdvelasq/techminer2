import pandas as pd  # type: ignore

from tm2p import ThesaurusField
from tm2p._internals import Params
from tm2p._internals.package_data import load_builtin_mapping

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
    number_to_letter = load_builtin_mapping("number_to_letter.json")
    for number, letter in number_to_letter.items():
        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf"^{number} ", f" {letter} ", regex=True
        )
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
