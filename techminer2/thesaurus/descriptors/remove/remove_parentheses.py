# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Parentheses Remover
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, RemoveParentheses

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Remove parentheses
    >>> RemoveParentheses(root_directory="example/").run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Removing parentheses from thesaurus keys
    <BLANKLINE>
      File : example/thesaurus/descriptors.the.txt
      7 removals made successfully
      Parentheses removal completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        CACIOPPO
          CACIOPPO_[1]
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
        A_A_)_THEORY
          A_A_)_THEORY
    <BLANKLINE>
    <BLANKLINE>


"""
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

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

        file_path = self.thesaurus_path

        sys.stderr.write("Removing parentheses from thesaurus keys\n")
        sys.stderr.write(f"\n  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):
        sys.stderr.write("  Parentheses removal completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

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

        self.with_thesaurus_file("descriptors.the.txt")

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
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
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
