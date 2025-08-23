# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Initial Words
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, RemoveInitialWords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Remove common initial words
    >>> RemoveInitialWords(root_directory="examples/fintech/", tqdm_disable=True, use_colorama=False).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +SKIP
    Removing common initial words from thesaurus keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
      208 common initial words removed successfully
      Removal process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        ACADEMICS
          ACADEMICS; OTHER_ACADEMICS
        ACCESS
          ACCELERATE_ACCESS; ACCESS
        ACHIEVEMENTS
          CONTEMPORARY_ACHIEVEMENTS
        ACTION
          LATE_ACTION
        ACTORS
          ACTORS; HETEROGENEOUS_ACTORS
        ADDITIONAL_COMPONENTS
          FIVE_ADDITIONAL_COMPONENTS
        AFFORDANCES
          AFFORDANCES; THREE_AFFORDANCES
        AGRICULTURE_BUSINESS_PROCESS
          TRANSFORM_AGRICULTURE_BUSINESS_PROCESS
    <BLANKLINE>
    <BLANKLINE>


"""
import re
import sys

import pandas as pd  # type: ignore
from colorama import Fore, init
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2.package_data.text_processing import internal__load_text_processing_terms
from techminer2.thesaurus._internals import (
    ThesaurusMixin,
    internal__print_thesaurus_header,
)

tqdm.pandas()


class RemoveInitialWords(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if self.params.use_colorama:
            filename = str(file_path).rsplit("/", maxsplit=1)
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Removing common initial words from thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write(f"  Removal process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path, use_colorama=self.params.use_colorama
        )

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__remove_initial_words_from_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        words = internal__load_text_processing_terms("common_initial_words.txt")
        known_phrases = internal__load_text_processing_terms("known_noun_phrases.txt")

        # create regular expressions
        patterns = []

        patterns += [re.compile("^" + w.lower() + " ") for w in words]
        patterns += [re.compile("^" + w.upper() + " ") for w in words]
        patterns += [re.compile("^" + w.upper() + "_") for w in words]
        patterns += [re.compile("^" + w.capitalize() + " ") for w in words]
        patterns += [re.compile("^" + w.title() + " ") for w in words]

        def replace_patterns(text):
            if text not in known_phrases:
                for pattern in patterns:
                    text = pattern.sub("", text)
            return text

        tqdm.pandas(
            desc="  Progress ",
            disable=self.params.tqdm_disable,
            ncols=80,
        )
        sys.stderr.write("\n")
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} common initial words removed successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__remove_initial_words_from_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
