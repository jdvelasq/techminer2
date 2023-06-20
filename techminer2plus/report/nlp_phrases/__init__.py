"""
This module contains functions for computing keywords indicators.

"""
from .most_frequent_words import most_frequent_words
from .treemap import treemap
from .trending_words_per_year import trending_words_per_year
from .word_cloud import word_cloud
from .words_frequency_over_time import words_frequency_over_time

__all__ = [
    "most_frequent_words",
    "treemap",
    "trending_words_per_year",
    "word_cloud",
    "words_frequency_over_time",
]
