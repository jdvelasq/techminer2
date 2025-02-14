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

>>> from techminer2.thesaurus.user import CleanupThesaurus
>>> (
...     CleanupThesaurus()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- The thesaurus file 'example/thesaurus/descriptors.the.txt' has been cleaned up.

"""
import sys

import pandas as pd  # type: ignore
from spellchecker import SpellChecker
from textblob import TextBlob, Word  # type: ignore

from ...internals.mixins import ParamsMixin
from ...package_data.database import internal__load_technical_stopwords
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
)


class CleanupThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def create_new_key_column(self, data_frame):
        data_frame["new_key"] = data_frame["key"].str.lower()
        return data_frame

    # -------------------------------------------------------------------------
    def remove_technical_stopwords(self, data_frame):
        stopwords = internal__load_technical_stopwords()
        data_frame["new_key"] = data_frame["new_key"].apply(
            lambda x: " ".join([word for word in x.split() if word not in stopwords])
        )
        return data_frame

    # -------------------------------------------------------------------------
    def apply_word_correction(self, data_frame):
        data_frame["new_key"] = data_frame["new_key"].apply(
            lambda x: TextBlob(x).correct()
        )
        return data_frame

    # -------------------------------------------------------------------------
    def apply_stemming_to_new_key_column(self, data_frame):
        data_frame["new_key"] = data_frame["new_key"].apply(
            lambda x: " ".join([Word(word).stem() for word in x.split()])
        )
        return data_frame

    # -------------------------------------------------------------------------
    def build_new_keys_mapping(self, data_frame):
        data_frame = data_frame[["key", "new_key"]]
        data_frame = data_frame.drop_duplicates()
        data_frame = data_frame.set_index("new_key")
        mapping = data_frame["key"].to_dict()
        return mapping

    # -------------------------------------------------------------------------
    def build_cleaned_key(self, data_frame, mapping):
        data_frame["key"] = data_frame["new_key"].apply(lambda x: mapping[x])
        return data_frame

    # -------------------------------------------------------------------------
    def save_thesaurus_on_disk(self, file_path, data_frame):
        data_frame = data_frame.sort_values(by=["key", "value"])
        with open(file_path, "w", encoding="utf-8") as file:
            for key, value in data_frame.groupby("key"):
                file.write(key + "\n")
                for value in value["value"]:
                    file.write("    " + value + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        data_frame = internal__load_thesaurus_as_data_frame(file_path=file_path)
        data_frame = self.create_new_key_column(data_frame)
        data_frame = self.remove_technical_stopwords(data_frame)
        # data_frame = self.apply_word_correction(data_frame)
        data_frame = self.apply_stemming_to_new_key_column(data_frame)
        mapping = self.build_new_keys_mapping(data_frame)
        data_frame = self.build_cleaned_key(data_frame, mapping)
        self.save_thesaurus_on_disk(file_path, data_frame)

        sys.stdout.write(
            f"--INFO-- The thesaurus file '{file_path}' has been cleaned up."
        )
        sys.stdout.flush()


# =============================================================================
