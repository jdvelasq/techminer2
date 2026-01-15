# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Register Keyword
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, RegisterKeyword

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Register a new keyword
    >>> (
    ...     RegisterKeyword()
    ...     .having_word("ARTIFICIAL_NEURAL_NETWORK")
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Registering new keyword...
      Registration process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""
import sys
from importlib.resources import files

from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.package_data.text_processing import (
    internal__sort_text_processing_terms,
)


class RegisterKeyword(
    ParamsMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        sys.stderr.write("Registering new keyword...\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Registration process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__register_new_word(self):

        data_path = files("techminer2.package_data.text_processing.data").joinpath(
            "known_noun_phrases.txt"
        )
        data_path = str(data_path)

        words = self.params.word
        if isinstance(words, str):
            words = [words]

        words = [word.strip().upper() for word in words]

        with open(data_path, "a", encoding="utf-8") as file:
            for word in words:
                if word == "":
                    continue
                file.write(f"\n{word}")

        internal__sort_text_processing_terms()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__notify_process_start()
        self.internal__register_new_word()
        self.internal__notify_process_end()
