# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Key Order Sorter
===============================================================================

>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.user import KeyOrderSorter
>>> (
...     KeyOrderSorter()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting successfully for file: example/thesaurus/demo.the.txt

>>> from techminer2.thesaurus.user import KeyOrderSorter
>>> (
...     KeyOrderSorter()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_keys_ordered_by("key_length")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting successfully for file: example/thesaurus/demo.the.txt



>>> from techminer2.thesaurus.user import KeyOrderSorter
>>> (
...     KeyOrderSorter()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_keys_ordered_by("word_length")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting successfully for file: example/thesaurus/demo.the.txt
                   
"""
import sys

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class KeyOrderSorter(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def notify__process_start(self):

        file_path = self.thesaurus_path

        self.order_by = {
            "alphabetical": "alphabetically",
            "key_length": "by key length",
            "word_length": "by word length",
        }[self.params.keys_order_by]
        order_by = self.order_by

        sys.stderr.write(f"\nSorting thesaurus {order_by}")
        sys.stderr.write(f"\n  File : {file_path}")
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def notify__process_end(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 55:
            truncated_path = "..." + truncated_path[-51:]
        sys.stdout.write(f"\nThesaurus sorting successfully for file: {truncated_path}")
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__sort_keys(self):
        #
        if self.params.keys_order_by == "alphabetical":
            self.sorted_keys = sorted(self.mapping.keys(), reverse=False)
            return
        #
        if self.params.keys_order_by == "key_length":
            self.sorted_keys = sorted(
                self.mapping.keys(), key=lambda x: (len(x), x), reverse=False
            )
            return
        #
        if self.params.keys_order_by == "word_length":
            self.sorted_keys = sorted(
                self.mapping.keys(),
                key=lambda x: (max(len(y) for y in x.split("_")), x),
                reverse=True,
            )
            return
        #
        self.sorted_keys = self.mapping.keys()

    # -------------------------------------------------------------------------
    def internal__write_thesaurus_to_disk(self):
        with open(self.thesaurus_path, "w", encoding="utf-8") as file:
            for key in self.sorted_keys:
                file.write(key + "\n")
                for item in sorted(set(self.mapping[key].split("; "))):
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.notify__process_start()
        self.internal__load_thesaurus_as_mapping()
        #
        self.internal__sort_keys()
        self.internal__write_thesaurus_to_disk()
        #
        self.notify__process_end()

        internal__print_thesaurus_header(self.thesaurus_path)


# =============================================================================
