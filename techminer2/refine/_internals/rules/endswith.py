import pandas as pd  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import Params

from ._pre_process import _pre_process
from .fuzzy_cutoff_0_word import _compute_matches, _prepare_thesaurus, _report_mergings

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


def apply_endswith_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    thesaurus_df = _prepare_thesaurus(thesaurus_df=thesaurus_df)

    endswith_df = thesaurus_df[
        thesaurus_df[PREFERRED].str.endswith(params.pattern)
    ].copy()

    candidates_0_df = endswith_df[endswith_df["word_count"] == 1].copy()
    candidates_0_df = candidates_0_df.reset_index(drop=True)

    mapping_0_word = _compute_matches(
        thesaurus_df=candidates_0_df,
        similarity_cutoff=params.similarity_cutoff,
        fuzzy_threshold=0.0,
        use_word_level=False,
        word_count_tolerance=0,
    )

    candidates_1_df = endswith_df[endswith_df["word_count"] >= 2].copy()
    candidates_1_df = candidates_1_df.reset_index(drop=True)

    mapping_1_word = _compute_matches(
        thesaurus_df=candidates_1_df,
        similarity_cutoff=params.similarity_cutoff,
        fuzzy_threshold=params.fuzzy_threshold,
        use_word_level=True,
        word_count_tolerance=1,
    )

    mapping = {**mapping_0_word, **mapping_1_word}

    _report_mergings(
        params=params,
        mapping=mapping,
        filename="candidate_mergings.txt",
    )

    return thesaurus_df
