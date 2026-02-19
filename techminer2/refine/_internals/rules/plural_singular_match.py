import pandas as pd  # type: ignore
from textblob import Word  # type: ignore

from techminer2 import ThesaurusField
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


def apply_plural_singular_match_rule(
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
