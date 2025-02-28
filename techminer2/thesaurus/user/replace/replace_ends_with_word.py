# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Ends With Word 
===============================================================================

>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="descriptors", 
...     root_directory="example/", quiet=True).run()

>>> from techminer2.thesaurus.user import ReplaceEndsWithWord
>>> (
...     ReplaceEndsWithWord()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_word("BUSINESS")
...     .having_replacement("business")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 
Replacing ending word in keys
         File : example/thesaurus/demo.the.txt
         Word : None
  Replacement : business
  2 replacements made successfully
  Word replacing completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
<BLANKLINE>
    business
      BUSINESS; BUSINESSES
    THE_BANKING_business
      THE_BANKING_BUSINESS
    A_A_)_THEORY
      A_A_)_THEORY
    A_A_THEORY
      A_A_THEORY
    A_BASIC_RANDOM_SAMPLING_STRATEGY
      A_BASIC_RANDOM_SAMPLING_STRATEGY
    A_BEHAVIOURAL_PERSPECTIVE
      A_BEHAVIOURAL_PERSPECTIVE
    A_BETTER_UNDERSTANDING
      A_BETTER_UNDERSTANDING
    A_BLOCKCHAIN_IMPLEMENTATION_STUDY
      A_BLOCKCHAIN_IMPLEMENTATION_STUDY
<BLANKLINE>




"""
import re
import sys

import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class ReplaceEndsWithWord(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)
        word = self.params.pattern
        replacement = self.params.replacement

        if len(file_path) > 40:
            file_path = "..." + file_path[-36:]

        sys.stdout.write("Replacing ending word in keys\n")
        sys.stdout.write(f"         File : {file_path}\n")
        sys.stdout.write(f"         Word : {word}\n")
        sys.stdout.write(f"  Replacement : {replacement}\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stdout.write("  Word replacing completed successfully\n\n")
        internal__print_thesaurus_header(self.thesaurus_path)

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
                re.compile("_" + word + "$"), "_" + replacement, regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile(" " + word + "$"), " " + replacement, regex=True
            )

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stdout.write(f"  {n_matches} replacements made successfully\n")
        sys.stdout.flush()

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
