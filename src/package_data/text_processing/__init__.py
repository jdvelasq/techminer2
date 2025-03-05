"""Text Processing"""

from .load_text_processing_terms import internal__load_text_processing_terms
from .sort_hypened_words_alphabetically import (
    internal__sort_hypened_words_alphabetically,
)
from .sort_hypened_words_reversed import internal__sort_hypened_words_reversed
from .sort_text_processing_terms import internal__sort_text_processing_terms

__all__ = [
    "internal__load_text_processing_terms",
    "internal__sort_hypened_words_alphabetically",
    "internal__sort_hypened_words_reversed",
    "internal__sort_text_processing_terms",
]
