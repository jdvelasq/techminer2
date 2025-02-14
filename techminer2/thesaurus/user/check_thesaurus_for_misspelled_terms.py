# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Check Thesaurus for Misspelled Terms
===============================================================================

>>> from techminer2.thesaurus.user import CheckThesaurusForMisspelledTerms
>>> (
...     CheckThesaurusForMisspelledTerms()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_maximum_occurrence(3)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- The thesaurus file 'example/thesaurus/descriptors.the.txt' has been processed.

"""
import sys
from os.path import isfile, join

import pandas as pd  # type: ignore
from spellchecker import SpellChecker
from textblob import TextBlob  # type: ignore

from ...internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_reversed_thesaurus_as_mapping,
    internal__load_thesaurus_as_data_frame,
)


class CheckThesaurusForMisspelledTerms(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def load_terms_in_thesaurus(self, file_path):
        reversed_th_dict = internal__load_reversed_thesaurus_as_mapping(file_path)
        terms = list(reversed_th_dict.keys())
        return terms

    # -------------------------------------------------------------------------
    def extract_and_filter_words_from_terms(self, terms):
        words = [word for term in terms for word in term.split("_")]
        words = pd.Series(words).value_counts()
        words = words[words <= self.params.maximum_occurrence]
        words = [word for word in words.index if word.isalpha()]
        return words

    # -------------------------------------------------------------------------
    def extract_mispelled_words(self, words):
        spell = SpellChecker()
        misspelled_words = spell.unknown(words)
        misspelled_words = sorted(misspelled_words)
        return misspelled_words

    # -------------------------------------------------------------------------
    def sort_thesaurus_on_disk(self, misspelled_words):
        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        data_frame = internal__load_thesaurus_as_data_frame(file_path=file_path)
        data_frame["misspelled"] = 0
        for word in misspelled_words:
            data_frame.loc[data_frame["key"].str.contains(word), "misspelled"] = 1
        data_frame = data_frame.sort_values(
            by=["misspelled", "key"], ascending=[False, True]
        )
        data_frame = data_frame.drop(columns=["misspelled"])
        gropued = data_frame.groupby("key").agg({"value": list})
        with open(file_path, "w", encoding="utf-8") as file:
            for key, values in gropued.iterrows():
                file.write(key + "\n")
                for value in values["value"]:
                    file.write("    " + value + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        terms = self.load_terms_in_thesaurus(file_path)
        words = self.extract_and_filter_words_from_terms(terms)
        misspelled_words = self.extract_mispelled_words(words)
        self.sort_thesaurus_on_disk(misspelled_words)

        sys.stdout.write(
            f"--INFO-- The thesaurus file '{file_path}' has been processed."
        )
        sys.stdout.flush()


# =============================================================================
