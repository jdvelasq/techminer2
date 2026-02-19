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
      Status       : 2440 items added to the thesaurus.
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

# from tqdm import tqdm  # type: ignore
from techminer2 import CorpusField
from techminer2._internals import ParamsMixin
from techminer2.refine._internals.objs.thesaurus_match_result import (
    ThesaurusMatchResult,
)
from techminer2.refine._internals.rules import (
    apply_chemical_compounds_match_rule,
    apply_common_and_basic_rule,
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


class PreProcessingMerger(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> ThesaurusMatchResult:

        self.with_thesaurus_file("descriptors.the.txt")
        self.with_source_field(CorpusField.DESCRIPTOR_TOK)

        thesaurus_df = load_thesaurus_as_dataframe(params=self.params)

        for rule in [
            apply_exact_match_rule,
            apply_geographic_names_rule,
            apply_leading_noise_removal_rule,
            # apply_trailing_noise_removal_rule,
            apply_number_to_letter_rule,
            apply_num_punct_to_space_rule,
            apply_xml_encoding_rule,
            apply_white_space_normalization_rule,
            apply_chemical_compounds_match_rule,
            apply_punctuation_variation_match_rule,
            apply_hyphenation_match_rule,
            apply_plural_singular_match_rule,
            apply_prefer_singular_over_plural_rule,
            apply_common_and_basic_rule,
            apply_scientific_and_academic_rule,
            apply_inflected_verb_forms_rule,
        ]:
            thesaurus_df = rule(thesaurus_df, self.params)

        save_dataframe_as_thesaurus(params=self.params, dataframe=thesaurus_df)

        return ThesaurusMatchResult(
            colored_output=self.params.colored_output,
            output_file=None,
            thesaurus_file=self.params.thesaurus_file,
            msg="Fuzzy cutoff matching completed.",
            success=True,
            field=self.params.field.value,
        )
