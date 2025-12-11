# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Sorts text processing terms.

>>> from techminer2.package_data.text_processing import (
...     internal__sort_text_processing_terms,
... )
>>> internal__sort_text_processing_terms()

"""
import glob
import unicodedata  # type: ignore
from importlib.resources import files


def get_file_names():

    data_path = files("techminer2.package_data.text_processing.data").joinpath("*.txt")
    data_path = str(data_path)
    file_names = glob.glob(data_path)
    return file_names


def sort_connectors(file_name):

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    #
    lines = [line.strip().lower() for line in lines]
    lines = [line.replace("_", " ") for line in lines]
    lines = list(set(lines))
    lines = sorted(lines)
    #
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def sort_copyright_regex(file_name):

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    #
    lines = [line.strip().lower() for line in lines]
    lines = [line.replace("_", " ").lower() for line in lines]

    lines = list(set(lines))
    lines = [(len(line.split(" ")), line) for line in lines]
    lines = sorted(lines, reverse=True)
    lines = [line[1] for line in lines]

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def sort_known_noun_phrases(file_name):
    """:meta private:"""

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    #
    lines = [line.strip().upper() for line in lines]
    lines = [line.replace(" ", "_") for line in lines]
    lines = [line for line in lines if line != ""]
    lines = sorted(set(lines))

    #
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def sort_known_organizations(file_name):
    """:meta private:"""

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    #
    # remove accents
    lines = [unicodedata.normalize("NFKD", line) for line in lines]
    lines = [line.encode("ASCII", "ignore") for line in lines]
    lines = [line.decode() for line in lines]
    #
    lines = [line.replace("_", " ") for line in lines]
    lines = list(set(lines))
    #
    lines = sorted(lines)

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def sort_hypened_words(file_name):
    """:meta private:"""

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = sorted(set(lines))

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def sort_discursive_patterns(file_name):
    """:meta private:"""

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip().lower().replace("_", " ") for line in lines]
    lines = sorted(set(lines))

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def sort_technical_stopwords(file_name):

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    #
    lines = [line.strip().lower() for line in lines]
    lines = list(set(lines))
    lines = sorted(set(lines))
    #
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def sort_common_words(file_name):

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    #
    lines = [line.strip().upper() for line in lines]
    lines = list(set(lines))
    lines = sorted(lines)
    lines = [line for line in lines if line != ""]
    #
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def internal__sort_text_processing_terms():
    """:meta private:"""

    file_names = get_file_names()
    for file_name in file_names:

        if file_name.endswith("connectors.txt"):
            sort_connectors(file_name)
            continue

        if file_name.endswith("copyright_regex.txt"):
            sort_copyright_regex(file_name)
            continue

        if file_name.endswith("known_noun_phrases.txt"):
            sort_known_noun_phrases(file_name)
            continue

        if file_name.endswith("known_organizations.txt"):
            sort_known_organizations(file_name)
            continue

        if file_name.endswith("hyphenated_is_correct.txt"):
            sort_hypened_words(file_name)
            continue

        if file_name.endswith("hyphenated_is_incorrect.txt"):
            sort_hypened_words(file_name)
            continue

        if file_name.endswith("discursive_patterns.txt"):
            sort_discursive_patterns(file_name)
            continue

        if file_name.endswith("technical_stopwords.txt"):
            sort_technical_stopwords(file_name)
            continue

        if file_name.endswith("common_initial_words.txt"):
            sort_common_words(file_name)
            continue

        if file_name.endswith("common_last_words.txt"):
            sort_common_words(file_name)
            continue
