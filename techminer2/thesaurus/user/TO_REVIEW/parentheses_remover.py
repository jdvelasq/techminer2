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


>>> from techminer2.thesaurus.user import ParenthesesRemover
>>> (
...     ParenthesesRemover()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Removing parentheses successfully for file: example/thesaurus/demo.the.txt



"""
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class ParenthesesRemover(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def notify__process_start(self):

        file_path = self.thesaurus_path

        sys.stderr.write("\nRemoving parentheses from thesaurus keys")
        sys.stderr.write(f"\n  File : {file_path}")
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def notify__process_end(self):
        truncated_file_path = str(self.thesaurus_path)
        if len(truncated_file_path) > 55:
            truncated_file_path = "..." + truncated_file_path[-51:]
        sys.stdout.write(
            f"\nRemoving parentheses successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
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
    def build(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.notify__process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()

        self.internal__remove_surrounding_chars("(", ")")
        self.internal__remove_surrounding_chars("[", "]")

        self.internal__invert_abbreviation_definitions("(", ")")
        self.internal__invert_abbreviation_definitions("[", "]")

        self.internal__remove_definitions("(", ")")
        self.internal__remove_definitions("[", "]")

        self.internal__repair_keys()

        self.internal__group_values_by_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.notify__process_end()

        internal__print_thesaurus_header(self.thesaurus_path)
