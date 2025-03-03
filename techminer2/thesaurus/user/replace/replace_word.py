# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Starts With Word 
===============================================================================

>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors", 
...     root_directory="example/", quiet=True).run()

>>> from techminer2.thesaurus.user import ReplaceWord
>>> (
...     ReplaceWord()
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
Replacing word in keys
         File : example/thesaurus/demo.the.txt
         Word : None
  Replacement : business
  19 replacements made successfully
  Word replacing completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
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
    FUNDAMENTALLY_NEW_business_OPPORTUNITIES
      FUNDAMENTALLY_NEW_BUSINESS_OPPORTUNITIES
<BLANKLINE>


"""
import re
import sys

import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class ReplaceWord(
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

        sys.stdout.write("Replacing word in keys\n")
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

            # complete word:
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + word + "$"), replacement, regex=True
            )

            # starting word:
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + word + "_"), replacement + "_", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + word + " "), replacement + " ", regex=True
            )

            # ending word:
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("_" + word + "$"), "_" + replacement, regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile(" " + word + "$"), " " + replacement, regex=True
            )

            # middle word:
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("_" + word + "_"), "_" + replacement + "_", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile(" " + word + "_"), " " + replacement + "_", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("_" + word + " "), "_" + replacement + " ", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile(" " + word + " "), " " + replacement + " ", regex=True
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
