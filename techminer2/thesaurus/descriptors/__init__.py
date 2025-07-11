"Thesaurus."

from .general.apply_thesaurus import ApplyThesaurus
from .general.cleanup_thesaurus import CleanupThesaurus
from .general.compress_thesaurus import CompressThesaurus
from .general.create_thesaurus import CreateThesaurus
from .general.integrity_check import IntegrityCheck
from .general.reduce_keys import ReduceKeys
from .remove.remove_determiners import RemoveDeterminers
from .remove.remove_initial_words import RemoveInitialWords
from .remove.remove_last_words import RemoveLastWords
from .remove.remove_parentheses import RemoveParentheses
from .remove.remove_stopwords import RemoveStopwords
from .replace.replace_abbreviations import ReplaceAbbreviations
from .replace.replace_hyphenated_words import ReplaceHyphenatedWords
from .replace.replace_initial_word import ReplaceInitialWord
from .replace.replace_last_word import ReplaceLastWord
from .replace.replace_word import ReplaceWord
from .sort.find_editorials import FindEditorials
from .sort.sort_by_alphabet import SortByAlphabet
from .sort.sort_by_endswith_match import SortByEndsWithMatch
from .sort.sort_by_exact_match import SortByExactMatch
from .sort.sort_by_fuzzy_match import SortByFuzzyMatch
from .sort.sort_by_key_length import SortByKeyLength
from .sort.sort_by_match import SortByMatch
from .sort.sort_by_occurrences import SortByOccurrences
from .sort.sort_by_startswith_match import SortByStartsWithMatch
from .sort.sort_by_word_length import SortByWordLength
from .sort.sort_by_word_match import SortByWordMatch
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
    "RemoveLastWords",
    "RemoveDeterminers",
    "RemoveStopwords",
    "RemoveParentheses",
    "ReplaceAbbreviations",
    "ReplaceLastWord",
    "ReplaceHyphenatedWords",
    "ReplaceInitialWord",
    "ReplaceWord",
    "FindEditorials",
    "SortByAlphabet",
    "SortByEndsWithMatch",
    "SortByFuzzyMatch",
    "SortByMatch",
    "SortByKeyLength",
    "SortByOccurrences",
    "SortByStartsWithMatch",
    "SortByWordMatch",
    "SortByWordLength",
    "AmericanToBritishSpelling",
    "BritishToAmericanSpelling",
    "SortByExactMatch",
    "exactmatch",
    "reduce_keys",
    "replace",
    "reset_thesaurus",
    "sort_by_occurrences",
    "startswith",
]
