"""Thesaurus module."""

from .general.apply_thesaurus import ApplyThesaurus
from .general.compress_thesaurus import CompressThesaurus
from .general.create_thesaurus import CreateThesaurus
from .general.explode_keys import ExplodeKeys
from .general.integrity_check import IntegrityCheck
from .general.reduce_keys import ReduceKeys
from .general.spell_check import SpellCheck
from .replace.replace_ends_with_word import ReplaceEndsWithWord
from .replace.replace_starts_with_word import ReplaceStartsWithWord
from .replace.replace_word import ReplaceWord
from .sort.sort_by_ends_with_key_match import SortByEndsWithKeyMatch
from .sort.sort_by_exact_key_match import SortByExactKeyMatch
from .sort.sort_by_fuzzy_key_match import SortByFuzzyKeyMatch
from .sort.sort_by_key_match import SortByKeyMatch
from .sort.sort_by_key_order import SortByKeyOrder
from .sort.sort_by_match import SortByMatch
from .sort.sort_by_occurrences import SortByOccurrences
from .sort.sort_by_starts_with_key_match import SortByStartsWithKeyMatch
from .sort.sort_by_word_key_match import SortByWordKeyMatch
from .translate.american_to_british_spelling import AmericanToBritishSpelling
from .translate.british_to_american_spelling import BritishToAmericanSpelling

__all__ = [
    "AmericanToBritishSpelling",
    "ApplyThesaurus",
    "BritishToAmericanSpelling",
    "CompressThesaurus",
    "CreateThesaurus",
    "ExplodeKeys",
    "IntegrityCheck",
    "ReduceKeys",
    "ReplaceEndsWithWord",
    "ReplaceStartsWithWord",
    "ReplaceWord",
    "SortByEndsWithKeyMatch",
    "SortByExactKeyMatch",
    "SortByFuzzyKeyMatch",
    "SortByKeyMatch",
    "SortByKeyOrder",
    "SortByMatch",
    "SortByOccurrences",
    "SortByStartsWithKeyMatch",
    "SortByWordKeyMatch",
    "SpellCheck",
]
