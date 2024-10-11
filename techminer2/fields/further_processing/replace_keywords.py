# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import glob
import os
import pathlib
import re

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

# Register tqdm pandas progress bar
tqdm.pandas()


def replace_keywords(
    #
    # DATABASE PARAMS:
    root_dir,
):
    #
    # --------------------------------------------------------------------------------------------
    def collect_keywords():
        terms = []
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        for file in files:
            #
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            #
            keywords = data["raw_keywords"].dropna().copy()
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
            #
            terms += keywords

        terms = list(set(terms))
        terms = sorted(terms, key=lambda x: len(x.split(" ")), reverse=True)
        return terms

    keywords = collect_keywords()

    #
    # ------------------------------------------------------------------------------------------------
    def replace_keywords_per_record(keywords):

        documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
        documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")

        for index, row in tqdm(documents.iterrows(), total=len(documents)):

            selected_keywords = [
                d
                for d in keywords
                if (isinstance(row["document_title"], str) and d in row["document_title"])
                or (isinstance(row["abstract"], str) and d in row["abstract"])
            ]

            selected_keywords = sorted(selected_keywords, key=lambda x: len(x.split(" ")), reverse=True)

            selected_keywords = [re.escape(d) for d in selected_keywords]
            selected_keywords += [d + r"(?:'s)" for d in selected_keywords]  # apostrophe
            selected_keywords += [d + r":" for d in selected_keywords]  # colon
            selected_keywords += [r"\(" + d + r"\)" for d in selected_keywords]  # parenthesis
            selected_keywords = "|".join(selected_keywords)
            regex = re.compile(r"\b(" + selected_keywords + r")\b")

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

    replace_keywords_per_record(keywords)
