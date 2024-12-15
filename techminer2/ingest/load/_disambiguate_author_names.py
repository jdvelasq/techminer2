"""Disambiguate author names using Scopus Author(s) ID."""

import glob
import os

import pandas as pd  # type: ignore

from ._message import message


def disambiguate_author_names(root_dir):
    """Disambiguate author names using Scopus Author(s) ID."""

    #
    def load_authors_names():
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        data = [
            pd.read_csv(file, encoding="utf-8", compression="zip")[
                ["authors", "authors_id"]
            ]
            for file in files
        ]
        data = pd.concat(data)
        data = data.dropna()

        return data

    #
    def build_dict_names(data):
        data = data.copy()
        data = data.assign(authors_and_ids=data.authors + "#" + data.authors_id)
        data.authors_and_ids = data.authors_and_ids.str.split("#")
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: (x[0].split(";"), x[1].split(";"))
        )
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: list(zip(x[0], x[1]))
        )
        data = data.explode("authors_and_ids")
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: (x[0].strip(), x[1].strip())
        )
        data = data.reset_index(drop=True)
        data = data[["authors_and_ids"]]
        data["author"] = data.authors_and_ids.apply(lambda x: x[0])
        data["author_id"] = data.authors_and_ids.apply(lambda x: x[1])

        # assert data.author_id.map(lambda x: "7401744122" in x).sum() > 0

        data = data.drop(columns=["authors_and_ids"])
        data = data.drop_duplicates()
        data = data.sort_values(by=["author"])
        data = data.assign(counter=data.groupby(["author"]).cumcount())
        data = data.assign(author=data.author + "/" + data.counter.astype(str))
        data.author = data.author.str.replace("/0", "")
        author_id2name = dict(zip(data.author_id, data.author))
        return author_id2name

    def repair_names(author_id2name):
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            data = data.assign(authors=data.authors_id.copy())
            data["authors"] = data["authors"].str.split(";")
            data["authors"] = data["authors"].map(
                lambda x: [author_id2name[id.strip()] for id in x],
                na_action="ignore",
            )
            data["authors"] = data["authors"].str.join("; ")
            data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    #
    message("Disambiguating `authors` column")
    data = load_authors_names()
    author_id2name = build_dict_names(data)
    repair_names(author_id2name)
