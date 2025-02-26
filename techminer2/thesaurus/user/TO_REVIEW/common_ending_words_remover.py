# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Common Ending Words Remover
===============================================================================


>>> from techminer2.thesaurus.user import CommonEndingWordsRemover
>>> (
...     CommonEndingWordsRemover()
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
Removing common ending words successfully for file: ...e/thesaurus/demo.the.txt



"""
import re
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals import ParamsMixin
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class CommonEndingWordsRemover(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def notify__process_start(self):

        file_path = self.thesaurus_path

        sys.stderr.write("\nRemoving common ending words from thesaurus keys")
        sys.stderr.write(f"\n  File : {file_path}")
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def notify__process_end(self):
        truncated_file_path = str(self.thesaurus_path)
        if len(truncated_file_path) > 30:
            truncated_file_path = "..." + truncated_file_path[-26:]
        sys.stdout.write(
            f"\nRemoving common ending words successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__remove_common_ending_words_from_keys(self):

        words = internal__load_text_processing_terms("common_ending_words.txt")

        # create regular expressions
        patterns = []

        patterns += [re.compile(" " + w.lower() + "$") for w in words]
        patterns += [re.compile(" " + w.upper() + "$") for w in words]
        patterns += [re.compile("_" + w.upper() + "$") for w in words]
        patterns += [re.compile(" " + w.capitalize() + "$") for w in words]
        patterns += [re.compile(" " + w.title() + "$") for w in words]

        def replace_patterns(text):
            for pattern in patterns:
                text = pattern.sub("", text)
            return text

        tqdm.pandas(desc="  Progress")
        sys.stderr.write("\n")
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.notify__process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()
        self.internal__remove_common_ending_words_from_keys()
        self.internal__group_values_by_key()
        self.internal__sort_data_frame_by_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.notify__process_end()

        internal__print_thesaurus_header(self.thesaurus_path)
