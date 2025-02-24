# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Clean Thesaurus
===============================================================================

>>> from techminer2.thesaurus.descriptors import CleanupThesaurus
>>> (
...     CleanupThesaurus()
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus cleanup completed successfully for file: ...aurus/descriptors.the.txt



"""
import sys

import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals import (
    internal__apply_porter_stemmer,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
)

# -------------------------------------------------------------------------
PARTICLES = [
    "_AIDED_",
    "_ASSISTED_",
    "_AND_",
    "_AND_THE_",
    "_APPLIED_TO_",
    "_AT_",
    "_BASED_",
    "_FOR_",
    "_IN_",
    "_LIKE_",
    "_OF_",
    "_OF_THE_",
    "_OF_USING_",
    "_ON_",
    "_S_",
    "_SIZED_",
    "_TO_",
    "_UNDER_",
    "_USING_",
]


class CleanupThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def generate_user_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def load_thesaurus_as_data_frame(self):
        sys.stderr.write(f"  Loading {self.file_path} thesaurus file as data frame.\n")
        sys.stderr.flush()
        self.data_frame = internal__load_thesaurus_as_data_frame(self.file_path)

    # -------------------------------------------------------------------------
    def create_fingerprint_column_in_data_frame(self):
        sys.stderr.write(f"  Creating fingerprint column.\n")
        sys.stderr.flush()
        self.data_frame["fingerprint"] = (
            self.data_frame["key"].str.lower().str.replace("_", " ").str.strip()
        )

    # -------------------------------------------------------------------------
    def remove_particles_from_fingerprints(self):
        sys.stderr.write(f"  Removing text particles from fingerprints.\n")
        sys.stderr.flush()
        for particle in PARTICLES:
            particle = particle.replace("_", " ").lower()
            self.data_frame["fingerprint"] = self.data_frame["fingerprint"].str.replace(
                f" {particle} ",
                " ",
                regex=False,
            )

    # -------------------------------------------------------------------------
    def apply_porter_stemmer_to_fingerprint(self):
        sys.stderr.write(f"  Applying Porter stemmer to fingerprints.\n")
        sys.stderr.flush()
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].str.split(" ")
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].map(
            lambda x: [internal__apply_porter_stemmer(z) for z in x]
        )
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].map(sorted)
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].str.join("_")

    # -------------------------------------------------------------------------
    def compute_n_terms_by_key(self):
        sys.stderr.write(f"  Counting terms by fingerprint.\n")
        sys.stderr.flush()
        self.data_frame["n_terms"] = self.data_frame.groupby(
            ["fingerprint", "key"]
        ).transform("count")
        self.data_frame = self.data_frame.sort_values(
            ["fingerprint", "n_terms", "key"], ascending=True
        )

    # -------------------------------------------------------------------------
    def replace_fingerprint_by_key(self):
        #
        # replace the fingerprint for the most frequent key (i.e., the key
        # with the highest number of terms)
        #
        sys.stderr.write(f"  Generating new thesaurus keys.\n")
        sys.stderr.flush()
        repl = {row.fingerprint: row.key for _, row in self.data_frame.iterrows()}
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].map(repl)

    # -------------------------------------------------------------------------
    def save_thesaurus_to_disk(self):

        sys.stderr.write(f"  Writing cleaned thesaurus to disk.\n")
        sys.stderr.flush()

        data_frame = self.data_frame[["fingerprint", "value"]]
        data_frame = data_frame.drop_duplicates()
        data_frame = data_frame.sort_values(["fingerprint", "value"], ascending=True)
        data_frame = data_frame.groupby("fingerprint").agg(list)

        with open(self.file_path, "w", encoding="utf-8") as file:
            for key, row in data_frame.iterrows():
                file.write(key + "\n")
                for value in row.value:
                    file.write("    " + value + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        sys.stderr.write("Cleanup Descriptors Thesaurus.\n")
        sys.stderr.flush()
        self.params.update(thesaurus_file="descriptors.the.txt")
        self.generate_user_thesaurus_file_path()
        self.load_thesaurus_as_data_frame()
        self.create_fingerprint_column_in_data_frame()
        self.apply_porter_stemmer_to_fingerprint()
        self.compute_n_terms_by_key()
        self.replace_fingerprint_by_key()
        self.save_thesaurus_to_disk()

        truncated_file_path = str(self.file_path)
        if len(truncated_file_path) > 29:
            truncated_file_path = "..." + truncated_file_path[-25:]
        sys.stdout.write(
            f"\nThesaurus cleanup completed successfully for file: {truncated_file_path}\n"
        )
        sys.stdout.flush()


# =============================================================================
