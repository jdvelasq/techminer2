from .begins_with import apply_begins_with_rule
from .case_variation import apply_case_variation_rule
from .chemical_compounds import apply_chemical_compounds_rule
from .common_and_basic import apply_common_and_basic_rule
from .contains_pattern import apply_contains_pattern_rule
from .ends_with import apply_ends_with_rule
from .error_metrics import apply_error_metrics_rule
from .exact_match import apply_exact_match_rule
from .find_close_match import apply_find_close_match_rule
from .fuzzy_cutoff_0_word import apply_fuzzy_cutoff_match_rule
from .fuzzy_cutoff_1_word import apply_fuzzy_cutoff_1_word_match_rule
from .geographic_names import apply_geographic_names_rule
from .hyphenation import apply_hyphenation_rule
from .inflected_verb_forms import apply_inflected_verb_forms_rule
from .isolated_word_lemmatization import apply_isolated_word_lemmatization_rule
from .leading_noise_removal import apply_leading_noise_removal_rule
from .num_punct_to_space import apply_num_punct_to_space_rule
from .number_to_letter import apply_number_to_letter_rule
from .plural_singular import apply_plural_singular_rule
from .prefer_singular_over_plural import apply_prefer_singular_over_plural_rule
from .punctuation_variation import apply_punctuation_variation_rule
from .regex_pattern import apply_regex_pattern_rule
from .scientific_and_academic import apply_scientific_and_academic_rule
from .stemming import apply_stemming_rule
from .stopwords_removal import apply_stopwords_removal_rule
from .trailing_noise_removal import apply_trailing_noise_removal_rule
from .white_space_normalization import apply_white_space_normalization_rule
from .word_order import apply_word_order_rule
from .xml_encoding import apply_xml_encoding_rule

__all__ = [
    "apply_begins_with_rule",
    "apply_case_variation_rule",
    "apply_chemical_compounds_rule",
    "apply_common_and_basic_rule",
    "apply_contains_pattern_rule",
    "apply_ends_with_rule",
    "apply_error_metrics_rule",
    "apply_exact_match_rule",
    "apply_find_close_match_rule",
    "apply_fuzzy_cutoff_1_word_match_rule",
    "apply_fuzzy_cutoff_match_rule",
    "apply_geographic_names_rule",
    "apply_hyphenation_rule",
    "apply_inflected_verb_forms_rule",
    "apply_isolated_word_lemmatization_rule",
    "apply_leading_noise_removal_rule",
    "apply_num_punct_to_space_rule",
    "apply_number_to_letter_rule",
    "apply_plural_singular_rule",
    "apply_prefer_singular_over_plural_rule",
    "apply_punctuation_variation_rule",
    "apply_regex_pattern_rule",
    "apply_scientific_and_academic_rule",
    "apply_stemming_rule",
    "apply_stopwords_removal_rule",
    "apply_trailing_noise_removal_rule",
    "apply_white_space_normalization_rule",
    "apply_word_order_rule",
    "apply_xml_encoding_rule",
]
