"""Thesaurus module."""

from .general.apply_thesaurus import ApplyThesaurus
from .general.compress_thesaurus import CompressThesaurus
from .general.explode_keys import ExplodeKeys
from .general.initialize_thesaurus import InitializeThesaurus
from .general.integrity_check import IntegrityCheck
from .general.reduce_keys import ReduceKeys
from .general.spell_check import SpellCheck
from .replace.replace_initial_word import ReplaceInitialWord
from .replace.replace_last_word import ReplaceLastWord
from .replace.replace_word import ReplaceWord
from .sort.sort_by_alphabet import SortByAlphabet
from .sort.sort_by_endswith_match import SortByEndsWithMatch
from .sort.sort_by_exact_match import SortByExactMatch
from .sort.sort_by_fuzzy_match import SortByFuzzyMatch
from .sort.sort_by_initial_words import SortByInitialWords
from .sort.sort_by_key_length import SortByKeyLength
from .sort.sort_by_last_words import SortByLastWords
from .sort.sort_by_match import SortByMatch
from .sort.sort_by_occurrences import SortByOccurrences
from .sort.sort_by_startswith_match import SortByStartsWithMatch
from .sort.sort_by_stopwords import SortByStopwords
from .sort.sort_by_word_length import SortByWordLength
from .sort.sort_by_word_match import SortByWordMatch
from .translate.american_to_british_spelling import AmericanToBritishSpelling
from .translate.british_to_american_spelling import BritishToAmericanSpelling

__all__ = [
    "ApplyThesaurus",
    "CompressThesaurus",
    "ExplodeKeys",
    "InitializeThesaurus",
    "IntegrityCheck",
    "ReduceKeys",
    "SpellCheck",
    "ReplaceInitialWord",
    "ReplaceLastWord",
    "ReplaceWord",
    "SortByAlphabet",
    "SortByEndsWithMatch",
    "SortByExactMatch",
    "SortByFuzzyMatch",
    "SortByInitialWords",
    "SortByKeyLength",
    "SortByLastWords",
    "SortByMatch",
    "SortByOccurrences",
    "SortByStartsWithMatch",
    "SortByStopwords",
    "SortByWordLength",
    "SortByWordMatch",
    "AmericanToBritishSpelling",
    "BritishToAmericanSpelling",
]
