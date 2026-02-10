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

from tqdm import tqdm  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import ParamsMixin

from ._internals.io.load_as_dataframe import load_as_dataframe
from ._internals.mixins import MatchMixin
from ._internals.rules.apply_exact_match_rule import apply_exact_match_rule
from ._internals.rules.apply_hyphenation_rule import apply_hyphenation_rule
from ._internals.rules.apply_numeric_variation_rule import apply_numeric_variation_rule
from ._internals.rules.apply_plural_singular_rule import apply_plural_singular_rule
from ._internals.rules.apply_puntuation_variation_rule import (
    apply_puntuation_variation_rule,
)
from ._internals.rules.apply_word_order_rule import apply_word_order_rule
from ._internals.thesaurus_match_result import ThesaurusMatchResult


class FuzzyCutoffMatch(
    ParamsMixin,
    MatchMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def normalize(self, dataframe):

        dataframe[ThesaurusField.KEY.value] = dataframe[
            ThesaurusField.KEY.value
        ].str.lower()

        dataframe[ThesaurusField.KEY.value] = dataframe[
            ThesaurusField.KEY.value
        ].str.replace("_", " ")

        dataframe[ThesaurusField.KEY_LENGTH.value] = dataframe[
            ThesaurusField.KEY.value
        ].str.split()

        dataframe[ThesaurusField.KEY_LENGTH.value] = dataframe[
            ThesaurusField.KEY.value
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

        keys = dataframe[ThesaurusField.KEY.value].tolist()

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
            dataframe.loc[df.index, ThesaurusField.KEY.value] = dataframe.loc[
                index, ThesaurusField.KEY.value
            ]

        dataframe = dataframe[dataframe["selected"]]

        return dataframe[
            [
                ThesaurusField.PREFERRED.value,
                ThesaurusField.KEY.value,
                ThesaurusField.OCC.value,
            ]
        ]

    # -------------------------------------------------------------------------
    def run(self) -> ThesaurusMatchResult:

        dataframe = load_as_dataframe(params=self.params)
        # dataframe = apply_exact_match_rule(dataframe)
        # dataframe = apply_word_order_rule(dataframe)
        # dataframe = apply_puntuation_variation_rule(dataframe)
        # dataframe = apply_hyphenation_rule(dataframe)
        # dataframe = apply_numeric_variation_rule(dataframe)
        dataframe = apply_plural_singular_rule(dataframe)

        return self.report_match_results(
            params=self.params,
            dataframe=dataframe,
        )
