"""

ExactMatch
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField
    >>> from techminer2.thesaurus._internals.exact_match import ExactMatch
    >>> (
    ...     ExactMatch()
    ...     .using_colored_output(False)
    ...     .with_field(CorpusField.ALL_KEY_NP_WORD_RAW)
    ...     .with_thesaurus_file("terms.the.txt")
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )
    INFO: Found 71 exact match candidates for merging.
      Success        : True
      Field          : CorpusField.ALL_KEY_NP_WORD_RAW
      Thesaurus      : terms.the.txt
      Candidates     : 71
      Groups         : 35
      Output File    : examples/small/data/thesaurus/candidates.the.txt
    <BLANKLINE>


"""

from techminer2 import ThesaurusField
from techminer2._internals import ParamsMixin

from .mixins import MatchMixin
from .thesaurus_match_result import ThesaurusMatchResult


class ExactMatch(
    ParamsMixin,
    MatchMixin,
):
    """:meta private:"""

    def run(self) -> ThesaurusMatchResult:

        dataframe = self.load_thesaurus_as_dataframe(params=self.params)
        dataframe = self.compute_occurrences(params=self.params, dataframe=dataframe)
        dataframe = self.normalize_keys(dataframe)
        dataframe = self.select_duplicated_items(dataframe)

        num_candidates = self.compute_num_candidates(dataframe)
        num_groups = self.compute_num_groups(dataframe)

        dataframe = self.add_occ_info(dataframe)

        reporting_df = self.generate_reporting_dataframe(dataframe)
        candidates_filepath = self.get_candidates_filepath()
        self.generate_candidates_txt_file(
            filepath=candidates_filepath, dataframe=reporting_df
        )

        return ThesaurusMatchResult(
            colored_output=self.params.colored_output,
            output_file=str(candidates_filepath),
            thesaurus_file=self.params.thesaurus_file,
            msg=f"Found {num_candidates} exact match candidates for merging.",
            success=True,
            field=self.params.field,
            num_candidates=num_candidates,
            num_groups=num_groups,
        )

    def normalize_keys(self, dataframe):

        dataframe = dataframe.copy()

        dataframe[ThesaurusField.PREFERRED_NORM.value] = dataframe[
            ThesaurusField.PREFERRED.value
        ]
        dataframe[ThesaurusField.PREFERRED_NORM.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].str.replace(r"\r\n|\r", "", regex=True)
        dataframe[ThesaurusField.PREFERRED_NORM.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].str.strip()
        dataframe[ThesaurusField.PREFERRED_NORM.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].map(lambda x: " ".join(x.split()), na_action="ignore")
        dataframe[ThesaurusField.PREFERRED_NORM.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].str.lower()

        return dataframe
