"""Tranform keywords to uppercase in abstract and title"""


import glob
import os
import pathlib
import re

import pandas as pd
from tqdm import tqdm

from ._message import message


def transform_keywords_to_uppercase_in_abstract_and_title(root_dir):
    """Transform keywords in abstracts to uppercase

    :meta private:
    """
    message("Transforming keywords in abstracts to upper case with underscores")

    replace_hypen_in_title_column(root_dir)
    replace_hypen_in_abstract_column(root_dir)

    regex1 = re.compile(r"\(.*\)")
    regex2 = re.compile(r"\[.*\]")

    #
    # Load documents
    all_descriptors = []
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if "raw_descriptors" in data.columns:
            all_descriptors.append(data["raw_descriptors"].dropna().copy())
    all_descriptors = pd.concat(all_descriptors)

    #
    # Process all descriptors
    all_descriptors = all_descriptors.str.translate(str.maketrans("", "", "\"'#!"))
    all_descriptors = all_descriptors.str.replace(regex1, "", regex=True)
    all_descriptors = all_descriptors.str.replace(regex2, "", regex=True)
    all_descriptors = all_descriptors.str.translate(str.maketrans("_", " "))
    all_descriptors = all_descriptors.str.lower()
    all_descriptors = all_descriptors.str.split("; ")
    all_descriptors = all_descriptors.explode()
    all_descriptors = all_descriptors.str.strip()
    all_descriptors = all_descriptors.drop_duplicates()
    all_descriptors = all_descriptors.to_list()
    all_descriptors = sorted(
        all_descriptors, key=lambda x: len(x.split(" ")), reverse=True
    )

    #
    # Process the main database
    documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
    documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")

    for index, row in tqdm(documents.iterrows(), total=len(documents)):
        #
        descriptors = [
            d
            for d in all_descriptors
            if (isinstance(row["document_title"], str) and d in row["document_title"])
            or (isinstance(row["abstract"], str) and d in row["abstract"])
        ]

        descriptors = sorted(descriptors, key=lambda x: len(x.split(" ")), reverse=True)

        descriptors = [re.escape(d) for d in descriptors]
        descriptors += [d + r"(?:'s)" for d in descriptors]  # apostrophe
        descriptors += [d + r":" for d in descriptors]  # colon
        descriptors += [r"\(" + d + r"\)" for d in descriptors]  # parenthesis
        descriptors = "|".join(descriptors)
        regex = re.compile(r"\b(" + descriptors + r")\b")

        new_title = re.sub(
            regex,
            lambda z: z.group().upper().replace(" ", "_"),
            str(row["document_title"]),
        )

        new_abstract = re.sub(
            regex, lambda z: z.group().upper().replace(" ", "_"), str(row["abstract"])
        )

        documents.loc[index, "document_title"] = new_title
        documents.loc[index, "abstract"] = new_abstract

    documents.to_csv(documents_path, index=False, compression="zip")


def replace_hypen_in_title_column(root_dir):
    """Replace "-" by " " in `title` column"""

    message('Replacing "-" by " " in `title` column')

    documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
    documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")
    #
    documents["document_title"] = (
        documents["document_title"]
        .astype(str)
        .apply(lambda x: x.translate(str.maketrans("-", " ")))
    )
    #
    documents.to_csv(documents_path, index=False, compression="zip")


def replace_hypen_in_abstract_column(root_dir):
    """Replace "-" by " " in `abstract` column"""

    message('Replacing "-" by " " in `abstract` column')
    documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
    documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")
    #
    documents["abstract"] = (
        documents["abstract"]
        .astype(str)
        .apply(lambda x: x.translate(str.maketrans("-", " ")))
    )
    #
    documents.to_csv(documents_path, index=False, compression="zip")
