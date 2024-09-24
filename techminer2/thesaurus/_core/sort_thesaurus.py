# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sorts a thesaurus file.

"""
import os.path

from .load_thesaurus_as_dict import load_thesaurus_as_dict


def sort_thesaurus(
    #
    # THESAURURS FILE:
    thesaurus_file,
    order="alphabetical",
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    th_file = os.path.join(root_dir, thesaurus_file)
    th_dict = _load_thesaurus(th_file)
    sorted_keys = _sort_keys(th_dict, order)
    _save_thesaurus(th_file, th_dict, sorted_keys)

    print(f"--INFO-- The file {th_file} has been sorted.")


def _save_thesaurus(th_file, th_dict, sorted_keys):
    with open(th_file, "w", encoding="utf-8") as file:
        for key in sorted_keys:
            file.write(key + "\n")
            for item in sorted(set(th_dict[key])):
                file.write("    " + item + "\n")


def _load_thesaurus(th_file):
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")
    th_dict = load_thesaurus_as_dict(th_file)
    return th_dict


def _sort_keys(th_dict, order):
    if order == "alphabetical":
        return sorted(th_dict.keys(), reverse=False)
    if order == "by-key-length":
        return sorted(th_dict.keys(), key=lambda x: (len(x), x), reverse=False)
    if order == "by-word-length":
        return sorted(th_dict.keys(), key=lambda x: (max(len(y) for y in x.split("_")), x), reverse=True)
    return th_dict.keys()
