# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Hypenated Words Transformer
===============================================================================


>>> from techminer2.thesaurus.user import HyphenatedWordsTransformer
>>> (
...     HyphenatedWordsTransformer()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Transforming hyphenated words completed successfully for file: .../demo.the.txt



"""
import re
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class HyphenatedWordsTransformer(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def notify__process_start(self):

        file_path = self.thesaurus_path

        sys.stderr.write("\nTransforming hyphenated words in thesaurus keys")
        sys.stderr.write(f"\n  File : {file_path}")
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def notify__process_end(self):
        truncated_file_path = str(self.thesaurus_path)
        if len(truncated_file_path) > 17:
            truncated_file_path = "..." + truncated_file_path[-14:]
        sys.stdout.write(
            f"\nTransforming hyphenated words completed successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__transform_hyphenated_words_in_keys(self):

        # replace the word by this hyphenated version
        words = internal__load_text_processing_terms("hyphenated_words.txt")

        patterns = []

        #
        # Words in lower case + spaces
        #
        patterns += [
            (
                re.compile(r"^" + word.lower().replace("_", "") + " "),
                word.lower() + " ",
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r" " + word.lower().replace("_", "") + r"$"),
                " " + word.lower(),
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r"^" + word.lower().replace("_", "") + r"$"),
                word.lower(),
            )
            for word in words
        ]

        #
        # Words in upper case + spaces
        #
        patterns += [
            (
                re.compile(r"^" + word.upper().replace("_", "") + " "),
                word.upper() + " ",
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r" " + word.upper().replace("_", "") + r"$"),
                " " + word.upper(),
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r"^" + word.upper().replace("_", "") + r"$"),
                word.upper(),
            )
            for word in words
        ]

        #
        # Words in upper case + "_"
        #
        patterns += [
            (
                re.compile(r"^" + word.upper().replace("_", "") + "_"),
                word.upper() + "_",
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r"_" + word.upper().replace("_", "") + r"$"),
                "_" + word.upper(),
            )
            for word in words
        ]

        # replace the words
        def f(x):
            for pattern, replacement in patterns:
                x = pattern.sub(replacement, x)
            return x

        tqdm.pandas(desc="  Processing hyphenated words")
        sys.stderr.write("\n")
        self.data_frame["key"] = self.data_frame["key"].progress_apply(f)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def internal__fix_bad_hyphenated_words_in_keys(self):

        # replace the word by this hyphenated version
        words = internal__load_text_processing_terms("non_hypened_words.txt")

        patterns = []

        #
        # Words in lower case + spaces
        #
        patterns += [
            (
                re.compile(r"^" + word.lower() + " "),
                word.lower().replace("_", "") + " ",
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r" " + word.lower() + r"$"),
                " " + word.lower().replace("_", ""),
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r"^" + word.lower() + r"$"),
                word.lower().replace("_", ""),
            )
            for word in words
        ]

        #
        # Words in upper case + spaces
        #
        patterns += [
            (
                re.compile(r"^" + word.upper() + " "),
                word.upper().replace("_", "") + " ",
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r" " + word.upper() + r"$"),
                " " + word.upper().replace("_", ""),
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r"^" + word.upper() + r"$"),
                word.upper().replace("_", ""),
            )
            for word in words
        ]

        #
        # Words in upper case + "_"
        #
        patterns += [
            (
                re.compile(r"^" + word.upper() + "_"),
                word.upper().replace("_", "") + "_",
            )
            for word in words
        ]

        patterns += [
            (
                re.compile(r"_" + word.upper() + r"$"),
                "_" + word.upper().replace("_", ""),
            )
            for word in words
        ]

        # replace the words
        def f(x):
            for pattern, replacement in patterns:
                x = pattern.sub(replacement, x)
            return x

        self.data_frame["key"] = self.data_frame["key"].apply(f)

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.notify__process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()
        #
        self.internal__transform_hyphenated_words_in_keys()
        self.internal__fix_bad_hyphenated_words_in_keys()
        #
        self.internal__group_values_by_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.notify__process_end()

        internal__print_thesaurus_header(self.thesaurus_path)
