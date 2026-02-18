from pathlib import Path

import pandas as pd

from techminer2 import ThesaurusField
from techminer2._internals import Params

from ..._internals.objs.thesaurus_match_result import ThesaurusMatchResult


class MatchMixin:
    """:meta private:"""

    # def add_occ_info(self, dataframe):
    #     dataframe = dataframe.sort_values(
    #         by=ThesaurusField.OCC.value, ascending=False
    #     ).reset_index(drop=True)
    #     dataframe[ThesaurusField.PREFERRED.value] = (
    #         dataframe[ThesaurusField.PREFERRED.value]
    #         + "  # occ: "
    #         + dataframe[ThesaurusField.OCC.value].astype(str)
    #     )
    #     return dataframe

    def compute_num_candidates(self, dataframe):
        return dataframe.shape[0]

    def compute_num_groups(self, dataframe):
        return dataframe[ThesaurusField.OLD.value].drop_duplicates().shape[0]

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
                ThesaurusField.OLD.value,
                ThesaurusField.OCC.value,
            ]
        ]
        reporting_df = dataframe.groupby(ThesaurusField.OLD.value, as_index=False).agg(
            list
        )
        reporting_df[ThesaurusField.OCC.value] = reporting_df[
            ThesaurusField.OCC.value
        ].map(lambda x: x[0])

        reporting_df = reporting_df.sort_values(
            by=[ThesaurusField.OCC.value, ThesaurusField.OLD.value],
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

    def find_matches(self, dataframe):

        dataframe = dataframe.copy()

        counting = dataframe[ThesaurusField.OLD.value].value_counts()
        counting = counting[counting > 1]
        duplicated_items = counting.index.to_list()

        dataframe = dataframe[
            dataframe[ThesaurusField.OLD.value].isin(duplicated_items)
        ]

        return dataframe
