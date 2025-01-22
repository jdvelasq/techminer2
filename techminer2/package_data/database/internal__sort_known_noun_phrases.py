# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Sorts noun phrases.

>>> from techminer2.package_data.database.internal__sort_known_noun_phrases import (
...     internal__sort_known_noun_phrases
... )
>>> internal__sort_known_noun_phrases()

"""

import pkg_resources  # type: ignore


def internal__sort_known_noun_phrases():
    """:meta private:"""

    file_path = pkg_resources.resource_filename(
        "techminer2",
        "package_data/database/data/known_noun_phrases.txt",
    )

    with open(file_path, "r", encoding="utf-8") as file:
        noun_phrases = file.readlines()

    noun_phrases = [phrase.lower().replace("_", " ") for phrase in noun_phrases]
    noun_phrases = sorted(set(noun_phrases))
    noun_phrases = [noun_phrase.strip() for noun_phrase in noun_phrases]

    with open(file_path, "w", encoding="utf-8") as file:
        for noun_phrase in noun_phrases:
            file.write(noun_phrase + "\n")
