# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
British to American Spelling
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import BritishToAmericanSpelling, CreateThesaurus

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()

    >>> # Creates, configures, an run the translator
    >>> translator = (
    ...     BritishToAmericanSpelling(tqdm_disable=True)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("example/")
    ... )
    >>> translator.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Converting British to American English
      File : example/data/thesaurus/demo.the.txt
      13 replacements made successfully
    Translation completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/demo.the.txt
    <BLANKLINE>
        ANALOG_PROCESSES
          ANALOGUE_PROCESSES
        ANALYZE_THE_KEY_FACTORS
          ANALYSE_THE_KEY_FACTORS
        ANALYZE_THE_SYSTEMIC_CHARACTERISTICS
          ANALYSE_THE_SYSTEMIC_CHARACTERISTICS
        ANALYZE_THE_SYSTEMIC_INNOVATION_CHARACTERISTICS
          ANALYSE_THE_SYSTEMIC_INNOVATION_CHARACTERISTICS
        BEHAVIORAL_ECONOMICS
          BEHAVIOURAL_ECONOMICS
        ENTREPRENEURIAL_ENDEAVORS
          ENTREPRENEURIAL_ENDEAVOURS
        FAVOR
          FAVOUR
        HARMONIZE_TECHNOLOGICAL_ADVANCEMENTS
          HARMONISE_TECHNOLOGICAL_ADVANCEMENTS
    <BLANKLINE>
    <BLANKLINE>



"""
import re
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import (
    ThesaurusMixin,
    internal__generate_system_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)

tqdm.pandas()


class BritishToAmericanSpelling(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 72:
            truncated_path = "..." + truncated_path[-68:]
        sys.stderr.write("Converting British to American English\n")
        sys.stderr.write(f"  File : {truncated_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("Translation completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__translate_words_on_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        file_path = internal__generate_system_thesaurus_file_path(
            "language/british2american.the.txt"
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)
        mapping = {k: v[0] for k, v in mapping.items()}

        patterns = []

        for key, value in mapping.items():
            pat = [
                (re.compile(r"^" + key.lower() + " "), value.lower() + " "),
                (re.compile(r" " + key.lower() + r"$"), " " + value.lower()),
                (re.compile(r"^" + key.lower() + r"$"), value.lower()),
                (re.compile(r"^" + key.upper() + " "), value.upper() + " "),
                (re.compile(r" " + key.upper() + r"$"), " " + value.upper()),
                (re.compile(r"^" + key.upper() + r"$"), value.upper()),
                (re.compile(r"^" + key.upper() + "_"), value.upper() + "_"),
                (re.compile(r"_" + key.upper() + r"$"), "_" + value.upper()),
            ]
            patterns.extend(pat)

        # replace the words
        def f(x):
            for pattern, replacement in patterns:
                x = pattern.sub(replacement, x)
            return x

        sys.stderr.flush()
        tqdm.pandas(desc="  Progress ", disable=self.params.tqdm_disable, ncols=80)
        self.data_frame["key"] = self.data_frame["key"].progress_apply(f)
        tqdm.pandas(desc=None)
        sys.stderr.flush()

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} replacements made successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__translate_words_on_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
