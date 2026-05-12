"""
BaseAuto
===============================================================================

Smoke test:
    >>> from tm2p.enum import AnalysisUnit, Field, ThFile
    >>> from tm2p.refine._intern.merge import BaseAuto
    >>> (
    ...     BaseAuto()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )



"""

import sys

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)
from tm2p.refine._intern.oper.sort_thesaurus_df_by_occ import sort_thesaurus_df_by_occ

from ..group.group import _explode_variants, _group_variants
from ._intern import (
    apply_british_to_american_rule,
    apply_chemical_compounds_rule,
    apply_common_and_basic_rule,
    apply_error_metrics_rule,
    apply_exact_match_rule,
    apply_geographic_names_rule,
    apply_inflected_verb_forms_rule,
    apply_leading_noise_removal_rule,
    apply_num_punct_to_space_rule,
    apply_number_to_letter_rule,
    apply_plural_singular_rule,
    apply_prefer_singular_over_plural_rule,
    apply_punctuation_variation_rule,
    apply_scientific_and_academic_rule,
    apply_single_letters_and_digits_rule,
    apply_technology_rule,
    apply_trailing_noise_removal_rule,
    apply_white_space_normalization_rule,
    apply_xml_encoding_rule,
)
from ._intern._mark_keywords import mark_keywords

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class BaseAuto(
    ParamsMixin,
):
    """:meta private:"""

    _HEADER_WIDTH = 70
    _STEP_PREFIX = "  → Rule : "
    _ORDINAL = [
        "First",
        "Second",
        "Third",
        "Fourth",
        "Fifth",
        "Sixth",
        "Seventh",
        "Eighth",
        "Ninth",
        "Tenth",
    ]

    def _write(self, text: str) -> None:
        sys.stderr.write(text)
        sys.stderr.flush()

    def _print_header(self) -> None:
        separator = "=" * self._HEADER_WIDTH
        self._write(f"\n{separator}\nPre-processing Thesaurus\n{separator}\n")

    def run(self) -> None:

        self._print_header()

        initial_length = None
        final_length = None

        phases = [
            [
                ("british to american", apply_british_to_american_rule),
                ("single letters and digits", apply_single_letters_and_digits_rule),
                ("exact match", apply_exact_match_rule),
                ("geographic names", apply_geographic_names_rule),
                ("error metrics", apply_error_metrics_rule),
                ("number to letter", apply_number_to_letter_rule),
                ("num punct to space", apply_num_punct_to_space_rule),
                ("xml encoding", apply_xml_encoding_rule),
                ("white space normalization", apply_white_space_normalization_rule),
                ("chemical compounds", apply_chemical_compounds_rule),
                ("technology", apply_technology_rule),
                ("punctuation variation", apply_punctuation_variation_rule),
            ]
        ] + [
            [
                ("geographic names", apply_geographic_names_rule),
                ("plural singular", apply_plural_singular_rule),
                ("prefer singular over plural", apply_prefer_singular_over_plural_rule),
                ("common and basic", apply_common_and_basic_rule),
                ("scientific and academic", apply_scientific_and_academic_rule),
                ("inflected verb forms", apply_inflected_verb_forms_rule),
                # ("leading noise removal", apply_leading_noise_removal_rule),
                ("punctuation variation", apply_punctuation_variation_rule),
                # ("trailing noise removal", apply_trailing_noise_removal_rule),
                ("punctuation variation", apply_punctuation_variation_rule),
            ],
        ] * 4

        for index, phase in enumerate(phases):

            self._write(f"\n[{index+1}] {self._ORDINAL[index]} Pass\n")

            df = load_thesaurus_as_dataframe(params=self.params)

            if initial_length is None:
                initial_length = df.shape[0]
            else:
                final_length = df.shape[0]

            df = sort_thesaurus_df_by_occ(params=self.params, thesaurus_df=df)
            df = _explode_variants(df)
            df = mark_keywords(df, self.params)

            for msg, rule in phase:

                self._write(f"{self._STEP_PREFIX}{msg}\n")
                df = rule(df, self.params)

            df = df[[PREFERRED, VARIANT]].copy()
            df = _group_variants(df)
            df = df.sort_values(PREFERRED)  # type: ignore

            save_dataframe_as_thesaurus(params=self.params, df=df)
