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
    >>> from techminer2.thesaurus.user import CreateThesaurus, SpellCheck

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()


    >>> # Creates, configures, an run the spell checker
    >>> checker = (
    ...     SpellCheck()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_maximum_occurrence(3)
    ...     .where_root_directory_is("example/")
    ... )
    >>> checker.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Spell checking thesaurus keys
      File : example/data/thesaurus/demo.the.txt
      Potential misspelled words (69):
    <BLANKLINE>
        - affordance
        - agroindustry
        - agropay
        - analyse
        - backoffice
        - behavioural
        - bitcoin
        - burdencapital
        - cacioppo
        - centricity
        ...
    <BLANKLINE>
      Matching keys found : 85
      Spell checking process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/demo.the.txt
    <BLANKLINE>
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_MULTI_LEVEL_ANALYSIS
          A_MULTI_LEVEL_ANALYSIS
        A_WIDE_RANGING_RECONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        AFFORDANCE_ACTUALIZATION
          AFFORDANCE_ACTUALIZATION
        AGROINDUSTRY
          AGROINDUSTRY
        AGROPAY
          AGROPAY
        ANALYSE_THE_KEY_FACTORS
          ANALYSE_THE_KEY_FACTORS
        ANALYSE_THE_SYSTEMIC_CHARACTERISTICS
          ANALYSE_THE_SYSTEMIC_CHARACTERISTICS
    <BLANKLINE>
    <BLANKLINE>


    >>> # Restaring the stderr
    >>> sys.stderr = StringIO()

    >>> # Creates, configures, an run the spell checker
    >>> SpellCheck(
    ...     thesaurus_file="demo.the.txt",
    ...     maximum_occurrence=3,
    ...     root_directory="example/",
    ... ).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Spell checking thesaurus keys
      File : example/data/thesaurus/demo.the.txt
      Potential misspelled words (69):
    <BLANKLINE>
        - affordance
        - agroindustry
        - agropay
        - analyse
        - backoffice
        - behavioural
        - bitcoin
        - burdencapital
        - cacioppo
        - centricity
        ...
    <BLANKLINE>
      Matching keys found : 85
      Spell checking process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/demo.the.txt
    <BLANKLINE>
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_MULTI_LEVEL_ANALYSIS
          A_MULTI_LEVEL_ANALYSIS
        A_WIDE_RANGING_RECONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        AFFORDANCE_ACTUALIZATION
          AFFORDANCE_ACTUALIZATION
        AGROINDUSTRY
          AGROINDUSTRY
        AGROPAY
          AGROPAY
        ANALYSE_THE_KEY_FACTORS
          ANALYSE_THE_KEY_FACTORS
        ANALYSE_THE_SYSTEMIC_CHARACTERISTICS
          ANALYSE_THE_SYSTEMIC_CHARACTERISTICS
    <BLANKLINE>
    <BLANKLINE>



"""
import sys

import pandas as pd  # type: ignore
from spellchecker import SpellChecker as ExternalSpellChecker

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class SpellCheck(
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
        sys.stderr.write("Spell checking thesaurus keys\n")
        sys.stderr.write(f"  File : {truncated_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Spell checking process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

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
