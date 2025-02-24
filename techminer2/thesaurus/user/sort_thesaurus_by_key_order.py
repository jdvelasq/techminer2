# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Order
===============================================================================

>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.user import SortThesaurusByKeyOrder
>>> (
...     SortThesaurusByKeyOrder()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting completed successfully for file: ...aurus/descriptors.the.txt

>>> from techminer2.thesaurus.user import SortThesaurusByKeyOrder
>>> (
...     SortThesaurusByKeyOrder()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_ordered_by("key_length")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting completed successfully for file: ...aurus/descriptors.the.txt



>>> from techminer2.thesaurus.user import SortThesaurusByKeyOrder
>>> (
...     SortThesaurusByKeyOrder()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_ordered_by("word_length")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting completed successfully for file: ...aurus/descriptors.the.txt
                   
"""
import sys

from ..._internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)


class SortThesaurusByKeyOrder(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_set_order_by(self):
        self.order_by = {
            "alphabetical": "alphabetically",
            "key_length": "by key length",
            "word_length": "by word length",
        }[self.params.keys_order_by]

    # -------------------------------------------------------------------------
    def step_03_print_info_header(self):
        order_by = self.order_by
        sys.stderr.write(f"\nSorting thesaurus {order_by}")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def step_04_load_thesaurus_as_mapping(self):
        file_path = self.file_path

        sys.stderr.write(f"\n  File : {file_path}")
        sys.stderr.flush()
        self.th_dict = internal__load_thesaurus_as_mapping(self.file_path)

    # -------------------------------------------------------------------------
    def step_05_get_thesaurus_sorted_keys(self):
        #
        if self.params.keys_order_by == "alphabetical":
            self.sorted_keys = sorted(self.th_dict.keys(), reverse=False)
            return
        #
        if self.params.keys_order_by == "key_length":
            self.sorted_keys = sorted(
                self.th_dict.keys(), key=lambda x: (len(x), x), reverse=False
            )
            return
        #
        if self.params.keys_order_by == "word_length":
            self.sorted_keys = sorted(
                self.th_dict.keys(),
                key=lambda x: (max(len(y) for y in x.split("_")), x),
                reverse=True,
            )
            return
        #
        self.sorted_keys = self.th_dict.keys()

    # -------------------------------------------------------------------------
    def step_06_save_sorted_thesaurus_on_disk(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for key in self.sorted_keys:
                file.write(key + "\n")
                for item in sorted(set(self.th_dict[key])):
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def step_07_print_info_tail(self):
        sys.stderr.write("\n")
        sys.stderr.flush()
        internal__print_thesaurus_header(file_path=self.file_path)

        truncated_file_path = str(self.file_path)
        if len(truncated_file_path) > 29:
            truncated_file_path = "..." + truncated_file_path[-25:]
        sys.stdout.write(
            f"\nThesaurus sorting completed successfully for file: {truncated_file_path}\n"
        )
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.step_01_get_thesaurus_file_path()
        self.step_02_set_order_by()
        self.step_03_print_info_header()
        self.step_04_load_thesaurus_as_mapping()
        self.step_05_get_thesaurus_sorted_keys()
        self.step_06_save_sorted_thesaurus_on_disk()
        self.step_07_print_info_tail()


# =============================================================================
