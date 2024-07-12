# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Misspelling Search
===============================================================================

>>> from techminer2.refine.thesaurus.descriptors import misspelling_search
>>> misspelling_search(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/misspelled.txt has been generated.

"""
import sys
from os.path import isfile, join

from spellchecker import SpellChecker
from textblob import TextBlob

from ....core.thesaurus.load_thesaurus_as_dict import load_thesaurus_as_dict

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def misspelling_search(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # Load the thesaurus file
    th_file = join(root_dir, THESAURUS_FILE)

    if not isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    th_current = load_thesaurus_as_dict(th_file)

    spell = SpellChecker()

    keywords = th_current.values()
    keywords = [word for keyword in keywords for word in keyword]
    keywords = [word for keyword in keywords for word in keyword.split("_")]
    keywords = set(keywords)
    keywords = [word for word in keywords if word.isalpha()]
    misspelled_words = spell.unknown(keywords)
    misspelled_words = sorted(misspelled_words)
    corrected_words = [str(TextBlob(word).correct()) for word in misspelled_words]
    words = [
        (misspelled_word, corrected_word)
        for misspelled_word, corrected_word in zip(misspelled_words, corrected_words)
        if misspelled_word != corrected_word
    ]

    misspelled_file = join(root_dir, "reports/misspelled.txt")
    with open(misspelled_file, "w", encoding="utf-8") as file:
        for misspelled, corrected in words:
            file.write(misspelled.upper() + "\n")
            file.write("    " + corrected.upper() + "\n")

    sys.stdout.write(f"--INFO-- The file {misspelled_file} has been generated.\n")
