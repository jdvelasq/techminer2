"""

FuzzyCutoffMatch
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField

    >>> from techminer2.refine.descriptors import CreateThesaurus

    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : ...fintech-with-references/refine/thesaurus/descriptors.the.txt
      Source field : DESCRIPTOR_TOK
      Status       : 2467 items added to the thesaurus.
    <BLANKLINE>

    >>> from techminer2.refine.descriptors.fuzzy_cutoff_match import FuzzyCutoffMatch
    >>> (
    ...     FuzzyCutoffMatch()
    ...     .using_colored_output(False)
    ...     .using_similarity_cutoff(85)
    ...     .using_fuzzy_threshold(95)
    ...     .with_thesaurus_file("descriptors.the.txt")
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .run()
    ... )
    INFO: Fuzzy cutoff matching completed.
      Success        : True
      Field          : _UNSPECIFIED_
      Thesaurus      : descriptors.the.txt
      Output File    :
    <BLANKLINE>


"""

from tqdm import tqdm  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import ParamsMixin
from techminer2.refine._internals.objs.thesaurus_match_result import (
    ThesaurusMatchResult,
)
from techminer2.refine._internals.rules import (
    apply_common_and_basic_rule,
    apply_exact_match_rule,
    apply_hyphenation_match_rule,
    apply_num_punct_to_space_rule,
    apply_number_to_letter_rule,
    apply_plural_singular_match_rule,
    apply_punctuation_variation_match_rule,
    apply_scientific_and_academic_rule,
    apply_stopwords_removal_match_rule,
    apply_white_space_normalization_rule,
    apply_word_order_match_rule,
    apply_xml_encoding_rule,
)

from .._internals.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)


class FuzzyCutoffMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> ThesaurusMatchResult:

        dataframe = load_thesaurus_as_dataframe(params=self.params)
        #
        # 0. upper/lower case normalization ← MUST be first (removes noise)
        dataframe = apply_exact_match_rule(thesaurus_df=dataframe)
        dataframe = apply_number_to_letter_rule(thesaurus_df=dataframe)
        #
        # 1. NumPunctToSpace ← MUST be first (removes noise)
        dataframe = apply_num_punct_to_space_rule(thesaurus_df=dataframe)
        #
        # 2. XMLEncoding
        dataframe = apply_xml_encoding_rule(thesaurus_df=dataframe)
        #
        # 3. WhitespaceNormalization
        dataframe = apply_white_space_normalization_rule(thesaurus_df=dataframe)
        #
        # 4. PunctuationVariationMatch
        dataframe = apply_punctuation_variation_match_rule(thesaurus_df=dataframe)
        #
        # 5. HyphenationMatch ← MUST be before domain thesauri
        dataframe = apply_hyphenation_match_rule(thesaurus_df=dataframe)
        #
        # 6. ChemicalCompounds
        #
        # 7. CommonAndBasic
        dataframe = apply_common_and_basic_rule(thesaurus_df=dataframe)

        #
        # 8. ScientificAndAcademic
        dataframe = apply_scientific_and_academic_rule(thesaurus_df=dataframe)
        #
        # 15. PluralSingularMatch ← MUST be before stemming
        dataframe = apply_plural_singular_match_rule(thesaurus_df=dataframe)

        # 17. WordOrderMatch
        dataframe = apply_stopwords_removal_match_rule(thesaurus_df=dataframe)
        dataframe = apply_word_order_match_rule(thesaurus_df=dataframe)

        #

        #
        # 20. FuzzyCutoffMatch ← MUST be last

        ####
        # On-demand meriging
        # No dependencies - can run in any order, any time:
        #

        # 9. ContainsPatternMatch ← Find "network" anywhere
        # 10. BeginsWithMatch ← Find terms starting with "machine"
        # 11. EndsWithMatch ← Find terms ending with "learning"
        # 12. RegexPatternMatch ← Find complex patterns
        # 16. StemmedMatch

        # 18. FindCloseMatches ← Check variants of specific term
        ####

        save_dataframe_as_thesaurus(params=self.params, dataframe=dataframe)

        return ThesaurusMatchResult(
            colored_output=self.params.colored_output,
            output_file=None,
            thesaurus_file=self.params.thesaurus_file,
            msg="Fuzzy cutoff matching completed.",
            success=True,
            field=self.params.field.value,
        )

    #####

    # -------------------------------------------------------------------------
    def normalize(self, dataframe):

        dataframe[ThesaurusField.OLD.value] = dataframe[
            ThesaurusField.OLD.value
        ].str.lower()

        dataframe[ThesaurusField.OLD.value] = dataframe[
            ThesaurusField.OLD.value
        ].str.replace("_", " ")

        dataframe[ThesaurusField.KEY_LENGTH.value] = dataframe[
            ThesaurusField.OLD.value
        ].str.split()

        dataframe[ThesaurusField.KEY_LENGTH.value] = dataframe[
            ThesaurusField.OLD.value
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

        keys = dataframe[ThesaurusField.OLD.value].tolist()

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
            dataframe.loc[df.index, ThesaurusField.OLD.value] = dataframe.loc[
                index, ThesaurusField.OLD.value
            ]

        dataframe = dataframe[dataframe["selected"]]

        return dataframe[
            [
                ThesaurusField.PREFERRED.value,
                ThesaurusField.OLD.value,
            ]
        ]

    # -------------------------------------------------------------------------
