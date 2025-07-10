"Thesaurus."

from .general.apply_thesaurus import ApplyThesaurus
from .general.cleanup_thesaurus import CleanupThesaurus
from .general.compress_thesaurus import CompressThesaurus
from .general.create_thesaurus import CreateThesaurus, reset_thesaurus
from .general.integrity_check import IntegrityCheck
from .general.reduce_keys import ReduceKeys, reduce_keys
from .remove.remove_determiners import RemoveDeterminers
from .remove.remove_initial_words import RemoveInitialWords
from .remove.remove_last_words import RemoveCommonLastWords
from .remove.remove_parentheses import RemoveParentheses
from .remove.remove_stopwords import RemoveStopwords
from .replace.replace_abbreviations import ReplaceAbbreviations
from .replace.replace_ends_with_word import ReplaceEndsWithWord
from .replace.replace_hyphenated_words import ReplaceHyphenatedWords
from .replace.replace_starts_with_word import ReplaceStartsWithWord
from .replace.replace_word import ReplaceWord, replace
from .sort.find_editorials import FindEditorials
from .sort.sort_by_ends_with_key_match import SortByEndsWithKeyMatch
from .sort.sort_by_exact_key_match import SortByExactKeyMatch, exactmatch
from .sort.sort_by_fuzzy_key_match import SortByFuzzyKeyMatch
from .sort.sort_by_key_match import SortByKeyMatch
from .sort.sort_by_key_order import SortByKeyOrder
from .sort.sort_by_occurrences import SortByOccurrences, sort_by_occurrences
from .sort.sort_by_starts_with_key_match import SortByStartsWithKeyMatch, startswith
from .sort.sort_by_word_key_match import SortByWordKeyMatch
from .translate.american_to_british_spelling import AmericanToBritishSpelling
from .translate.british_to_american_spelling import BritishToAmericanSpelling

__all__ = [
    "ApplyThesaurus",
    "CleanupThesaurus",
    "CompressThesaurus",
    "CreateThesaurus",
    "IntegrityCheck",
    "ReduceKeys",
    "RemoveInitialWords",
    "RemoveCommonLastWords",
    "RemoveDeterminers",
    "RemoveStopwords",
    "RemoveParentheses",
    "ReplaceAbbreviations",
    "ReplaceEndsWithWord",
    "ReplaceHyphenatedWords",
    "ReplaceStartsWithWord",
    "ReplaceWord",
    "FindEditorials",
    "SortByEndsWithKeyMatch",
    "SortByFuzzyKeyMatch",
    "SortByKeyMatch",
    "SortByKeyOrder",
    "SortByOccurrences",
    "SortByStartsWithKeyMatch",
    "SortByWordKeyMatch",
    "AmericanToBritishSpelling",
    "BritishToAmericanSpelling",
    "SortByExactKeyMatch",
    "exactmatch",
    "reduce_keys",
    "replace",
    "reset_thesaurus",
    "sort_by_occurrences",
    "startswith",
]
