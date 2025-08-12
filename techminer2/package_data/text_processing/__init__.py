"""Text Processing"""

from .load_text_processing_terms import internal__load_text_processing_terms
from .sort_text_processing_terms import internal__sort_text_processing_terms
from .check_noun_phrases import internal__check_noun_phrases
from .save_text_processing_terms import internal__save_text_processing_terms
from .sort_noun_phrases_by_last_word import internal__sort_noun_phrases_by_last_word

__all__ = [
    "internal__load_text_processing_terms",
    "internal__sort_text_processing_terms",
    "internal__check_noun_phrases",
    "internal__save_text_processing_terms",
    "internal__sort_noun_phrases_by_last_word",
]
