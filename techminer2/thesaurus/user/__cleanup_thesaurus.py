# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Cleanup Thesaurus
===============================================================================

>>> # TEST:
>>> from techminer2.thesaurus._internals import internal__print_thesaurus_head
>>> from techminer2._internals import Params
>>> params = Params().update(thesaurus_file="demo.the.txt", root_dir="example/")


>>> from techminer2.thesaurus.user import CleanupThesaurus
>>> (
...     CleanupThesaurus()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )

             
"""
import sys
from functools import lru_cache  # type: ignore

from textblob import Word  # type: ignore

from ..._internals.log_message import internal__log_message
from ..._internals.mixins import ParamsMixin
from ...package_data.text_processing import internal__load_text_processing_terms
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
)

# from spellchecker import SpellChecker
# from textblob import TextBlob, Word  # type: ignore


PARTICLES = [
    "aided",
    "and the",
    "and",
    "applied to",
    "assisted",
    "at",
    "based",
    "for",
    "in",
    "like",
    "of the",
    "of using",
    "of",
    "on",
    "s",
    "sized",
    "to",
    "under",
    "using",
]


class CleanupThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):

        file_path = self.file_path
        sys.stdout.write("\nINFO  Sorting thesaurus by match.")
        sys.stdout.write(f"\n            Thesaurus file: {file_path}")

    # -------------------------------------------------------------------------
    def step_03_load_thesaurus_as_data_frame(self):
        self.data_frame = internal__load_thesaurus_as_data_frame(
            file_path=self.file_path
        )

    # -------------------------------------------------------------------------
    def step_04_create_fingerprint_column(self):
        self.data_frame["fingerprint"] = (
            self.data_frame["key"]
            .str.lower()
            .replace("-", " ", regex=False)
            .replace("_", " ", regex=False)
        )

    # -------------------------------------------------------------------------
    def step_05_remove_particles_from_fingerprints(self):
        for particle in PARTICLES:
            self.data_frame["fingerprint"] = self.data_frame["fingerprint"].str.replace(
                f" {particle} ",
                " ",
                regex=False,
            )

    # -------------------------------------------------------------------------
    def step_06_remove_technical_stopwords_from_fingerprints(self):
        stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].apply(
            lambda x: " ".join([word for word in x.split() if word not in stopwords])
        )

    # -------------------------------------------------------------------------
    def step_07_singularize_fingerprint_words(self):
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].apply(
            lambda x: " ".join([Word(word).singularize() for word in x.split()])
        )

    # -------------------------------------------------------------------------
    def step_08_build_fingerprint2key_mapping(self):
        data_frame = self.data_frame[["key", "fingerprint"]]
        data_frame = data_frame.drop_duplicates()
        data_frame = data_frame.set_index("fingerprint")
        self.mapping = data_frame["key"].to_dict()

    # -------------------------------------------------------------------------
    def step_09_build_cleaned_key_from_fingerprints(self):
        self.data_frame["key"] = self.data_frame["fingerprint"].apply(
            lambda x: self.mapping[x]
        )

    # -------------------------------------------------------------------------
    def step_10_save_thesaurus_on_disk(self):
        self.data_frame = self.data_frame.sort_values(by=["key", "value"])
        with open(self.file_path, "w", encoding="utf-8") as file:
            for key, value in self.data_frame.groupby("key"):
                file.write(key + "\n")
                for value in value["value"]:
                    file.write("    " + value + "\n")

    # -------------------------------------------------------------------------
    def step_11_print_info_tail(self):
        sys.stdout.write("\n        Done.")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_thesaurus_as_data_frame()
        self.step_04_create_fingerprint_column()
        self.step_05_remove_particles_from_fingerprints()
        self.step_06_remove_technical_stopwords_from_fingerprints()
        self.step_07_singularize_fingerprint_words()
        self.step_08_build_fingerprint2key_mapping()
        self.step_09_build_cleaned_key_from_fingerprints()
        self.step_10_save_thesaurus_on_disk()
        self.step_11_print_info_tail()


# =============================================================================
