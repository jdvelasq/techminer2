import pandas as pd  # type: ignore
from textblob import Word  # type: ignore

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


def apply_plural_singular_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED]
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(
        lambda x: (
            [Word(y).singularize().singularize().singularize() for y in x]
            if isinstance(x, list)
            else x
        ),
    )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join(" ")
    #
    mapping_df = thesaurus_df[[SIGNATURE, PREFERRED]].copy()
    mapping_df = mapping_df.drop_duplicates()
    mapping = dict(zip(mapping_df[SIGNATURE].values, mapping_df[PREFERRED].values))
    thesaurus_df[PREFERRED] = thesaurus_df[SIGNATURE].apply(lambda x: mapping.get(x, x))
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
