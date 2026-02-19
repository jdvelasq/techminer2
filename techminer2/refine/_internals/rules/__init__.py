from .begins_with_match import apply_begins_with_match_rule
from .case_variation_match import apply_case_variation_match_rule
from .chemical_compounds_match import apply_chemical_compounds_match_rule
from .common_and_basic import apply_common_and_basic_rule
from .contains_pattern_match import apply_contains_pattern_match_rule
from .ends_with_match import apply_ends_with_match_rule
from .error_metrics import apply_error_metrics_rule
from .exact_match import apply_exact_match_rule
from .find_close_match import apply_find_close_match_rule
from .fuzzy_cutoff_1_word_match import apply_fuzzy_cutoff_1_word_match_rule
from .fuzzy_cutoff_match import apply_fuzzy_cutoff_match_rule
from .geographic_names import apply_geographic_names_rule
from .hyphenation_match import apply_hyphenation_match_rule
from .inflected_verb_forms import apply_inflected_verb_forms_rule
from .isolated_word_lemmatization import apply_isolated_word_lemmatization_rule
from .leading_noise_removal import apply_leading_noise_removal_rule
from .num_punct_to_space import apply_num_punct_to_space_rule
from .number_to_letter import apply_number_to_letter_rule
from .plural_singular_match import apply_plural_singular_match_rule
from .prefer_singular_over_plural import apply_prefer_singular_over_plural_rule
from .punctuation_variation_match import apply_punctuation_variation_match_rule
from .regex_pattern_match import apply_regex_pattern_match_rule
from .scientific_and_academic import apply_scientific_and_academic_rule
from .stemming_match import apply_stemming_match_rule
from .stopwords_removal_match import apply_stopwords_removal_match_rule
from .trailing_noise_removal import apply_trailing_noise_removal_rule
from .white_space_normalization import apply_white_space_normalization_rule
from .word_order_match import apply_word_order_match_rule
from .xml_encoding import apply_xml_encoding_rule

__all__ = [
    "apply_begins_with_match_rule",
    "apply_case_variation_match_rule",
    "apply_chemical_compounds_match_rule",
    "apply_common_and_basic_rule",
    "apply_contains_pattern_match_rule",
    "apply_ends_with_match_rule",
    "apply_error_metrics_rule",
    "apply_exact_match_rule",
    "apply_find_close_match_rule",
    "apply_fuzzy_cutoff_1_word_match_rule",
    "apply_fuzzy_cutoff_match_rule",
    "apply_geographic_names_rule",
    "apply_hyphenation_match_rule",
    "apply_inflected_verb_forms_rule",
    "apply_isolated_word_lemmatization_rule",
    "apply_leading_noise_removal_rule",
    "apply_num_punct_to_space_rule",
    "apply_number_to_letter_rule",
    "apply_plural_singular_match_rule",
    "apply_prefer_singular_over_plural_rule",
    "apply_punctuation_variation_match_rule",
    "apply_regex_pattern_match_rule",
    "apply_scientific_and_academic_rule",
    "apply_stemming_match_rule",
    "apply_stopwords_removal_match_rule",
    "apply_trailing_noise_removal_rule",
    "apply_white_space_normalization_rule",
    "apply_word_order_match_rule",
    "apply_xml_encoding_rule",
]
