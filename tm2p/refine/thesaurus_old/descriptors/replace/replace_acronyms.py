"""
Replace Abbreviations
===============================================================================

Smoke tests:
    >>> # Copy the acronyms file
    >>> import shutil
    >>> shutil.copy("examples/fintech/acronyms.the.txt", "examples/fintech/data/thesaurus/acronyms.the.txt")
    'examples/fintech/data/thesaurus/acronyms.the.txt'

    >>> # Create thesaurus
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Redirecting stderr to avoid messages
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the replacer
    >>> from techminer2.refine.thesaurus_old.descriptors import ReplaceAcronyms
    >>> ReplaceAcronyms(
    ...     root_directory="examples/fintech/",
    ...     tqdm_disable=True,
    ...     ,
    ... ).run()

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

from colorama import Fore, init
from tqdm import tqdm  # type: ignore

from tm2p._internals import Params, ParamsMixin
from tm2p.refine.thesaurus_old._internals import (
    ThesaurusMixin,
    internal__get_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
    internal__load_thesaurus_as_mapping,
)


class ReplaceAcronyms(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        # Prepare thesaurus path
        thesaurus_path = str(self.thesaurus_path)

        if len(thesaurus_path) > 40:
            thesaurus_path = "..." + thesaurus_path[-36:]

        if self.params.colored_stderr:
            filename = str(thesaurus_path).rsplit("/", maxsplit=1)[1]
            thesaurus_path = thesaurus_path.replace(filename, f"{Fore.RESET}{filename}")
            thesaurus_path = Fore.LIGHTBLACK_EX + thesaurus_path

        # Prepare acronyms path
        acronyms_path = str(self.acronyms_path)

        if len(acronyms_path) > 40:
            acronyms_path = "..." + acronyms_path[-36:]

        if self.params.colored_stderr:
            filename = str(acronyms_path).rsplit("/", maxsplit=1)[1]
            acronyms_path = acronyms_path.replace(filename, f"{Fore.RESET}{filename}")
            acronyms_path = Fore.LIGHTBLACK_EX + acronyms_path

        sys.stderr.write("Replacing acronyms in keys...\n")
        sys.stderr.write(f"  Thesaurus : {thesaurus_path}\n")
        sys.stderr.write(f"   Acronyms : {acronyms_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Replacement process completed successfully\n\n")

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__get_descriptors_thesaurus_file_path(self):

        params = (
            Params()
            .update(**self.params.__dict__)
            .update(thesaurus_file="concepts.the.txt")
        )

        self.thesaurus_path = internal__get_user_thesaurus_file_path(params=params)

    # -------------------------------------------------------------------------
    def internal__get_acronyms_thesaurus_file_path(self):

        params = (
            Params()
            .update(**self.params.__dict__)
            .update(thesaurus_file="acronyms.the.txt")
        )

        self.acronyms_path = internal__get_user_thesaurus_file_path(params=params)

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
        self.internal__get_acronyms_thesaurus_file_path()
        self.internal__notify_process_start()
        self.internal__load_descriptor_thesaurus_as_data_frame()
        self.internal__load_acronyms_thesaurus_as_mapping()
        self.internal__replace_acronyms()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self._sort_data_frame_by_rows_and_key()
        self._write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
        self.internal__print_thesaurus_header_to_stream(n=8, stream=sys.stderr)
