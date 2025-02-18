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

## >>> from techminer2.thesaurus.user import CleanupThesaurus
## >>> (
## ...     CleanupThesaurus()
## ...     # 
## ...     # THESAURUS:
## ...     .with_thesaurus_file("descriptors.the.txt")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )
--INFO-- The thesaurus file 'example/thesaurus/descriptors.the.txt' has been cleaned up.

"""

from functools import lru_cache  # type: ignore

from textblob import Word  # type: ignore

from ...internals.log_message import internal__log_message
from ...internals.mixins import ParamsMixin
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
    "based ",
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
    def step_01_create_fingerprint_column(self, data_frame):
        data_frame["fingerprint"] = (
            data_frame["key"]
            .str.lower()
            .replace("-", " ", regex=False)
            .replace("_", " ", regex=False)
        )
        return data_frame

    # -------------------------------------------------------------------------
    def step_02_remove_particles_from_fingerprints(self, data_frame):
        for particle in PARTICLES:
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                f" {particle} ",
                " ",
                regex=False,
            )
        return data_frame

    # -------------------------------------------------------------------------
    def step_03_remove_technical_stopwords_from_fingerprints(self, data_frame):
        stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
        data_frame["fingerprint"] = data_frame["fingerprint"].apply(
            lambda x: " ".join([word for word in x.split() if word not in stopwords])
        )
        return data_frame

    # -------------------------------------------------------------------------
    # def step_04_apply_porter_stemmer_to_fingerprints(self, data_frame):
    #     data_frame["fingerprint"] = data_frame["fingerprint"].apply(
    #         lambda x: " ".join([Word(word).stem() for word in x.split()])
    #     )
    #     return data_frame

    # -------------------------------------------------------------------------
    def step_04_singularize_fingerprint_words(self, data_frame):
        data_frame["fingerprint"] = data_frame["fingerprint"].apply(
            lambda x: " ".join([Word(word).singularize() for word in x.split()])
        )
        return data_frame

    # -------------------------------------------------------------------------
    def step_05_build_fingerprint2key_mapping(self, data_frame):
        data_frame = data_frame[["key", "fingerprint"]]
        data_frame = data_frame.drop_duplicates()
        data_frame = data_frame.set_index("fingerprint")
        mapping = data_frame["key"].to_dict()
        return mapping

    # -------------------------------------------------------------------------
    def step_06_build_cleaned_key_from_fingerprints(self, data_frame, mapping):
        data_frame["key"] = data_frame["fingerprint"].apply(lambda x: mapping[x])
        return data_frame

    # -------------------------------------------------------------------------
    def step_08_save_thesaurus_on_disk(self, file_path, data_frame):
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
        #
        # LOG:
        internal__log_message(
            msgs=[
                "Cleaninig up thesaurus.",
                "  Thesaurus file: '{file_path}'.",
            ],
            prompt_flag=self.params.prompt_flag,
        )
        #
        data_frame = internal__load_thesaurus_as_data_frame(file_path=file_path)
        data_frame = self.step_01_create_fingerprint_column(data_frame)
        data_frame = self.step_03_remove_technical_stopwords_from_fingerprints(
            data_frame
        )
        data_frame = self.step_04_singularize_fingerprint_words(data_frame)
        mapping = self.step_05_build_fingerprint2key_mapping(data_frame)
        data_frame = self.step_06_build_cleaned_key_from_fingerprints(
            data_frame, mapping
        )
        self.step_08_save_thesaurus_on_disk(file_path, data_frame)
        #
        # LOG:
        internal__log_message(
            msgs=f"  Done.",
            prompt_flag=self.params.prompt_flag,
        )


# =============================================================================
