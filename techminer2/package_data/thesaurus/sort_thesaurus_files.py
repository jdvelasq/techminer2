# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus Files
===============================================================================


## >>> from techminer2.prepare.thesaurus.default import sort_thesaurus_files
## >>> sort_thesaurus_files()
--INFO-- The _*.the.txt thesaurus files has been sorted.

"""
import glob
import os.path

import pkg_resources  # type: ignore

from ...thesaurus._internals.load_thesaurus_as_mapping import \
    internal__load_thesaurus_as_mapping


def sort_thesaurus_files():
    """:meta private:"""

    file_paths = pkg_resources.resource_filename(
        "techminer2",
        "thesaurus/_data/_*.the.txt",
    )

    for file_path in glob.glob(file_paths):

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        th_dict = internal__load_thesaurus_as_mapping(file_path)

        #
        # Saves the sorted thesaurus to the file
        with open(file_path, "w", encoding="utf-8") as file:
            for key in sorted(th_dict.keys()):
                file.write(key + "\n")
                for item in sorted(set(th_dict[key])):
                    file.write("    " + item + "\n")

    print("--INFO-- The _*.the.txt thesaurus files has been sorted.")
