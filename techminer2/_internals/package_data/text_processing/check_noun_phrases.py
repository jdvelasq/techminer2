# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

Smoke tests:
    >>> # Redirect stderr to capture output
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Check last word in noun phrases
    >>> from techminer2.package_data.text_processing import internal__check_noun_phrases
    >>> internal__check_noun_phrases(disable_tqdm=True)

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Checking last word in system noun phrases
      Checking process completed successfully
    <BLANKLINE>
    <BLANKLINE>



"""


import sys

from textblob import Word
from tqdm import tqdm

from .load_text_processing_terms import load_text_processing_terms
from .save_text_processing_terms import save_text_processing_terms


def get_plural_pairs(last_words):
    plurals = [
        (word, str(Word(word.lower()).pluralize()).upper()) for word in last_words
    ]
    plurals = list(set((a, b) for a, b in plurals if b in last_words and a != b))
    return plurals


def get_singular_pairs(last_words):
    singulars = [
        (word, str(Word(word.lower()).singularize()).upper()) for word in last_words
    ]
    singulars = list(set((b, a) for a, b in singulars if b in last_words and a != b))
    return singulars


def replace_pair(noun_phrases, word1, word2):

    new_noun_phrases = []
    for noun_phrase in noun_phrases:
        if noun_phrase.endswith(f"_{word1}"):
            new_noun_phrases.append(noun_phrase.replace(f"_{word1}", f"_{word2}"))

    noun_phrases += new_noun_phrases
    noun_phrases = sorted(set(noun_phrases))

    return noun_phrases


def internal__check_noun_phrases(disable_tqdm=False):

    sys.stderr.write(f"Checking last word in system noun phrases\n")
    sys.stderr.flush()

    noun_phrases = load_text_processing_terms("noun_phrases.txt")
    last_words = [phrase.split("_")[-1] for phrase in noun_phrases]
    plurals = get_plural_pairs(last_words)
    singulars = get_singular_pairs(last_words)

    pairs = list(set(plurals + singulars))

    for word1, word2 in tqdm(
        pairs, desc="  Processing", total=len(pairs), ncols=80, disable=disable_tqdm
    ):
        noun_phrases = replace_pair(noun_phrases, word1, word2)

    save_text_processing_terms("noun_phrases.txt", noun_phrases)

    sys.stderr.write("  Checking process completed successfully\n\n")
    sys.stderr.flush()
