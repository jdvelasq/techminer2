# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
import os.path
import pandas as pd

from techminer2._internals import Params
from techminer2.database._internals.io import internal__load_all_records_from_database
from techminer2.package_data.text_processing import internal__load_text_processing_terms


def collect_project_hyphenated_words(root_dir):

    dataframe = internal__load_all_records_from_database(
        Params(root_directory=root_dir)
    )

    words = []
    for column in [
        "raw_author_keywords",
        "raw_index_keywords",
    ]:
        if column in dataframe.columns:
            words.append(dataframe[column].dropna().copy())

    words = pd.concat(words)
    words = words.str.upper()
    words = words.str.split("; ")
    words = words.explode()
    words = words.str.split(" ")
    words = words.explode()
    words = words.str.strip()
    words = words[words.str.contains("-")]
    words = words.str.replace("-", "_", regex=False)
    words = words.to_list()
    words = list(set(words))

    return words


def collect_system_hyphenated_words():
    words = internal__load_text_processing_terms("hyphenated_is_correct.txt")
    words += internal__load_text_processing_terms("hyphenated_is_incorrect.txt")
    return words


def internal__check_hyphenated_form(root_dir):
    project_words = collect_project_hyphenated_words(root_dir)
    system_words = collect_system_hyphenated_words()
    undetected_words = set(project_words) - set(system_words)

    file_path = os.path.join(
        root_dir, "data/my_keywords/undetected_hyphenated_words.txt"
    )
    with open(file_path, "w") as f:
        for word in sorted(undetected_words):
            f.write(f"{word}\n")
