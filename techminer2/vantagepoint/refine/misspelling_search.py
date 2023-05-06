"""
Misspelling search
===============================================================================

Look for misspeling mistakes in the keywords of a thesaurus.

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.misspelling_search(
...     "keywords.txt",
...     directory=directory,
... )
--INFO-- The file data/regtech/processed/misspelled.txt has been generated.


"""
import sys
from os.path import isfile, join
from textblob import TextBlob
from spellchecker import SpellChecker


from ..._thesaurus import load_file_as_dict


def misspelling_search(
    thesaurus_file="keywords.txt",
    directory="./",
):
    """Look for misspeling mistakes in the keywords of a thesaurus."""

    # Load the thesaurus file
    th_file = join(directory, "processed", thesaurus_file)
    if isfile(th_file):
        th = load_file_as_dict(th_file)
    else:
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    spell = SpellChecker()

    keywords = th.values()
    keywords = [word for keyword in keywords for word in keyword]
    keywords = [word for keyword in keywords for word in keyword.split(" ")]
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

    misspelled_file = join(directory, "processed", "misspelled.txt")
    with open(misspelled_file, "w", encoding="utf-8") as file:
        for misspelled, corrected in words:
            file.write(misspelled + "\n")
            file.write("    " + corrected + "\n")

    sys.stdout.write(f"--INFO-- The file {misspelled_file} has been generated.\n")
