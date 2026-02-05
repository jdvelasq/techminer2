"""

FuzzyCutoffMatch
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField
    >>> from techminer2.thesaurus._internals.fuzzy_cutoff_match import FuzzyCutoffMatch
    >>> (
    ...     FuzzyCutoffMatch()
    ...     .using_colored_output(False)
    ...     .with_field(CorpusField.ALL_KEY_NP_WORD_RAW)
    ...     .using_similarity_cutoff(85)
    ...     .using_fuzzy_threshold(95)
    ...     .with_thesaurus_file("terms.the.txt")
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )
    INFO: Found 109 match candidates for merging.
      Success        : True
      Field          : CorpusField.ALL_KEY_NP_WORD_RAW
      Thesaurus      : terms.the.txt
      Candidates     : 109
      Groups         : 54
      Output File    : examples/small/data/thesaurus/candidates.the.txt
    <BLANKLINE>


"""

from fuzzywuzzy import fuzz  # type: ignore
from tqdm import tqdm  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import ParamsMixin

from .mixins import MatchMixin
from .thesaurus_match_result import ThesaurusMatchResult


class FuzzyCutoffMatch(
    ParamsMixin,
    MatchMixin,
):
    """:meta private:"""

    def compute_fuzzy_match(self, string1, string2):

        string1 = string1.split()
        string2 = string2.split()

        if len(string1) > len(string2):
            shorten_string = string2
            lengthen_string = string1
        else:
            shorten_string = string1
            lengthen_string = string2

        scores_per_word = []
        for base_word in shorten_string:
            best_match = 0
            for candidate_word in lengthen_string:
                score = fuzz.ratio(base_word, candidate_word)
                if score > best_match:
                    best_match = score
            scores_per_word.append(best_match)

        score = min(scores_per_word)
        match = all(score >= self.params.fuzzy_threshold for score in scores_per_word)

        return score, match

    # -------------------------------------------------------------------------
    def normalize(self, dataframe):

        dataframe[ThesaurusField.PREFERRED_NORM.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].str.lower()

        dataframe[ThesaurusField.PREFERRED_NORM.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].str.replace("_", " ")

        dataframe[ThesaurusField.KEY_LENGTH.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].str.split()

        dataframe[ThesaurusField.KEY_LENGTH.value] = dataframe[
            ThesaurusField.PREFERRED_NORM.value
        ].map(len, na_action="ignore")

        dataframe = dataframe.sort_values(
            by=[
                ThesaurusField.KEY_LENGTH.value,
                ThesaurusField.OCC.value,
                ThesaurusField.PREFERRED.value,
            ],
            ascending=[True, False, True],
        )

        return dataframe

    # -------------------------------------------------------------------------
    def find_matches(self, dataframe):

        dataframe["selected"] = False
        dataframe = dataframe.reset_index(drop=True)

        import sys

        sys.stderr.write(repr(dataframe.columns.tolist()))

        dataframe["diff_in_length"] = dataframe[ThesaurusField.KEY_LENGTH.value].map(
            lambda x: int((1 - self.params.similarity_cutoff / 100.0) * x)
        )

        dataframe["min_key_length"] = dataframe.apply(
            lambda row: max(
                row[ThesaurusField.KEY_LENGTH.value] - row["diff_in_length"], 1
            ),
            axis=1,
        )

        dataframe["max_key_length"] = dataframe.apply(
            lambda row: row[ThesaurusField.KEY_LENGTH.value] + row["diff_in_length"],
            axis=1,
        )

        keys = dataframe[ThesaurusField.PREFERRED_NORM.value].tolist()

        for index, key in tqdm(
            enumerate(keys),
            total=len(keys),
            desc="  Progress",
            ncols=80,
            disable=self.params.tqdm_disable,
        ):

            if dataframe.loc[index, "selected"] is True:
                continue

            df = dataframe[dataframe.index > index]

            df = df[
                df[ThesaurusField.KEY_LENGTH.value]
                == dataframe.loc[index, ThesaurusField.KEY_LENGTH.value]
            ]

            df = df[
                df[ThesaurusField.KEY_LENGTH.value]
                <= dataframe.loc[index, "max_key_length"]
            ]
            df = df[
                df[ThesaurusField.KEY_LENGTH.value]
                >= dataframe.loc[index, "min_key_length"]
            ]

            # Apply the cutoff rule
            df["cutoff"] = df[ThesaurusField.PREFERRED_NORM.value].apply(
                lambda x: fuzz.ratio(key, x)
            )
            df = df[df["cutoff"] >= self.params.similarity_cutoff]

            if df.empty:
                continue

            results = df[ThesaurusField.PREFERRED_NORM.value].apply(
                lambda x: self.compute_fuzzy_match(key, x)
            )

            df["fuzzy"] = results.map(lambda x: x[0])
            df["fuzzy_match"] = results.map(lambda x: x[1])

            df = df[df["fuzzy_match"].apply(lambda x: x is True)]

            if df.empty:
                continue

            dataframe.loc[index, "selected"] = True
            dataframe.loc[df.index, "selected"] = True
            dataframe.loc[df.index, ThesaurusField.PREFERRED_NORM.value] = (
                dataframe.loc[index, ThesaurusField.PREFERRED_NORM.value]
            )

        dataframe = dataframe[dataframe["selected"]]

        return dataframe[
            [
                ThesaurusField.PREFERRED.value,
                ThesaurusField.PREFERRED_NORM.value,
                ThesaurusField.OCC.value,
            ]
        ]

    # -------------------------------------------------------------------------
    def run(self) -> ThesaurusMatchResult:

        dataframe = self.prepare_thesaurus_dataframe(params=self.params)
        dataframe = self.normalize(dataframe)
        dataframe = self.find_matches(dataframe)

        return self.report_match_results(
            params=self.params,
            dataframe=dataframe,
        )
