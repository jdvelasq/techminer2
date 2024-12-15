# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""Tranform keywords to uppercase in abstract and title"""

import glob
import os
import pathlib
import re

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ._message import message


def _replace_descriptors(root_dir):
    """:meta private:"""

    message("Replacing descriptors in abstracts and titles")

    # --------------------------------------------------------------------------------------------
    def replace_hypen_by_space_in_title_column():
        message('Replacing "-" by " " in `title` column')

        documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
        documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")
        #
        documents["document_title"] = (
            documents["document_title"]
            .astype(str)
            .apply(lambda x: x.translate(str.maketrans("-", " ")))
        )
        documents["document_title"] = (
            documents["document_title"]
            .astype(str)
            .apply(lambda x: x.translate(str.maketrans("_", " ")))
        )
        #
        documents.to_csv(documents_path, index=False, compression="zip")

    replace_hypen_by_space_in_title_column()

    #
    # --------------------------------------------------------------------------------------------
    def replace_hypen_by_space_in_abstract_column(root_dir):
        message('Replacing "-" by " " in `abstract` column')

        documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
        documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")
        #
        documents["abstract"] = (
            documents["abstract"]
            .astype(str)
            .apply(lambda x: x.translate(str.maketrans("-", " ")))
        )
        documents["abstract"] = (
            documents["abstract"]
            .astype(str)
            .apply(lambda x: x.translate(str.maketrans("_", " ")))
        )
        #
        documents.to_csv(documents_path, index=False, compression="zip")

    replace_hypen_by_space_in_abstract_column(root_dir)

    #
    # --------------------------------------------------------------------------------------------
    def collect_terms():
        terms = []
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            for column in [
                "raw_nlp_phrases",
                "raw_author_keywords",
                "raw_index_keywords",
            ]:
                if column in data.columns:
                    terms.append(data[column].dropna().copy())
        terms = pd.concat(terms)
        return terms

    terms = collect_terms()

    #
    # --------------------------------------------------------------------------------------------
    def prepare_terms(terms):
        terms = terms.str.translate(str.maketrans("", "", "\"'#!"))
        terms = terms.str.replace(re.compile(r"\(.*\)"), "", regex=True)
        terms = terms.str.replace(re.compile(r"\[.*\]"), "", regex=True)
        terms = terms.str.translate(str.maketrans("_", " "))
        terms = terms.str.lower()
        terms = terms.str.split("; ")
        terms = terms.explode()
        terms = terms.str.strip()
        terms = terms.drop_duplicates()
        terms = terms.to_list()
        terms = sorted(terms, key=lambda x: (len(x.split(" ")), x), reverse=True)
        return terms

    terms = prepare_terms(terms)

    #
    # --------------------------------------------------------------------------------------------
    def process_data(terms):
        #
        documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
        documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")

        for index, row in tqdm(documents.iterrows(), total=len(documents)):
            #
            descriptors = [
                d
                for d in terms
                if (
                    isinstance(row["document_title"], str)
                    and d in row["document_title"]
                )
                or (isinstance(row["abstract"], str) and d in row["abstract"])
            ]

            descriptors_with_length = [(d, len(d.split(" "))) for d in descriptors]
            lengths = sorted(set(l for _, l in descriptors_with_length), reverse=True)

            new_title = str(row["document_title"])
            new_abstract = str(row["abstract"])

            for length in lengths:

                descriptors = [d for d, l in descriptors_with_length if l == length]
                descriptors = sorted(descriptors, reverse=False)

                aux = descriptors[:]

                descriptors = [re.escape(d) for d in descriptors]
                descriptors += [d + r"(?:'s)" for d in descriptors]  # apostrophe
                descriptors += [d + r":" for d in descriptors]  # colon
                descriptors += [r"\(" + d + r"\)" for d in descriptors]  # parenthesis
                descriptors = "|".join(descriptors)
                regex = re.compile(
                    r"\b(" + descriptors + r")\b",
                    flags=re.IGNORECASE,
                )

                new_title = re.sub(
                    regex,
                    lambda z: z.group().upper().replace(" ", "_"),
                    new_title,
                )

                new_abstract = re.sub(
                    regex,
                    lambda z: z.group().upper().replace(" ", "_"),
                    new_abstract,
                )

            documents.loc[index, "document_title"] = new_title
            documents.loc[index, "abstract"] = new_abstract

        documents.to_csv(documents_path, index=False, compression="zip")

    process_data(terms)
