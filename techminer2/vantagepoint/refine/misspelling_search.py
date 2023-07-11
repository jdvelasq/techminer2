# flake8: noqa
"""
Misspelling Search
===============================================================================

Look for misspeling mistakes in the keywords of a thesaurus.

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.refine.misspelling_search(
...     root_dir=root_dir,
... )
--INFO-- The file data/regtech/misspelled.txt has been generated.


"""
import sys
from os.path import isfile, join

from spellchecker import SpellChecker
from textblob import TextBlob

from ...thesaurus_lib import load_system_thesaurus_as_dict


def misspelling_search(
    thesaurus_file="descriptors.txt",
    root_dir="./",
):
    """Look for misspeling mistakes in the keywords of a thesaurus."""

    # Load the thesaurus file
    th_file = join(root_dir, thesaurus_file)

    if not isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    th_current = load_system_thesaurus_as_dict(th_file)

    spell = SpellChecker()

    keywords = th_current.values()
    keywords = [word for keyword in keywords for word in keyword]
    keywords = [word for keyword in keywords for word in keyword.split("_")]
    keywords = set(keywords)
    keywords = [word for word in keywords if word.isalpha()]
    misspelled_words = spell.unknown(keywords)
    misspelled_words = sorted(misspelled_words)
    corrected_words = [
        str(TextBlob(word).correct()) for word in misspelled_words
    ]
    words = [
        (misspelled_word, corrected_word)
        for misspelled_word, corrected_word in zip(
            misspelled_words, corrected_words
        )
        if misspelled_word != corrected_word
    ]

    misspelled_file = join(root_dir, "misspelled.txt")
    with open(misspelled_file, "w", encoding="utf-8") as file:
        for misspelled, corrected in words:
            file.write(misspelled.upper() + "\n")
            file.write("    " + corrected.upper() + "\n")

    sys.stdout.write(
        f"--INFO-- The file {misspelled_file} has been generated.\n"
    )
