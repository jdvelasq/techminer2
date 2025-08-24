# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Spell Check
===============================================================================



Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus, SpellCheck

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()


    >>> # Creates, configures, an run the spell checker
    >>> (
    ...     SpellCheck(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_maximum_occurrence(3)
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Spell checking thesaurus keys...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Potential misspelled words (59):
    <BLANKLINE>
        - affordance
        - affordances
        - backoffice
        - behavioural
        - bitcoin
        - blockchain
        - burdencapital
        - centricity
        - crowdfunding
        - crowdinvesting
        ...
    <BLANKLINE>
      Matching keys found : 71
      Spell checking process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/demo.the.txt
    <BLANKLINE>
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_BLOCKCHAIN_IMPLEMENTATION_STUDY
          A_BLOCKCHAIN_IMPLEMENTATION_STUDY
        A_HYBRID_MCDM_MODEL
          A_HYBRID_MCDM_MODEL
        A_MULTI_LEVEL_ANALYSIS
          A_MULTI_LEVEL_ANALYSIS
        A_WIDE_RANGING_RECONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        A_YOUTH_MICROLOAN_STARTUP
          A_YOUTH_MICROLOAN_STARTUP
        AFFORDANCE_ACTUALIZATION
          AFFORDANCE_ACTUALIZATION
        AFFORDANCES
          AFFORDANCES
    <BLANKLINE>
    <BLANKLINE>



    >>> # Restaring the stderr
    >>> sys.stderr = StringIO()

    >>> # Creates, configures, an run the spell checker
    >>> SpellCheck(
    ...     thesaurus_file="demo.the.txt",
    ...     maximum_occurrence=3,
    ...     root_directory="examples/fintech/",
    ...     use_colorama=False,
    ... ).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +SKIP
    Spell checking thesaurus keys...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Potential misspelled words (59):
    <BLANKLINE>
        - affordance
        - affordances
        - backoffice
        - behavioural
        - bitcoin
        - blockchain
        - burdencapital
        - centricity
        - crowdfunding
        - crowdinvesting
        ...
    <BLANKLINE>
      Matching keys found : 71
      Spell checking process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/demo.the.txt
    <BLANKLINE>
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_BLOCKCHAIN_IMPLEMENTATION_STUDY
          A_BLOCKCHAIN_IMPLEMENTATION_STUDY
        A_HYBRID_MCDM_MODEL
          A_HYBRID_MCDM_MODEL
        A_MULTI_LEVEL_ANALYSIS
          A_MULTI_LEVEL_ANALYSIS
        A_WIDE_RANGING_RECONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        A_YOUTH_MICROLOAN_STARTUP
          A_YOUTH_MICROLOAN_STARTUP
        AFFORDANCE_ACTUALIZATION
          AFFORDANCE_ACTUALIZATION
        AFFORDANCES
          AFFORDANCES
    <BLANKLINE>
    <BLANKLINE>



"""
import sys

import pandas as pd  # type: ignore
from colorama import Fore, init
from spellchecker import SpellChecker as ExternalSpellChecker

from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import (
    ThesaurusMixin,
    internal__print_thesaurus_header,
)


class SpellCheck(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if len(file_path) > 72:
            file_path = "..." + file_path[-68:]

        if self.params.use_colorama:
            filename = str(file_path).rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Spell checking thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Spell checking process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path, use_colorama=self.params.use_colorama
        )

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__extract_words_from_mapping(self):

        terms = list(self.mapping.keys())
        terms = [t.replace("_", " ") for t in terms]
        words = [word for term in terms for word in term.split(" ")]
        words = pd.Series(words).value_counts()
        words = words[words <= self.params.maximum_occurrence]
        words = [word for word in words.index if word.isalpha()]
        self.words = words

    # -------------------------------------------------------------------------
    def internal__search_mispelled_words(self):

        spell = ExternalSpellChecker()
        misspelled_words = spell.unknown(self.words)
        misspelled_words = sorted(misspelled_words)
        self.misspelled_words = misspelled_words

    # -------------------------------------------------------------------------
    def internal__print_mispelled_words_to_sysout(self):

        if len(self.misspelled_words) == 0:
            sys.stderr.write("  No misspelled words found\n")
            sys.stderr.flush()
            return

        misspelled_words = self.misspelled_words[:10]
        for i_word, word in enumerate(misspelled_words):
            if i_word == 0:
                sys.stderr.write(
                    f"  Potential misspelled words ({len(self.misspelled_words)}):\n\n"
                )
            sys.stderr.write(f"    - {word}\n")
        if len(misspelled_words) == 10:
            sys.stderr.write("    ...\n\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__select_data_frame_rows(self):

        self.data_frame["__row_selected__"] = False

        self.data_frame["fingerprint"] = self.data_frame["key"].copy()
        self.data_frame["fingerprint"] = (
            self.data_frame["fingerprint"]
            .str.lower()
            .str.replace("_", " ")
            .str.split(" ")
        )

        for word in self.misspelled_words:
            self.data_frame.loc[
                self.data_frame.fingerprint.str.contains(word, regex=False),
                "__row_selected__",
            ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  Matching keys found : {n_matches}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__extract_words_from_mapping()
        self.internal__search_mispelled_words()
        self.internal__print_mispelled_words_to_sysout()
        self.internal__select_data_frame_rows()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================
