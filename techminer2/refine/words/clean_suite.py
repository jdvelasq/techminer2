# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Clean Suite
===============================================================================

* Acronym identifier:

>>> from techminer2.refine.words import clean_suite
>>> clean_suite(
...     #
...     # ACTIONS:
...     restart_thesaurus=True,
...     acronym_identifier=True,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
... )
(
    ('AML', 'ANTI MONEY LAUNDERING'),
    ('OF INFORMATION', 'CLASSIFICATION'),
    ('CSR', 'CORPORATE SOCIAL RESPONSIBILITIES'),
    ('GDPR', 'GENERAL DATA PROTECTION REGULATION'),
    ('KYC', 'KNOW YOUR CUSTOMER'),
    ('MANDAS', 'MERGERS AND ACQUISITIONS'),
    ('PSD 2', 'PAYMENT SERVICES DIRECTIVE 2'),
    ('REGTECH', 'REGULATION TECHNOLOGY'),
    ('REGTECH', 'REGULATORY TECHNOLOGY'),
)



"""
import glob
import os
import os.path
import pathlib

import pandas as pd

from ...thesaurus_lib import load_system_thesaurus_as_dict_reversed


def clean_suite(
    #
    # ACTIONS:
    restart_thesaurus=False,
    acronym_identifier=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    # ====================================================================================================
    def restart():
        terms = set()
        thesaurus_file = pathlib.Path(root_dir) / "words.txt"
        with open(thesaurus_file, "r", encoding="utf-8") as file:
            for line in file.readlines():
                if line.startswith("   "):
                    terms.add(line.strip())
        with open(thesaurus_file, "w", encoding="utf-8") as file:
            for term in sorted(terms):
                file.write(term + "\n")
                file.write("    " + term + "\n")

    # ====================================================================================================
    def create_data_frame():
        #
        # Creates a data frame with the existent thesaurus
        thesaurus_file = os.path.join(root_dir, "words.txt")
        thesaurus = load_system_thesaurus_as_dict_reversed(thesaurus_file)
        data_frame = pd.DataFrame(
            {
                "descriptor_text": sorted(thesaurus.keys()),
                "descriptor_key": sorted(thesaurus.values()),
            }
        )

        #
        # Replace hypen by " "
        data_frame["descriptor_key"] = data_frame["descriptor_key"].str.replace("_", " ")
        data_frame["descriptor_text"] = data_frame["descriptor_text"].str.replace("_", " ")

        return data_frame

    # ===================================================================================================
    def create_acronym_list(data_frame):
        #
        data_frame = data_frame.copy()

        #
        # Extracts the acronym and remove rows without acronym
        data_frame["acronym"] = data_frame["descriptor_text"].map(
            lambda x: x[x.find("(") + 1 : x.find(")")] if "(" in x else pd.NA
        )
        data_frame = data_frame[~data_frame.acronym.isna()]

        #
        # remove the acronym from the descriptor, then remove duplicates
        data_frame["descriptor_text"] = data_frame["descriptor_text"].map(
            lambda x: x[: x.find("(")] if "(" in x else x
        )
        data_frame["descriptor_text"] = data_frame["descriptor_text"].str.strip()
        data_frame = data_frame.drop_duplicates(subset=["descriptor_text", "acronym"])

        #
        # Prints the report
        if data_frame.shape[0] > 0:
            print("(")
            for _, row in data_frame.iterrows():
                print(f"    ({repr(row.acronym)}, {repr(row.descriptor_text)}),")
            print(")")

    #
    #  MAIN CODE:
    #
    if restart_thesaurus:
        restart()

    data_frame = create_data_frame()

    if acronym_identifier:
        create_acronym_list(data_frame)


def to_check():
    # pylint: disable=line-too-long
    print(
        "--INFO-- Applying `words.txt` thesaurus to author/index keywords and abstract/title words"
    )

    thesaurus_file = os.path.join(root_dir, "words.txt")
    thesaurus = load_system_thesaurus_as_dict_reversed(thesaurus_file)

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        for raw_column, column in [
            ("raw_author_keywords", "author_keywords"),
            ("raw_index_keywords", "index_keywords"),
            ("raw_keywords", "keywords"),
            ("raw_title_nlp_phrases", "title_nlp_phrases"),
            ("raw_abstract_nlp_phrases", "abstract_nlp_phrases"),
            ("raw_nlp_phrases", "nlp_phrases"),
            ("raw_descriptors", "descriptors"),
        ]:
            if raw_column in data.columns:
                data[column] = data[raw_column].str.split(";")
                data[column] = data[column].map(
                    lambda x: [thesaurus.get(y.strip(), y.strip()) for y in x]
                    if isinstance(x, list)
                    else x
                )
                data[column] = data[column].map(
                    lambda x: sorted(set(x)) if isinstance(x, list) else x
                )
                data[column] = data[column].str.join("; ")
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
