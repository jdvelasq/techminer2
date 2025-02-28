"""Thesaurus module."""

from .general.apply_thesaurus import ApplyThesaurus
from .general.create_thesaurus import CreateThesaurus
from .general.integrity_check import IntegrityCheck
from .general.reduce_keys import ReduceKeys
from .general.spell_check import SpellCheck
from .replace.replace_ends_with_word import ReplaceEndsWithWord
from .replace.replace_starts_with_word import ReplaceStartsWithWord
from .replace.replace_word import ReplaceWord
from .sort.sort_by_ends_with_key_match import SortByEndsWithKeyMatch
from .sort.sort_by_fuzzy_key_match import SortByFuzzyKeyMatch
from .sort.sort_by_key_match import SortByKeyMatch
from .sort.sort_by_key_order import SortByKeyOrder
from .sort.sort_by_starts_with_key_match import SortByStartsWithKeyMatch
from .sort.sort_by_word_match import SortByWordMatch
from .translate.translate_american_to_british_spelling import (
    TranslateAmericanToBritishSpelling,
)
from .translate.translate_british_to_american_spelling import (
    TranslateBritishToAmericanSpelling,
)

__all__ = [
    "ApplyThesaurus",
    "CreateThesaurus",
    "IntegrityCheck",
    "ReduceKeys",
    "SpellCheck",
    "ReplaceEndsWithWord",
    "ReplaceStartsWithWord",
    "ReplaceWord",
    "SortByEndsWithKeyMatch",
    "SortByWordMatch",
    "SortByFuzzyKeyMatch",
    "SortByKeyMatch",
    "SortByKeyOrder",
    "SortByStartsWithKeyMatch",
    "TranslateAmericanToBritishSpelling",
    "TranslateBritishToAmericanSpelling",
]
