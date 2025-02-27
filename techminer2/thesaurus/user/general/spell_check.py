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
<BLANKLINE>
Spell checking completed successfully for file: example/thesaurus/demo.the.txt


>>> SpellCheck(
...     thesaurus_file="demo.the.txt", 
...     maximum_occurrence=3,
...     root_directory="example/",
... ).run()
<BLANKLINE>
Spell checking completed successfully for file: example/thesaurus/demo.the.txt

"""
import sys

import pandas as pd  # type: ignore
from spellchecker import SpellChecker as ExternalSpellChecker

from ..._internals.mixins import ParamsMixin
from .._internals import (
    ThesaurusMixin,
    internal__load_thesaurus_as_data_frame,
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

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 72:
            truncated_path = "..." + truncated_path[-68:]
        sys.stderr.write("\nSpell checking thesaurus keys")
        sys.stderr.write(f"\n  File : {truncated_path}")
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 31:
            truncated_path = "..." + truncated_path[-27:]
        sys.stdout.write(
            f"\nSpell checking completed successfully for file: {truncated_path}"
        )
        sys.stdout.flush()

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
    def internal__print_mispelled_words_to_syserr(self):

        if len(self.misspelled_words) == 0:
            sys.stderr.write("\n  No misspelled words found.")
            sys.stderr.flush()
            return

        misspelled_words = self.misspelled_words[:10]
        for i_word, word in enumerate(misspelled_words):
            if i_word == 0:
                sys.stderr.write("\n  Potential misspelled words:")
            sys.stderr.write(f"\n    - {word}")
        if len(misspelled_words) == 10:
            sys.stderr.write("\n    ...\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__filter_data_frame(self):

        data_frame = self.data_frame
        data_frame["fingerprint"] = (
            data_frame["key"].str.lower().str.replace("_", " ").str.split(" ")
        )

        result = []
        for word in self.misspelled_words:
            result.append(
                data_frame[data_frame["fingerprint"].apply(lambda x: word in x)]
            )

        if result != []:
            self.result = pd.concat(result)
            self.data_frame = self.result[["key", "value"]].drop_duplicates()
        else:
            self.data_frame = None

    # -------------------------------------------------------------------------
    def internal__extract_findings(self):

        if self.data_frame is None:
            self.findings = {}
            return
        keys = self.data_frame.key.drop_duplicates()
        findings = {key: self.mapping[key] for key in sorted(keys)}
        self.findings = findings

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()
        #
        self.internal__extract_words_from_mapping()
        self.internal__search_mispelled_words()
        self.internal__print_mispelled_words_to_syserr()
        self.internal__filter_data_frame()
        self.internal__extract_findings()
        self.internal__write_thesaurus_mapping_to_disk()
        self.internal__notify_process_end()

        internal__print_thesaurus_header(self.thesaurus_path)


# =============================================================================
