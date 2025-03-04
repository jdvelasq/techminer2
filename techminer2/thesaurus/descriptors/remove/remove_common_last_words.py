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

>>> # TEST PREPARATION:
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import RemoveCommonLastWords
>>> RemoveCommonLastWords(root_directory="example/", tqdm_disable=True).run()


>>> # TEST EXECUTION:
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Removing common last words from thesaurus keys
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
<BLANKLINE>
  15 ending words removed successfully
  Common last words removal completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    AGRICULTURE
      AGRICULTURE; AGRICULTURE_PLAYS
    CONTINUANCE_INTENTION
      CONTINUANCE_INTENTION; CONTINUANCE_INTENTIONS; CONTINUANCE_INTENTION_DIFFERS
    DIGITAL_FINANCE
      DIGITAL_FINANCE; DIGITAL_FINANCE_ENCOMPASSES
    ENTREPRENEURIAL
      ENTREPRENEURIAL_ENDEAVOURS
    FINTECHS
      FINTECHS_SYNTHESIZE
    FOUR_SPECIFIC
      FOUR_SPECIFIC_INCREASES
    INNOVATIONS
      INNOVATIONS_EXACERBATE
    LENDINGCLUB_LOANS
      LENDINGCLUB_LOANS_INCREASES
<BLANKLINE>
<BLANKLINE>


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


class RemoveCommonLastWords(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path

        sys.stderr.write("Removing common last words from thesaurus keys\n")
        sys.stderr.write(f"  File : {file_path}\n\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write(f"  Common last words removal completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__remove_common_ending_words_from_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        words = internal__load_text_processing_terms("common_last_words.txt")

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

        tqdm.pandas(desc="  Progress ", disable=self.params.tqdm_disable)
        sys.stderr.write("\n")
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} ending words removed successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__remove_common_ending_words_from_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
