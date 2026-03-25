# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value


def apply_num_punct_to_space_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: "#removed" if x and x[0].isdigit() or x[0] in "+/'.,;:!?-" else x
    )

    return thesaurus_df
