# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Apply References Thesaurus 
===============================================================================

Cleans the 'global references' columns using the file references.txt, located 
in the same directory as the documents.csv file.

>>> from techminer2.refine import apply_references_thesaurus
>>> apply_references_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The data/regtech/organizations.txt thesaurus file was applied to affiliations in all databases

"""
import os.path
import pathlib

import pandas as pd

from ....thesaurus_lib import load_system_thesaurus_as_dict_reversed


def apply_references_thesaururs(root_dir):
    """
    :meta private:
    """
    #
    # Apply the thesaurus to raw_global_references
    #

    #
    # Loads the thesaurus
    file_path = pathlib.Path(root_dir) / "global_references.txt"
    th = load_system_thesaurus_as_dict_reversed(file_path=file_path)

    #
    # Loadas the main database
    main_file = os.path.join(root_dir, "databases/_main.zip")
    data = pd.read_csv(main_file, encoding="utf-8", compression="zip")

    #
    # Replace raw_global_references
    data["global_references"] = data["raw_global_references"].str.split("; ")
    data["global_references"] = data["global_references"].map(
        lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore"
    )
    data["global_references"] = data["global_references"].map(
        lambda x: pd.NA if x == [] else x, na_action="ignore"
    )
    data["global_references"] = data["global_references"].map(
        lambda x: ";".join(sorted(x)) if isinstance(x, list) else x
    )

    data.to_csv(main_file, index=False, encoding="utf-8", compression="zip")

    print(
        f"--INFO-- The {file_path} thesaurus file was applied to global_references in 'main' database"
    )
