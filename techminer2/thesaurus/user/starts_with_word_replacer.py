# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Starts With Word Replacer
===============================================================================


>>> from techminer2.thesaurus.user import StartsWithWordReplacer
>>> (
...     StartsWithWordReplacer()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_word("BUSINESS")
...     .having_replacement("business")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Word replacing completed successfully: example/thesaurus/demo.the.txt




"""
import re
import sys

import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals import ThesaurusMixin, internal__print_thesaurus_header


class StartsWithWordReplacer(
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

        sys.stderr.write("\nReplacing word in keys")
        sys.stderr.write(f"\n         File : {file_path}")
        sys.stderr.write(f"\n         Word : {word}")
        sys.stderr.write(f"\n  Replacement : {replacement}")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 40:
            truncated_path = "..." + truncated_path[-36:]
        sys.stderr.write("\n")
        sys.stdout.write(f"\nWord replacing completed successfully: {truncated_path}")
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__replace_word(self):
        #
        data_frame = self.data_frame
        replacement = self.params.replacement
        #
        result = []
        #
        if isinstance(self.params.word, str):
            words = [self.params.word]
        else:
            words = self.params.word

        for word in words:

            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + word + "$"), replacement, regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + word + "_"), replacement + "_", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + word + " "), replacement + " ", regex=True
            )

        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()
        self.internal__replace_word()
        self.internal__reduce_keys()
        self.internal__group_values_by_key()
        self.internal__sort_data_frame_by_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

        internal__print_thesaurus_header(self.thesaurus_path)


# =============================================================================
