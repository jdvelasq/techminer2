import pandas as pd

from techminer2._internals import Params
from techminer2.enums import ThesaurusField

from .thesaurus_match_result import ThesaurusMatchResult

FLAG = ThesaurusField.CHANGED.value
KEY = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
VARIANT = ThesaurusField.VARIANT.value


def report_thesaurus_match_results(
    params: Params,
    dataframe: pd.DataFrame,
) -> ThesaurusMatchResult:

    dataframe = dataframe.copy()

    counting = dataframe[ThesaurusField.PREFERRED_TEMP.value].value_counts()
    counting = counting[counting > 1]
    duplicated_items = counting.index.to_list()
    dataframe = dataframe[
        dataframe[ThesaurusField.PREFERRED_TEMP.value].isin(duplicated_items)
    ]

    num_candidates = self.compute_num_candidates(dataframe)
    num_groups = self.compute_num_groups(dataframe)
    dataframe = self.add_occ_info(dataframe)
    reporting_df = self.generate_reporting_dataframe(dataframe)
    candidates_filepath = self.get_candidates_filepath()
    self.generate_candidates_txt_file(
        filepath=candidates_filepath, dataframe=reporting_df
    )

    return ThesaurusMatchResult(
        colored_output=params.colored_output,
        output_file=str(candidates_filepath),
        thesaurus_file=params.thesaurus_file,
        msg=f"Found {num_candidates} match candidates for merging.",
        success=True,
        field=params.field.value,
        num_candidates=num_candidates,
        num_groups=num_groups,
    )
