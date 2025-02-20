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


"""
import sys

import pandas as pd  # type: ignore
from spellchecker import SpellChecker

from ..._internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_head,
)


class CheckThesaurusForMisspelledTerms(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):

        file_path = self.file_path

        sys.stdout.write("\nINFO  Checking thesaurus mispelled keys.")
        sys.stdout.write(f"\n        Thesaurus file: {file_path}")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_03_load_thesaurus_as_mapping(self):
        self.mapping = internal__load_thesaurus_as_mapping(self.file_path)

    # -------------------------------------------------------------------------
    def step_04_extract_words_from_mapping(self):
        terms = list(self.mapping.keys())
        terms = [t.replace("_", " ") for t in terms]
        words = [word for term in terms for word in term.split(" ")]
        words = pd.Series(words).value_counts()
        words = words[words <= self.params.maximum_occurrence]
        words = [word for word in words.index if word.isalpha()]
        self.words = words

    # -------------------------------------------------------------------------
    def step_05_search_mispelled_words(self):
        spell = SpellChecker()
        misspelled_words = spell.unknown(self.words)
        misspelled_words = sorted(misspelled_words)
        self.misspelled_words = misspelled_words

    # -------------------------------------------------------------------------
    def step_06_print_mispelled_words(self):
        if len(self.misspelled_words) == 0:
            sys.stdout.write("\n        No misspelled words found.")
            sys.stdout.flush()
            return

        misspelled_words = self.misspelled_words[:10]
        for i_word, word in enumerate(misspelled_words):
            if i_word == 0:
                sys.stdout.write(f"\n        Words: {word}")
            else:
                sys.stdout.write(f"\n               {word}")
        if len(misspelled_words) == 10:
            sys.stdout.write("\n               ...")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_07_sort_thesaurus_on_disk(self):

        if len(self.misspelled_words) == 0:
            return

        # loads a new copy of the thesaurus
        data_frame = internal__load_thesaurus_as_data_frame(file_path=self.file_path)

        # search for misspelled words
        data_frame["misspelled"] = 0
        data_frame["fingerprint"] = data_frame["key"].str.lower().str.replace("_", " ")
        for word in self.misspelled_words:
            word = r"\b" + word + r"\b"
            data_frame.loc[
                data_frame["fingerprint"].str.contains(word, regex=True), "misspelled"
            ] = 1
        data_frame = data_frame.drop(columns=["fingerprint"])

        misspelled_data_frame = data_frame[data_frame["misspelled"] == 1]
        if len(misspelled_data_frame) == 0:
            return
        data_frame = data_frame[data_frame["misspelled"] == 0]

        # writes the thesaurus to disk
        with open(self.file_path, "w", encoding="utf-8") as file:

            # writes the misspelled words
            grouped = misspelled_data_frame.groupby("key").agg({"value": list})
            for key, values in grouped.iterrows():
                file.write(key + "\n")
                for value in values["value"]:
                    file.write("    " + value + "\n")

            # writes the correct words
            grouped = data_frame.groupby("key").agg({"value": list})
            for key, values in grouped.iterrows():
                file.write(key + "\n")
                for value in values["value"]:
                    file.write("    " + value + "\n")

    # -------------------------------------------------------------------------
    def step_08_print_info_tail(self):
        sys.stdout.write("\n        Done.")
        internal__print_thesaurus_head(file_path=self.file_path)
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_thesaurus_as_mapping()
        self.step_04_extract_words_from_mapping()
        self.step_05_search_mispelled_words()
        self.step_06_print_mispelled_words()
        self.step_07_sort_thesaurus_on_disk()
        self.step_08_print_info_tail()


# =============================================================================
