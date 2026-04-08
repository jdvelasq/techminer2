# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p.enum import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value

_PROTECTED = [
    "1g",
    "2g",
    "3g",
    "4g",
    "5g",
    "6g",
]


def apply_num_punct_to_space_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: (
            "#removed"
            if x and (x[0].isdigit() or x[0] in "+/'.,;:!?-") and x not in _PROTECTED
            else x
        )
    )

    return thesaurus_df
