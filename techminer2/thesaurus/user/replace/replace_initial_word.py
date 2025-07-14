# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Initial Word
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus, ReplaceInitialWord

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()

    >>> # Creates, configures, an run the replacer
    >>> replacer = (
    ...     ReplaceInitialWord(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_word("BUSINESS")
    ...     .having_replacement("business")
    ...     .where_root_directory_is("example/")
    ... )
    >>> replacer.run()

    >>> # Capture and print stderr output to test the algorithm using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Replacing initial word in keys...
             File : example/data/thesaurus/demo.the.txt
             Word : BUSINESS
      Replacement : business
      8 replacements made successfully
      Replacement process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/demo.the.txt
    <BLANKLINE>
        business
          BUSINESS; BUSINESSES
        business_DEVELOPMENT
          BUSINESS_DEVELOPMENT
        business_GERMANY
          BUSINESS_GERMANY
        business_INFRASTRUCTURE
          BUSINESS_INFRASTRUCTURE; BUSINESS_INFRASTRUCTURES
        business_MODEL
          BUSINESS_MODEL; BUSINESS_MODELS
        business_OPPORTUNITIES
          BUSINESS_OPPORTUNITIES
        business_PROCESS
          BUSINESS_PROCESS
        business_TO_CONSUMERS_MODELS
          BUSINESS_TO_CONSUMERS_MODELS
    <BLANKLINE>
    <BLANKLINE>



"""
import re
import sys

import pandas as pd  # type: ignore
from colorama import Fore, init

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class ReplaceInitialWord(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)
        word = self.params.word
        replacement = self.params.replacement

        if len(file_path) > 40:
            file_path = "..." + file_path[-36:]

        if self.params.use_colorama:
            filename = str(file_path).split("/")[-1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Replacing initial word in keys...\n")
        sys.stderr.write(f"         File : {file_path}\n")
        sys.stderr.write(f"         Word : {word}\n")
        sys.stderr.write(f"  Replacement : {replacement}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Replacement process completed successfully\n\n")
        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path, use_colorama=self.params.use_colorama
        )

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__replace_word(self):
        #
        replacement = self.params.replacement
        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()
        #
        if isinstance(self.params.word, str):
            words = [self.params.word]
        else:
            words = self.params.word

        for word in words:

            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + word + "$"), replacement, regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + word + "_"), replacement + "_", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + word + " "), replacement + " ", regex=True
            )

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} replacements made successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__replace_word()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================
