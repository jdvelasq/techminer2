"""

Pre-Processing Merger
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField

    >>> from techminer2.refine.descriptors import CreateThesaurus

    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : examples/tests/refine/thesaurus/descriptors.the.txt
      Source field : DESCRIPTOR_TOK
      Status       : 2441 items added to the thesaurus.
    <BLANKLINE>

    >>> from techminer2.refine.descriptors.pre_processing_merger import PreProcessingMerger
    >>> (
    ...     PreProcessingMerger()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )
    INFO: Fuzzy cutoff matching completed.
      Success        : True
      Field          : _UNSPECIFIED_
      Thesaurus      : descriptors.the.txt
    <BLANKLINE>


"""

import sys

from techminer2 import CorpusField, ThesaurusField
from techminer2._internals import ParamsMixin
from techminer2.refine._internals.objs.thesaurus_match_result import (
    ThesaurusMatchResult,
)
from techminer2.refine._internals.rules import (
    apply_chemical_compounds_match_rule,
    apply_common_and_basic_rule,
    apply_error_metrics_rule,
    apply_exact_match_rule,
    apply_geographic_names_rule,
    apply_hyphenation_match_rule,
    apply_inflected_verb_forms_rule,
    apply_leading_noise_removal_rule,
    apply_num_punct_to_space_rule,
    apply_number_to_letter_rule,
    apply_plural_singular_match_rule,
    apply_prefer_singular_over_plural_rule,
    apply_punctuation_variation_match_rule,
    apply_scientific_and_academic_rule,
    apply_trailing_noise_removal_rule,
    apply_white_space_normalization_rule,
    apply_xml_encoding_rule,
)

from .._internals.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

PREFERRED = ThesaurusField.PREFERRED.value


class PreProcessingMerger(
    ParamsMixin,
):
    """:meta private:"""

    _HEADER_WIDTH = 70
    _STEP_PREFIX = "  → Rule : "
    _ORDINAL = ["First", "Second"]

    def _write(self, text: str) -> None:
        sys.stderr.write(text)
        sys.stderr.flush()

    def _print_header(self) -> None:
        separator = "=" * self._HEADER_WIDTH
        self._write(f"\n{separator}\nPre-processing Merger\n{separator}\n")

    def run(self) -> ThesaurusMatchResult:

        self.with_thesaurus_file("descriptors.the.txt")
        self.with_source_field(CorpusField.DESCRIPTOR_TOK)

        thesaurus_df = load_thesaurus_as_dataframe(params=self.params)

        self._print_header()

        for phase in range(2):

            self._write(f"\n[{phase+1}] {self._ORDINAL[phase]} Pass\n")

            for msg, rule in [
                ("Exact match", apply_exact_match_rule),
                ("Geographic names", apply_geographic_names_rule),
                ("Error metrics", apply_error_metrics_rule),
                ("Number to letter", apply_number_to_letter_rule),
                ("Num punct to space", apply_num_punct_to_space_rule),
                ("XML encoding", apply_xml_encoding_rule),
                ("White space normalization", apply_white_space_normalization_rule),
                ("Chemical compounds", apply_chemical_compounds_match_rule),
                ("punctuation variation", apply_punctuation_variation_match_rule),
                ("Hyphenation", apply_hyphenation_match_rule),
                ("Plural singular", apply_plural_singular_match_rule),
                ("prefer singular over plural", apply_prefer_singular_over_plural_rule),
                ("common and basic", apply_common_and_basic_rule),
                ("scientific and academic", apply_scientific_and_academic_rule),
                ("inflected verb forms", apply_inflected_verb_forms_rule),
                ("leading noise removal", apply_leading_noise_removal_rule),
                ("trailing noise removal", apply_trailing_noise_removal_rule),
            ]:
                self._write(f"{self._STEP_PREFIX}{msg}\n")
                thesaurus_df = rule(thesaurus_df, self.params)

        thesaurus_df = thesaurus_df.sort_values(by=[PREFERRED])
        save_dataframe_as_thesaurus(params=self.params, dataframe=thesaurus_df)

        return ThesaurusMatchResult(
            colored_output=self.params.colored_output,
            output_file=None,
            thesaurus_file=self.params.thesaurus_file,
            msg="Fuzzy cutoff matching completed.",
            success=True,
            field=self.params.field.value,
        )
