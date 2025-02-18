# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key
===============================================================================

## >>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
## >>> from techminer2.thesaurus.user import SortThesaurusByKey
## >>> (
## ...     SortThesaurusByKey()
## ...     # 
## ...     # THESAURUS:
## ...     .with_thesaurus_file("descriptors.the.txt")
## ...     .having_keys_ordered_by("alphabetical")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )
--INFO-- The thesaurus file descriptors.the.txt has been ordered alphabetically.


"""
import sys

from ...internals.log_message import internal__log_message
from ...internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)


class SortThesaurusByKey(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def get_thesaurus_sorted_keys(self, th_dict):
        #
        if self.params.keys_order_by == "alphabetical":
            return sorted(th_dict.keys(), reverse=False)
        #
        if self.params.keys_order_by == "key_length":
            return sorted(th_dict.keys(), key=lambda x: (len(x), x), reverse=False)
        #
        if self.params.keys_order_by == "word_length":
            return sorted(
                th_dict.keys(),
                key=lambda x: (max(len(y) for y in x.split("_")), x),
                reverse=True,
            )
        #
        return th_dict.keys()

    # -------------------------------------------------------------------------
    def save_sorted_thesaurus_on_disk(self, file_path, th_dict, sorted_keys):
        with open(file_path, "w", encoding="utf-8") as file:
            for key in sorted_keys:
                file.write(key + "\n")
                for item in sorted(set(th_dict[key])):
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)

        order_by = {
            "alphabetical": "alphabetically",
            "key_length": "by key length",
            "word_length": "by word length",
        }[self.params.keys_order_by]

        internal__log_message(
            msgs=[
                f"Sorting thesaurus {order_by}.",
                f"      Thesaurus file: '{file_path}'",
            ],
            prompt_flag=self.params.prompt_flag,
        )

        th_dict = internal__load_thesaurus_as_mapping(file_path)
        sorted_keys = self.get_thesaurus_sorted_keys(th_dict)
        self.save_sorted_thesaurus_on_disk(file_path, th_dict, sorted_keys)

        internal__log_message(
            msgs="  Done.",
            prompt_flag=-1,
        )


# =============================================================================
