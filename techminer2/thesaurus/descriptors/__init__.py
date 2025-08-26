"Public API for descriptors."

from .general.apply_thesaurus import ApplyThesaurus
from .general.clump_keys import ClumpKeys
from .general.combine_keys import CombineKeys
from .general.cutoff_fuzzy_merging import CutoffFuzzyMerging
from .general.get_values import GetValues
from .general.initialize_thesaurus import InitializeThesaurus
from .general.integrity_check import IntegrityCheck
from .general.merge_keys import MergeKeys
from .general.normalize_keys import NormalizeKeys
from .general.reduce_keys import ReduceKeys
from .general.spell_check import SpellCheck
from .register.register_initial_word import RegisterInitialWord
from .register.register_keyword import RegisterKeyword
from .register.register_last_word import RegisterLastWord
from .remove.remove_determiners import RemoveDeterminers
from .remove.remove_initial_words import RemoveInitialWords
from .remove.remove_last_words import RemoveLastWords
from .remove.remove_parentheses import RemoveParentheses
from .remove.remove_stopwords import RemoveStopwords
from .replace.replace_acronyms import ReplaceAcronyms
from .replace.replace_hyphenated_words import ReplaceHyphenatedWords
from .replace.replace_initial_word import ReplaceInitialWord
from .replace.replace_last_word import ReplaceLastWord
from .replace.replace_word import ReplaceWord
from .sort.sort_by_alphabet import SortByAlphabet
from .sort.sort_by_endswith_match import SortByEndsWithMatch
from .sort.sort_by_exact_match import SortByExactMatch
from .sort.sort_by_fuzzy_match import SortByFuzzyMatch
from .sort.sort_by_initial_words import SortByInitialWords
from .sort.sort_by_key_length import SortByKeyLength
from .sort.sort_by_last_word import SortByLastWords
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
    "CombineKeys",
    "GetValues",
    "NormalizeKeys",
    "ClumpKeys",
    "CutoffFuzzyMerging",
    "IntegrityCheck",
    "InitializeThesaurus",
    "ReduceKeys",
    "RegisterInitialWord",
    "RegisterKeyword",
    "RegisterLastWord",
    "RemoveDeterminers",
    "RemoveInitialWords",
    "RemoveLastWords",
    "RemoveParentheses",
    "RemoveStopwords",
    "ReplaceAcronyms",
    "ReplaceHyphenatedWords",
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
    "MergeKeys",
    "SpellCheck",
]
