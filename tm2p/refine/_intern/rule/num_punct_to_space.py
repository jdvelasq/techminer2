import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThField.CHANGED.value
IS_KEYWORD = ThField.IS_KEYWORD.value
OCC = ThField.OCC.value
OLD = ThField.OLD.value
PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
VARIANT = ThField.VARIANT.value


def apply_num_punct_to_space_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.lower()
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: "#removed" if x and x[0].isdigit() or x[0] in "+/'.,;:!?-" else x
    )
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
