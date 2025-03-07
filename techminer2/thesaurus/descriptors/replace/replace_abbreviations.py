# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Abbreviations
===============================================================================

Example:
    >>> import shutil
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, ReplaceAbbreviations

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Copy the abbreviations file
    >>> shutil.copy("example/abbreviations.the.txt", "example/thesaurus/abbreviations.the.txt")
    'example/thesaurus/abbreviations.the.txt'

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = ReplaceAbbreviations(root_directory="example/", tqdm_disable=True)
    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Replacing abbreviations in keys
          Thesaurus : example/thesaurus/descriptors.the.txt
      Abbreviations : example/thesaurus/abbreviations.the.txt
      122 replacements made successfully
      Abbreviations replacement completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_EUROPEAN_OR_NATIONAL_FINANCIAL_TECHNOLOGY_MARKET
          A_EUROPEAN_OR_NATIONAL_FINTECH_MARKET
        A_FINANCIAL_TECHNOLOGY_COMPANY
          A_FINTECH_COMPANY
        A_FINANCIAL_TECHNOLOGY_ECOSYSTEM
          A_FINTECH_ECOSYSTEM
        A_NEW_FINANCIAL_TECHNOLOGY_INNOVATION_MAPPING_APPROACH
          A_NEW_FINTECH_INNOVATION_MAPPING_APPROACH
        A_THEORETICAL_DATA_DRIVEN_FINANCIAL_TECHNOLOGY_FRAMEWORK
          A_THEORETICAL_DATA_DRIVEN_FINTECH_FRAMEWORK
        ACTIVE_FINANCIAL_TECHNOLOGY_SOLUTIONS
          ACTIVE_FINTECH_SOLUTIONS
        ARTIFICIAL_INTELLIGENCE
          AI; ARTIFICIAL_INTELLIGENCE
        BANK_FINANCIAL_TECHNOLOGY_PARTNERSHIP
          BANK_FINTECH_PARTNERSHIP
    <BLANKLINE>
    <BLANKLINE>

"""
import re
import sys

from tqdm import tqdm  # type: ignore

from ...._internals.mixins import Params, ParamsMixin
from ..._internals import (
    ThesaurusMixin,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)


class ReplaceAbbreviations(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        thesaurus_path = str(self.thesaurus_path)
        if len(thesaurus_path) > 40:
            thesaurus_path = "..." + thesaurus_path[-36:]

        abbreviations_path = str(self.abbreviations_path)
        if len(abbreviations_path) > 40:
            abbreviations_path = "..." + abbreviations_path[-36:]

        sys.stderr.write("Replacing abbreviations in keys\n")
        sys.stderr.write(f"      Thesaurus : {thesaurus_path}\n")
        sys.stderr.write(f"  Abbreviations : {abbreviations_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Abbreviations replacement completed successfully\n\n")
        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__get_descriptors_thesaurus_file_path(self):

        params = (
            Params()
            .update(**self.params.__dict__)
            .update(thesaurus_file="descriptors.the.txt")
        )

        self.thesaurus_path = internal__generate_user_thesaurus_file_path(params=params)

    # -------------------------------------------------------------------------
    def internal__get_abbrevaviations_thesaurus_file_path(self):

        params = (
            Params()
            .update(**self.params.__dict__)
            .update(thesaurus_file="abbreviations.the.txt")
        )

        self.abbreviations_path = internal__generate_user_thesaurus_file_path(
            params=params
        )

    # -------------------------------------------------------------------------
    def internal__load_descriptor_thesaurus_as_data_frame(self):
        self.data_frame = internal__load_thesaurus_as_data_frame(self.thesaurus_path)

    # -------------------------------------------------------------------------
    def internal__load_abbreviations_thesaurus_as_mapping(self):
        self.mapping = internal__load_thesaurus_as_mapping(self.abbreviations_path)

    # -------------------------------------------------------------------------
    def internal__replace_abbreviations(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        for abbr, value in tqdm(
            self.mapping.items(),
            desc="  Progress ",
            disable=self.params.tqdm_disable,
        ):
            #
            # Replace abbreviations in descriptor keys
            value = value[0]

            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + abbr + "$"), value, regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + abbr + "_"), value + "_", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("^" + abbr + " "), value + " ", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("_" + abbr + "$"), "_" + value, regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile(" " + abbr + "$"), " " + value, regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("_" + abbr + "_"), "_" + value + "_", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile(" " + abbr + "_"), " " + value + "_", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile("_" + abbr + " "), "_" + value + " ", regex=True
            )
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                re.compile(" " + abbr + " "), " " + value + " ", regex=True
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
        self.internal__get_descriptors_thesaurus_file_path()
        self.internal__get_abbrevaviations_thesaurus_file_path()
        self.internal__notify_process_start()
        self.internal__load_descriptor_thesaurus_as_data_frame()
        self.internal__load_abbreviations_thesaurus_as_mapping()
        self.internal__replace_abbreviations()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
