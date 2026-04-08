# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p.enum import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value


def apply_single_letters_and_digits_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: (
            "#single_letters_and_digits"
            if (len(x) == 1 and x.isalpha()) or x.isdigit()
            else x
        )
    )

    return thesaurus_df
