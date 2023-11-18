"""Tranform keywords to uppercase in abstract and title"""


import glob
import os
import pathlib
import re

import pandas as pd
from tqdm import tqdm

from ._message import message


def transform_keywords_to_uppercase_in_abstract_and_title(root_dir):
    """:meta private:"""

    message("Transforming keywords in abstracts to upper case with underscores")

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
        #
        documents.to_csv(documents_path, index=False, compression="zip")

    replace_hypen_by_space_in_abstract_column(root_dir)

    #
    # --------------------------------------------------------------------------------------------
    def collect_keywords(column):
        keywords = []
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            if column in data.columns:
                keywords.append(data[column].dropna().copy())
        keywords = pd.concat(keywords)
        return keywords

    def prepare_keywords(keywords):
        keywords = keywords.str.translate(str.maketrans("", "", "\"'#!"))
        keywords = keywords.str.replace(re.compile(r"\(.*\)"), "", regex=True)
        keywords = keywords.str.replace(re.compile(r"\[.*\]"), "", regex=True)
        keywords = keywords.str.translate(str.maketrans("_", " "))
        keywords = keywords.str.lower()
        keywords = keywords.str.split("; ")
        keywords = keywords.explode()
        keywords = keywords.str.strip()
        keywords = keywords.drop_duplicates()
        keywords = keywords.to_list()
        keywords = sorted(keywords, key=lambda x: len(x.split(" ")), reverse=True)
        return keywords

    def process_data(keywords):
        #
        documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
        documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")

        for index, row in tqdm(documents.iterrows(), total=len(documents)):
            #
            descriptors = [
                d
                for d in keywords
                if (
                    isinstance(row["document_title"], str)
                    and d in row["document_title"]
                )
                or (isinstance(row["abstract"], str) and d in row["abstract"])
            ]

            descriptors = sorted(
                descriptors, key=lambda x: len(x.split(" ")), reverse=True
            )

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
                regex,
                lambda z: z.group().upper().replace(" ", "_"),
                str(row["abstract"]),
            )

            documents.loc[index, "document_title"] = new_title
            documents.loc[index, "abstract"] = new_abstract

        documents.to_csv(documents_path, index=False, compression="zip")

    for column in [
        "raw_author_keywords",
        "raw_index_keywords",
    ]:
        keywords = collect_keywords(column)
        keywords = prepare_keywords(keywords)
        process_data(keywords)
