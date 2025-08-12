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
    >>> # Redirect stderr to capture output
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Check last word in noun phrases
    >>> from techminer2.package_data.text_processing import internal__sort_noun_phrases_by_last_word
    >>> internal__sort_noun_phrases_by_last_word()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting system noun phrases by last word
      Sorting process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""


from .load_text_processing_terms import internal__load_text_processing_terms
from .save_text_processing_terms import internal__save_text_processing_terms
import sys
from colorama import Fore, init


def internal__sort_noun_phrases_by_last_word():
    """:meta private:"""

    sys.stderr.write(f"Sorting system noun phrases by last word\n")
    sys.stderr.flush()

    noun_phrases = internal__load_text_processing_terms("known_noun_phrases.txt")

    noun_phrases.sort(key=lambda x: x[::-1])

    internal__save_text_processing_terms("known_noun_phrases.txt", noun_phrases)

    sys.stderr.write("  Sorting process completed successfully\n\n")
    sys.stderr.flush()
