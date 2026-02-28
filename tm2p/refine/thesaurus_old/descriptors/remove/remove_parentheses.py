"""
Parentheses
===============================================================================


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from tm2p.refine.thesaurus_old.descriptors import InitializeThesaurus, RemoveParentheses

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Remove parentheses
    >>> RemoveParentheses(root_directory="examples/fintech/", ).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Removing parentheses from thesaurus keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      6 removals made successfully
      Removal process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        CLASSIFICATION
          CLASSIFICATION (OF_INFORMATION)
        COMPETITION
          COMPETITION; COMPETITION (ECONOMICS)
        FINANCIAL_TECHNOLOGY
          FINANCIAL_TECHNOLOGIES; FINANCIAL_TECHNOLOGY; FINANCIAL_TECHNOLOGY (FINTECH)
        INTERNET_OF_THING
          INTERNET_OF_THING (IOT); INTERNET_OF_THINGS
        NETWORKS
          NETWORKS; NETWORKS (CIRCUITS)
        PRESSES
          PRESSES (MACHINE_TOOLS)
        A_A_THEORY
          A_A_THEORY
        A_BASIC_RANDOM_SAMPLING_STRATEGY
          A_BASIC_RANDOM_SAMPLING_STRATEGY
    <BLANKLINE>
    <BLANKLINE>


"""

import sys

import pandas as pd  # type: ignore
from colorama import Fore, init
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from tm2p._internals import ParamsMixin
from tm2p.refine.thesaurus_old._internals import ThesaurusMixin

tqdm.pandas()


class RemoveParentheses(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if self.params.colored_stderr:
            filename = str(file_path).rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Removing parentheses from thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):
        sys.stderr.write("  Removal process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__run_at_beining(self):
        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

    # -------------------------------------------------------------------------
    def internal__remove_surrounding_chars(self, left_char, right_char):
        #
        def remove(text):
            if len(text) > 0 and text[0] == left_char and text[-1] == right_char:
                return text[1:-1]
            return text

        self.data_frame["key"] = self.data_frame.key.map(remove)

    # -------------------------------------------------------------------------
    def internal__invert_abbreviation_definitions(self, left_char, right_char):
        #
        # Case:
        # "REGTECH (REGULATORY_TECHNOLOGY)" -> "REGULATORY_TECHNOLOGY (REGTECH)"
        #
        def invert_definitions(text):
            start_idx = text.find(left_char)
            end_idx = text.find(right_char)
            if start_idx == -1 or end_idx == -1:
                text_to_remove = text[start_idx + 1 : end_idx].strip()
                meaning = text[:start_idx].strip()
                if (
                    len(meaning) < len(text_to_remove)
                    and len(text_to_remove.strip()) > 1
                ):
                    return f"{text_to_remove} ({meaning})"
            return text

        self.data_frame["key"] = self.data_frame.key.apply(invert_definitions)

    # -------------------------------------------------------------------------
    def internal__remove_definitions(self, left_char, right_char):
        #
        # Tansforms:
        #
        # "REGULATORY_TECHNOLOGY [REGTECH]" -> "REGULATORY_TECHNOLOGY"
        #
        def remove(text):
            start_idx = text.find(left_char)
            end_idx = text.find(right_char)
            if start_idx != -1 and end_idx != -1:
                text_to_remove = text[start_idx : end_idx + 1]
                text = text.replace(text_to_remove, "").strip()
                text = text.replace("  ", " ").replace("  ", " ").replace("  ", " ")
            return text

        self.data_frame["key"] = self.data_frame.key.apply(remove)

    # -------------------------------------------------------------------------
    def internal__repair_keys(self):
        #
        def repair(text):
            if text[-1] == "_":
                text = text[:-1]
            if text[0] == "_":
                text = text[1:]
            text = (
                text.replace("  ", " ")
                .replace("  ", " ")
                .replace("  ", " ")
                .replace(" ", "_")
            )
            return text

        self.data_frame["key"] = self.data_frame.key.apply(repair)

    # -------------------------------------------------------------------------
    def internal__run_at_ending(self):
        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} removals made successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("concepts.the.txt")

        self._build_user_thesaurus_path()
        self.internal__notify_process_start()
        self._load_thesaurus_as_mapping()
        self._transform_mapping_to_data_frame()
        self.internal__run_at_beining()

        self.internal__remove_surrounding_chars("(", ")")
        self.internal__remove_surrounding_chars("[", "]")

        self.internal__invert_abbreviation_definitions("(", ")")
        self.internal__invert_abbreviation_definitions("[", "]")

        self.internal__remove_definitions("(", ")")
        self.internal__remove_definitions("[", "]")

        self.internal__run_at_ending()

        self.internal__repair_keys()

        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self._sort_data_frame_by_rows_and_key()
        self._write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
        self.internal__print_thesaurus_header_to_stream(n=8, stream=sys.stderr)
