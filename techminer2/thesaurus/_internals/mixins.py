from pathlib import Path
from typing import Dict

import pandas as pd

from techminer2 import ThesaurusField
from techminer2._internals import Params

from .thesaurus_match_result import ThesaurusMatchResult


class MatchMixin:
    """:meta private:"""

    def add_occ_info(self, dataframe):
        dataframe = dataframe.sort_values(
            by=ThesaurusField.OCC.value, ascending=False
        ).reset_index(drop=True)

        dataframe[ThesaurusField.PREFERRED.value] = (
            dataframe[ThesaurusField.PREFERRED.value]
            + "  # occ: "
            + dataframe[ThesaurusField.OCC.value].astype(str)
        )

        return dataframe

    def compute_num_candidates(self, dataframe):
        return dataframe.shape[0]

    def compute_num_groups(self, dataframe):
        return dataframe[ThesaurusField.KEY.value].drop_duplicates().shape[0]

    def generate_candidates_txt_file(self, filepath, dataframe):

        with open(filepath, "w", encoding="utf-8") as file:
            for _, row in dataframe.iterrows():
                terms = row[ThesaurusField.PREFERRED.value]
                file.write(f"{terms[0]}\n")
                for term in terms[1:]:
                    file.write(f"    {term}\n")

    def generate_reporting_dataframe(self, dataframe):
        dataframe = dataframe[
            [
                ThesaurusField.PREFERRED.value,
                ThesaurusField.KEY.value,
                ThesaurusField.OCC.value,
            ]
        ]
        reporting_df = dataframe.groupby(ThesaurusField.KEY.value, as_index=False).agg(
            list
        )
        reporting_df[ThesaurusField.OCC.value] = reporting_df[
            ThesaurusField.OCC.value
        ].map(lambda x: x[0])

        reporting_df = reporting_df.sort_values(
            by=[ThesaurusField.OCC.value, ThesaurusField.KEY.value],
            ascending=False,
        ).reset_index(drop=True)

        return reporting_df

    def get_candidates_filepath(self):
        return (
            Path(self.params.root_directory)
            / "data"
            / "thesaurus"
            / "candidates.the.txt"
        )

    def report_match_results(
        self, params: Params, dataframe: pd.DataFrame
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
            field=params.field,
            num_candidates=num_candidates,
            num_groups=num_groups,
        )

    def find_matches(self, dataframe):

        dataframe = dataframe.copy()

        counting = dataframe[ThesaurusField.KEY.value].value_counts()
        counting = counting[counting > 1]
        duplicated_items = counting.index.to_list()

        dataframe = dataframe[
            dataframe[ThesaurusField.KEY.value].isin(duplicated_items)
        ]

        return dataframe
