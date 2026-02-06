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

    def normalize(self, dataframe):

        dataframe = dataframe.copy()

        dataframe[ThesaurusField.KEY.value] = dataframe[
            ThesaurusField.KEY.value
        ].str.replace(r"\r\n|\r", "", regex=True)

        dataframe[ThesaurusField.KEY.value] = dataframe[
            ThesaurusField.KEY.value
        ].str.strip()

        dataframe[ThesaurusField.KEY.value] = dataframe[ThesaurusField.KEY.value].map(
            lambda x: " ".join(x.split()), na_action="ignore"
        )

        dataframe[ThesaurusField.KEY.value] = dataframe[
            ThesaurusField.KEY.value
        ].str.lower()

        return dataframe

    def run(self) -> ThesaurusMatchResult:

        dataframe = self.prepare_thesaurus_dataframe(params=self.params)
        dataframe = self.normalize(dataframe)
        dataframe = self.find_matches(dataframe)

        return self.report_match_results(
            params=self.params,
            dataframe=dataframe,
        )
