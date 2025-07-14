# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Register Initial Word
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, RegisterInitialWord

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Register a new initial word
    >>> (
    ...     RegisterInitialWord()
    ...     .having_word("ABDUCT")
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Registering new common initial word...
      Registration process completed successfully
    <BLANKLINE>
    <BLANKLINE>

"""
import sys

import pkg_resources  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....package_data.text_processing import internal__sort_text_processing_terms


class RegisterInitialWord(
    ParamsMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        sys.stderr.write("Registering new common initial word...\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Registration process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__register_new_word(self):

        data_path = "package_data/text_processing/data/common_initial_words.txt"
        data_path = pkg_resources.resource_filename("techminer2", data_path)

        with open(data_path, "a", encoding="utf-8") as file:
            file.write(f"\n{self.params.word}\n")

        internal__sort_text_processing_terms()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__notify_process_start()
        self.internal__register_new_word()
        self.internal__notify_process_end()
