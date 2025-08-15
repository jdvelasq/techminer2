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
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, ReplaceHyphenatedWords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = (
    ...     ReplaceHyphenatedWords(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Replacing hyphenated words in thesaurus keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      33 hypenated words transformed successfully
      Replacement process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_FINTECH_ECO_SYSTEM
          A_FINTECH_ECOSYSTEM
        A_WIDE_RANGING_RE_CONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        AGRI_BUSINESS
          AGRIBUSINESS
        BACK_OFFICE_FUNCTIONS
          BACKOFFICE_FUNCTIONS
        BLOCK_CHAIN
          BLOCKCHAIN
        BLOCK_CHAIN_IMPLEMENTATION
          BLOCKCHAIN_IMPLEMENTATION
        BROADER_AGRICULTURE_ECO_SYSTEM
          BROADER_AGRICULTURE_ECOSYSTEM
        COMPLEX_GENERATES_DIGITAL_ECO_SYSTEMS
          COMPLEX_GENERATES_DIGITAL_ECOSYSTEMS
    <BLANKLINE>
    <BLANKLINE>


"""
import re
import sys

import pandas as pd  # type: ignore
from colorama import Fore
from colorama import init
from techminer2._internals.mixins import ParamsMixin
from techminer2.package_data.text_processing import internal__load_text_processing_terms
from techminer2.thesaurus._internals import internal__print_thesaurus_header
from techminer2.thesaurus._internals import ThesaurusMixin
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

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

        file_path = str(self.thesaurus_path)

        if self.params.use_colorama:
            filename = str(file_path).split("/")[-1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Replacing hyphenated words in thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):
        sys.stderr.write(f"  Replacement process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path, use_colorama=self.params.use_colorama
        )

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
        words = internal__load_text_processing_terms("non_hyphenated_words.txt")

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
