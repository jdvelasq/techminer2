import pandas as pd  # type: ignore

from tm2p import ThesaurusField
from tm2p._intern import Params

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


#
# User provides regex pattern
#
# For each key in thesaurus:
#   If key matches regex:
#     Add to candidate list
#
# Present candidates to user
#
# Candidates:
#
# test 1
#     test 1
# test 2
#     test 2
# test 10
#     test 10
# benchmark test 1
#     benchmark test 1
#
# User regex: \btest \d+\b (find "test" followed by number)
#


def apply_regex_pattern_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    #

    #
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
