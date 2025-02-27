"""Thesaurus module."""

from .apply_thesaurus import ApplyThesaurus
from .create_thesaurus import CreateThesaurus
from .integrity_check import IntegrityCheck
from .reduce_keys import ReduceKeys
from .replace.replace_ends_with_word import ReplaceEndsWithWord
from .replace.replace_starts_with_word import ReplaceStartsWithWord
from .replace.replace_word import ReplaceWord
from .sort.sort_by_ends_with_key_match import SortByEndsWithKeyMatch
from .sort.sort_by_fuzzy_key_match import SortByFuzzyKeyMatch
from .sort.sort_by_key_match import SortByKeyMatch
from .sort.sort_by_key_order import SortByKeyOrder
from .sort.sort_by_starts_with_key_match import SortByStartsWithKeyMatch
from .spell_check import SpellCheck
from .TO_REVIEW._cleanup_thesaurus import CleanupThesaurus
from .TO_REVIEW.common_ending_words_remover import CommonEndingWordsRemover
from .TO_REVIEW.common_starting_words_remover import CommonStartingWordsRemover
from .TO_REVIEW.hyphenated_words_transformer import HyphenatedWordsTransformer
from .TO_REVIEW.parentheses_remover import ParenthesesRemover
from .TO_REVIEW.starting_determiners_remover import StartingDeterminersRemover
from .TO_REVIEW.starting_stopwords_remover import StartingStopwordsRemover
from .translate.translate_american_to_british_spelling import (
    TranslateAmericanToBritishSpelling,
)
from .translate.translate_british_to_american_spelling import (
    TranslateBritishToAmericanSpelling,
)
