# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create thesaurus
===============================================================================


>>> from techminer2.thesaurus.user import CreateThesaurus
>>> (
...     CreateThesaurus()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # FIELD:
...     .with_field("descriptors")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )




"""
import re
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ..._internals.mixins import ParamsMixin
from ...database._internals.io import internal__load_records
from ...package_data.text_processing import internal__load_text_processing_terms
from .._internals import (
    ThesaurusMixin,
    internal__generate_system_thesaurus_file_path,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_head,
)

tqdm.pandas()


class CreateThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):

        file_path = self.file_path
        field = self.params.field
        sys.stderr.write("\nINFO  Creating thesaurus from field.")
        sys.stderr.write(f"\n                  Thesaurus file: {file_path}")
        sys.stderr.write(f"\n                    Source field: {field}")
        sys.stderr.write(f"\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def step_03_load_records(self):
        self.records = internal__load_records(params=self.params)

    # -------------------------------------------------------------------------
    def step_04_create_data_frame(self):
        #
        keys = self.records[self.params.field].dropna()
        keys = keys.str.split("; ")
        keys = keys.explode()
        keys = keys.str.strip()
        #
        fingerprints = keys.str.lower()
        fingerprints = fingerprints.str.replace("-", " ")
        fingerprints = fingerprints.str.replace("_", " ")
        #
        counts = keys.value_counts()
        mapping = dict(zip(counts.index.tolist(), counts.values.tolist()))
        #
        data_frame = pd.DataFrame(
            {
                "key": keys,
                "value": keys,
                "fingerprint": fingerprints,
                "occ": [mapping[k] for k in keys],
            }
        )
        #
        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def step_05_transform_british_to_american_spelling(self):
        file_path = internal__generate_system_thesaurus_file_path(
            "language/british2american.the.txt"
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)
        mapping = {k: v[0] for k, v in mapping.items()}
        #
        tqdm.pandas(desc="           Transforming spelling")
        #
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].progress_apply(
            lambda x: " ".join(mapping.get(w, w) for w in x.split(" "))
        )
        #
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_06_singularize_terms(self):
        tqdm.pandas(desc="             Singularizing terms")
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].progress_apply(
            lambda x: " ".join(Word(w).singularize() for w in x.split())
        )
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_07_remove_technical_stopwords(self):
        tqdm.pandas(desc="              Removing stopwords")
        stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].progress_apply(
            lambda x: " ".join([word for word in x.split() if word not in stopwords])
        )
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_08_transform_hypened_words(self):
        #
        def f(x):
            for pattern, replacement in patterns:
                x = pattern.sub(replacement, x)
            return x

        #
        hypened_words = internal__load_text_processing_terms("hypened_words.txt")
        hypened_words = [word.lower() for word in hypened_words]
        patterns = [
            (re.compile(r"\b" + word.replace("_", "") + r"\b"), word.replace("_", " "))
            for word in hypened_words
        ]
        #
        tqdm.pandas(desc="        Processing hypened words")
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].progress_apply(
            f
        )
        tqdm.pandas(desc=None)
        #

    # -------------------------------------------------------------------------
    def step_09_sort_fingerprint_words(self):
        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].apply(
            lambda x: " ".join(sorted(x.split(" ")))
        )

    # -------------------------------------------------------------------------
    def step_10_generate_fingerprint2value_mapping(self):
        self.data_frame = self.data_frame.sort_values(
            by=["fingerprint", "occ", "value"], ascending=[True, False, True]
        )
        self.data_frame = self.data_frame.drop_duplicates(subset=["fingerprint"])
        mapping = self.data_frame.set_index("fingerprint")["value"].to_dict()
        self.mapping = mapping

    # -------------------------------------------------------------------------
    def step_11_apply_mapping(self):
        tqdm.pandas(desc="                 Generating keys")
        self.data_frame["key"] = self.data_frame["fingerprint"].progress_apply(
            lambda x: self.mapping.get(x, x)
        )
        tqdm.pandas(desc=None)
        self.data_frame = self.data_frame[["key", "value"]]

    # -------------------------------------------------------------------------
    def step_12_save_thesaurus(
        self,
    ):
        self.data_frame = self.data_frame.groupby("key").agg({"value": list})
        with open(self.file_path, "w", encoding="utf-8") as file:
            for _, row in self.data_frame.iterrows():
                file.write(row.name + "\n")
                for value in row["value"]:
                    file.write(f"  {value}\n")

    # -------------------------------------------------------------------------
    def step_13_print_info_tail(self):
        sys.stderr.write("\n        Done.")
        internal__print_thesaurus_head(file_path=self.file_path)
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_records()
        self.step_04_create_data_frame()
        self.step_05_transform_british_to_american_spelling()
        self.step_06_singularize_terms()
        self.step_07_remove_technical_stopwords()
        self.step_08_transform_hypened_words()
        self.step_09_sort_fingerprint_words()
        self.step_10_generate_fingerprint2value_mapping()
        self.step_11_apply_mapping()
        self.step_12_save_thesaurus()
        self.step_13_print_info_tail()
