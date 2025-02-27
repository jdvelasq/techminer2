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


>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="descriptors", 
...     root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.user import SpellCheck
>>> (
...     SpellCheck()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     .having_maximum_occurrence(3)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Spell checking thesaurus keys
  File : example/thesaurus/demo.the.txt
  Potential misspelled words (77):
<BLANKLINE>
    - affordance
    - agroindustry
    - agropay
    - analyse
    - backoffice
    - behavioural
    - bitcoin
    - brummer
    - burdencapital
    - cacioppo
    ...
<BLANKLINE>
  Matching keys found : 91
  Spell checking completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
<BLANKLINE>
    A_BEHAVIOURAL_PERSPECTIVE
      A_BEHAVIOURAL_PERSPECTIVE
    A_MULTI_LEVEL_ANALYSIS
      A_MULTI_LEVEL_ANALYSIS
    A_WIDE_RANGING_RECONCEPTUALIZATION
      A_WIDE_RANGING_RECONCEPTUALIZATION
    A_YOUTH_MICROLOAN
      A_YOUTH_MICROLOAN
    AFFORDANCE_ACTUALIZATION
      AFFORDANCE_ACTUALIZATION
    AGROINDUSTRY
      AGROINDUSTRY
    AGROPAY
      AGROPAY
    ANALYSE
      ANALYSE
<BLANKLINE>



>>> SpellCheck(
...     thesaurus_file="demo.the.txt", 
...     maximum_occurrence=3,
...     root_directory="example/",
... ).run()
Spell checking thesaurus keys
  File : example/thesaurus/demo.the.txt
  Potential misspelled words (77):
<BLANKLINE>
    - affordance
    - agroindustry
    - agropay
    - analyse
    - backoffice
    - behavioural
    - bitcoin
    - brummer
    - burdencapital
    - cacioppo
    ...
<BLANKLINE>
  Matching keys found : 91
  Spell checking completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
<BLANKLINE>
    A_BEHAVIOURAL_PERSPECTIVE
      A_BEHAVIOURAL_PERSPECTIVE
    A_MULTI_LEVEL_ANALYSIS
      A_MULTI_LEVEL_ANALYSIS
    A_WIDE_RANGING_RECONCEPTUALIZATION
      A_WIDE_RANGING_RECONCEPTUALIZATION
    A_YOUTH_MICROLOAN
      A_YOUTH_MICROLOAN
    AFFORDANCE_ACTUALIZATION
      AFFORDANCE_ACTUALIZATION
    AGROINDUSTRY
      AGROINDUSTRY
    AGROPAY
      AGROPAY
    ANALYSE
      ANALYSE
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
        sys.stdout.write("Spell checking thesaurus keys\n")
        sys.stdout.write(f"  File : {truncated_path}\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stdout.write("  Spell checking completed successfully\n\n")
        sys.stdout.flush()

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
            sys.stdout.write("  No misspelled words found\n")
            sys.stdout.flush()
            return

        misspelled_words = self.misspelled_words[:10]
        for i_word, word in enumerate(misspelled_words):
            if i_word == 0:
                sys.stdout.write(
                    f"  Potential misspelled words ({len(self.misspelled_words)}):\n\n"
                )
            sys.stdout.write(f"    - {word}\n")
        if len(misspelled_words) == 10:
            sys.stdout.write("    ...\n\n")
        sys.stdout.flush()

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

        sys.stdout.write(f"  Matching keys found : {n_matches}\n")
        sys.stdout.flush()

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
