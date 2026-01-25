"""Text Processing"""

from .check_noun_phrases import internal__check_noun_phrases
from .load_text_processing_terms import load_text_processing_terms
from .save_text_processing_terms import save_text_processing_terms
from .sort_noun_phrases_by_last_word import internal__sort_noun_phrases_by_last_word
from .sort_text_processing_terms import internal__sort_text_processing_terms

__all__ = [
    "load_text_processing_terms",
    "internal__sort_text_processing_terms",
    "internal__check_noun_phrases",
    "save_text_processing_terms",
    "internal__sort_noun_phrases_by_last_word",
]
