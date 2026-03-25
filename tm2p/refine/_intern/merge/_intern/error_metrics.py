# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params
from tm2p._intern.packag_data import load_builtin_word_list

PREFERRED = ThField.PREFERRED.value


def apply_error_metrics_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    error_metrics = set(load_builtin_word_list("error_metrics.txt"))
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: x if x not in error_metrics else "#error_metrics"
    )

    return thesaurus_df
