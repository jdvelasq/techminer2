# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value


def apply_single_letters_and_digits_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: (
            x
            if not (len(x) == 1 and x.isalpha()) and not (x.isdigit())
            else "#single_letters_and_digits"
        )
    )

    return thesaurus_df
