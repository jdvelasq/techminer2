from .._intern.sort._old.sort_by_occurrences import SortByOccurrences
from .clean._old.are_synonymous import AreSynonymous
from .clean._old.combine_keys import CombineKeys
from .clean._old.define_term import DefineTerm
from .clean._old.is_stopword import IsStopword
from .clean._old.merge_synonymous import MergeSynonymous
from .clean._old.populate_stopwords import PopulateStopwords
from .general._old.apply_thesaurus import ApplyThesaurus
from .general._old.clump_keys import ClumpKeys
from .general._old.cutoff_fuzzy_merging import CutoffFuzzyMerging
from .general._old.get_contexts import GetContexts
from .general._old.get_values import GetValues
from .general._old.initialize_thesaurus import InitializeThesaurus
from .general._old.integrity_check import IntegrityCheck
from .general._old.merge_keys import MergeKeys
from .general._old.normalize_keys import NormalizeKeys
from .general._old.reduce_keys import ReduceKeys
from .general._old.spell_check import SpellCheck
from .register.register_initial_word import RegisterInitialWord
from .register.register_keyword import RegisterKeyword
from .register.register_last_word import RegisterLastWord
from .remove._old.remove_determiners import RemoveDeterminers
from .remove._old.remove_initial_words import RemoveInitialWords
from .remove._old.remove_last_words import RemoveLastWords
from .remove._old.remove_parentheses import RemoveParentheses
from .remove._old.remove_stopwords import RemoveStopwords
from .replace._old.replace_acronyms import ReplaceAcronyms
from .replace._old.replace_hyphenated_words import ReplaceHyphenatedWords
from .replace._old.replace_initial_word import ReplaceInitialWord
from .replace._old.replace_last_word import ReplaceLastWord
from .replace._old.replace_word import ReplaceWord
from .sort._old.sort_by_alphabet import SortByAlphabet
from .sort._old.sort_by_exact_match import SortByExactMatch
from .sort._old.sort_by_fuzzy_match import SortByFuzzyMatch
from .sort._old.sort_by_initial_words import SortByInitialWords
from .sort._old.sort_by_key_length import SortByKeyLength
from .sort._old.sort_by_last_word import SortByLastWords
from .sort._old.sort_by_match import SortByMatch
from .sort._old.sort_by_startswith_match import SortByStartsWithMatch
from .sort._old.sort_by_stopwords import SortByStopwords
from .sort._old.sort_by_word_length import SortByWordLength
from .sort._old.sort_by_word_match import SortByWordMatch
from .translate.american_to_british_spelling import AmericanToBritishSpelling
from .translate.british_to_american_spelling import BritishToAmericanSpelling

__all__ = [
    "AmericanToBritishSpelling",
    "ApplyThesaurus",
    "AreSynonymous",
    "BritishToAmericanSpelling",
    "ClumpKeys",
    "CombineKeys",
    "CutoffFuzzyMerging",
    "DefineTerm",
    "GetContexts",
    "GetValues",
    "InitializeThesaurus",
    "IntegrityCheck",
    "IsStopword",
    "MergeKeys",
    "MergeSynonymous",
    "NormalizeKeys",
    "PopulateStopwords",
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
    "SpellCheck",
]
