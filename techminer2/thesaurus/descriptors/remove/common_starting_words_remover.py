# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Common Starting Words Remover
===============================================================================


>>> from techminer2.thesaurus.user import CommonStartingWordsRemover
>>> (
...     CommonStartingWordsRemover()
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
Removing common starting words successfully for file: ...thesaurus/demo.the.txt



"""
import re
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class CommonStartingWordsRemover(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path

        sys.stdout.write("\nRemoving common starting words from thesaurus keys")
        sys.stdout.write(f"\n  File : {file_path}")
        sys.stdout.write("\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):
        truncated_file_path = str(self.thesaurus_path)
        if len(truncated_file_path) > 28:
            truncated_file_path = "..." + truncated_file_path[-24:]
        sys.stdout.write(
            f"\nRemoving common starting words successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__remove_common_starting_words_from_keys(self):

        words = internal__load_text_processing_terms("common_starting_words.txt")

        # create regular expressions
        patterns = []

        patterns += [re.compile("^" + w.lower() + " ") for w in words]
        patterns += [re.compile("^" + w.upper() + " ") for w in words]
        patterns += [re.compile("^" + w.upper() + "_") for w in words]
        patterns += [re.compile("^" + w.capitalize() + " ") for w in words]
        patterns += [re.compile("^" + w.title() + " ") for w in words]

        def replace_patterns(text):
            for pattern in patterns:
                text = pattern.sub("", text)
            return text

        tqdm.pandas(desc="  Progress")
        sys.stdout.write("\n")
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__remove_common_starting_words_from_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

        internal__print_thesaurus_header(self.thesaurus_path)
