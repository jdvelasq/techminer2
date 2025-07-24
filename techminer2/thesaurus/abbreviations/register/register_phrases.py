# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Register Phrases
===============================================================================

Example:
    >>> import shutil
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.abbreviations import RegisterPhrases

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Copy the abbreviations file
    >>> shutil.copy("example/abbreviations.the.txt", "example/data/thesaurus/abbreviations.the.txt")
    'example/data/thesaurus/abbreviations.the.txt'

    >>> # Register new thesaurus phrases
    >>> RegisterPhrases(root_directory="example/", use_colorama=False).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Registering new noun phrases...
      Registration process completed successfully
    <BLANKLINE>
    <BLANKLINE>

"""
import sys

import pkg_resources  # type: ignore

from ...._internals.mixins import Params, ParamsMixin
from ....package_data.text_processing import internal__sort_text_processing_terms
from ..._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)


class RegisterPhrases(
    ParamsMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        sys.stderr.write("Registering new noun phrases...\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Registration process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__get_abbrevaviations_thesaurus_file_path(self):

        params = (
            Params()
            .update(**self.params.__dict__)
            .update(thesaurus_file="abbreviations.the.txt")
        )

        self.abbreviations_path = internal__generate_user_thesaurus_file_path(
            params=params
        )

    # -------------------------------------------------------------------------
    def internal__load_abbreviations_thesaurus_as_mapping(self):
        self.mapping = internal__load_thesaurus_as_mapping(self.abbreviations_path)

    # -------------------------------------------------------------------------
    def internal__make_new_terms_list(self):

        self.new_terms = []
        for abbr, values in self.mapping.items():
            if "_" in abbr:
                self.new_terms.append(abbr)
            for value in values:
                if "_" in value:
                    self.new_terms.append(value)

    # -------------------------------------------------------------------------
    def internal__register_new_terms(self):

        data_path = "package_data/text_processing/data/known_noun_phrases.txt"
        data_path = pkg_resources.resource_filename("techminer2", data_path)

        with open(data_path, "a", encoding="utf-8") as file:
            for term in self.new_terms:
                file.write(f"\n{term}")

                print(term)

        internal__sort_text_processing_terms()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__notify_process_start()
        self.internal__get_abbrevaviations_thesaurus_file_path()
        self.internal__load_abbreviations_thesaurus_as_mapping()
        self.internal__make_new_terms_list()
        self.internal__register_new_terms()
        self.internal__notify_process_end()
