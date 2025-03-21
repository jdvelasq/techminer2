# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace hyphenated words
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, ReplaceHyphenatedWords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = (
    ...     ReplaceHyphenatedWords(tqdm_disable=True)
    ...     .where_root_directory_is("example/")
    ... )
    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Transforming hyphenated words in thesaurus keys
      File : example/thesaurus/descriptors.the.txt
      51 hypenated words transformed successfully
      Hyphenated words transformation completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_FINTECH_ECO_SYSTEM
          A_FINTECH_ECOSYSTEM
        A_WIDE_RANGING_RE_CONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        AGRI_BUSINESS
          AGRIBUSINESS
        AGRO_INDUSTRY
          AGROINDUSTRY
        BACK_OFFICE_FUNCTIONS
          BACKOFFICE_FUNCTIONS
        BLOCK_CHAIN
          BLOCKCHAIN; BLOCKCHAINS
        BLOCK_CHAIN_AND_FINTECH_INNOVATIONS
          BLOCKCHAIN_AND_FINTECH_INNOVATIONS
        BLOCK_CHAIN_ENABLES
          BLOCKCHAIN_ENABLES
    <BLANKLINE>
    <BLANKLINE>

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


class ReplaceHyphenatedWords(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path

        sys.stderr.write("Transforming hyphenated words in thesaurus keys\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):
        sys.stderr.write(
            f"  Hyphenated words transformation completed successfully\n\n"
        )
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__transform_hyphenated_words_in_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

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

        tqdm.pandas(
            desc="  Processing hyphenated words ",
            disable=self.params.tqdm_disable,
            ncols=80,
        )
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

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} hypenated words transformed successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        #
        self.internal__transform_hyphenated_words_in_keys()
        self.internal__fix_bad_hyphenated_words_in_keys()
        #
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
