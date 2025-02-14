"""Text Processing"""

from .load_common_ending_words import internal__load_common_ending_words
from .load_common_starting_words import internal__load_common_starting_words
from .load_connectors import internal__load_connectors
from .load_determiners import internal__load_determiners
from .load_hypened_words import internal__load_hypened_words
from .load_known_noun_phrases import internal__load_known_noun_phrases
from .load_technical_stopwords import internal__load_technical_stopwords
from .load_text_processing_terms import internal__load_text_processing_terms
from .sort_lines_in_data_files import internal__sort_lines_in_data_files

__all__ = [
    "internal__load_common_ending_words",
    "internal__load_common_starting_words",
    "internal__load_hypened_words",
    "internal__load_connectors",
    "internal__load_determiners",
    "internal__load_known_noun_phrases",
    "internal__load_technical_stopwords",
    "internal__load_text_processing_terms",
    "internal__sort_lines_in_data_files",
]
