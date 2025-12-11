# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

Example:
    # >>> # Redirect stderr to capture output
    # >>> import sys
    # >>> from io import StringIO
    # >>> original_stderr = sys.stderr
    # >>> sys.stderr = StringIO()

    # >>> # Check last word in noun phrases
    # >>> from techminer2.package_data.text_processing import internal__testing
    # >>> internal__testing()

    # >>> # Capture and print stderr output
    # >>> output = sys.stderr.getvalue()
    # >>> sys.stderr = original_stderr
    # >>> print(output)


"""


import sys

from colorama import Fore, init

from ..text_processing.load_text_processing_terms import (
    internal__load_text_processing_terms,
)
from ..text_processing.save_text_processing_terms import (
    internal__save_text_processing_terms,
)


def internal__testing():
    """:meta private:"""

    noun_phrases = internal__load_text_processing_terms("known_noun_phrases.txt")

    noun_phrases = [phrase.split("_")[-1] for phrase in noun_phrases]
    noun_phrases = sorted(set(noun_phrases))

    selected_terms = []
