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
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, ReplaceAbbreviations

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Copy the acronyms file
    >>> shutil.copy("examples/fintech/acronyms.the.txt", "examples/fintech/data/thesaurus/acronyms.the.txt")
    'examples/fintech/data/thesaurus/acronyms.the.txt'

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = ReplaceAbbreviations(root_directory="examples/fintech/", tqdm_disable=True, use_colorama=False)

    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Replacing acronyms in keys...
      Thesaurus : ...h/data/thesaurus/descriptors.the.txt
       Acronyms : ...data/thesaurus/acronyms.the.txt
      120 replacements made successfully
      Replacement process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_EUROPEAN_OR_NATIONAL_FINANCIAL_TECHNOLOGY_MARKET
          A_EUROPEAN_OR_NATIONAL_FINTECH_MARKET
        A_FINANCIAL_TECHNOLOGY_COMPANY
          A_FINTECH_COMPANY
        A_FINANCIAL_TECHNOLOGY_ECOSYSTEM
          A_FINTECH_ECOSYSTEM
        A_HYBRID_MULTI_CRITERIA_DECISION_MAKING_METHOD_MODEL
          A_HYBRID_MCDM_MODEL
        A_NEW_FINANCIAL_TECHNOLOGY_INNOVATION_MAPPING_APPROACH
          A_NEW_FINTECH_INNOVATION_MAPPING_APPROACH
        A_THEORETICAL_DATA_DRIVEN_FINANCIAL_TECHNOLOGY_FRAMEWORK
          A_THEORETICAL_DATA_DRIVEN_FINTECH_FRAMEWORK
        ACTIVE_FINANCIAL_TECHNOLOGY_SOLUTIONS
          ACTIVE_FINTECH_SOLUTIONS
        ACTOR_NETWORK_THEORY
          ACTOR_NETWORK_THEORY; ANT
    <BLANKLINE>
    <BLANKLINE>



"""
import re
import sys

from colorama import Fore
from colorama import init
from techminer2._internals.mixins import Params
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import internal__generate_user_thesaurus_file_path
from techminer2.thesaurus._internals import internal__load_thesaurus_as_data_frame
from techminer2.thesaurus._internals import internal__load_thesaurus_as_mapping
from techminer2.thesaurus._internals import internal__print_thesaurus_header
from techminer2.thesaurus._internals import ThesaurusMixin
from tqdm import tqdm  # type: ignore


class ReplaceAbbreviations(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if len(file_path) > 40:
            file_path = "..." + file_path[-36:]

        if self.params.use_colorama:
            filename = str(file_path).split("/")[-1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        acronyms_path = str(self.acronyms_path)
        if len(acronyms_path) > 40:
            acronyms_path = "..." + acronyms_path[-36:]

        if self.params.use_colorama:
            filename = str(acronyms_path).split("/")[-1]
            acronyms_path = acronyms_path.replace(filename, f"{Fore.RESET}{filename}")
            acronyms_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Replacing acronyms in keys...\n")
        sys.stderr.write(f"  Thesaurus : {file_path}\n")
        sys.stderr.write(f"   Acronyms : {acronyms_path}\n")
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
            .update(thesaurus_file="acronyms.the.txt")
        )

        self.acronyms_path = internal__generate_user_thesaurus_file_path(params=params)

    # -------------------------------------------------------------------------
    def internal__load_descriptor_thesaurus_as_data_frame(self):
        self.data_frame = internal__load_thesaurus_as_data_frame(self.thesaurus_path)

    # -------------------------------------------------------------------------
    def internal__load_acronyms_thesaurus_as_mapping(self):
        self.mapping = internal__load_thesaurus_as_mapping(self.acronyms_path)

    # -------------------------------------------------------------------------
    def internal__replace_acronyms(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        for abbr, value in tqdm(
            self.mapping.items(),
            desc="       Progress ",
            disable=self.params.tqdm_disable,
            ncols=80,
        ):
            #
            # Replace acronyms in descriptor keys
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
        self.internal__load_acronyms_thesaurus_as_mapping()
        self.internal__replace_acronyms()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
