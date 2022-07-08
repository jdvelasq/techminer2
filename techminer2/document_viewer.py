"""
Document Viewer
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> document_viewer(
...     'author_keywords', 
...     'regtech',
...     top_n=1,
...     directory=directory,
... )
               title : Fintech and regtech: Impact on regulators and banks
             authors : Anagnostopoulos I
    global_citations : 110
        source_title : Journal of Economics and Business
                year : 2018
 raw_author_keywords : business models
                       financial services
                       fintech
                       future research direction
                       regtech
                       regulation

"""
import textwrap

import pandas as pd

from ._read_records import read_records


def document_viewer(
    col,
    text,
    case=False,
    flags=0,
    regex=True,
    top_n=10,
    directory="./",
    database="documents",
):
    """Document  viewer."""

    documents = read_records(directory=directory, database=database, use_filter=False)
    contains = documents[col].str.contains(text, case=case, flags=flags, regex=regex)
    contains = contains.dropna()
    contains = contains[contains]
    documents = documents.loc[contains.index, :]

    column_list = []

    reported_columns = [
        "title",
        "authors",
        "global_citations",
        "source_title",
        "year",
        "abstract",
        "raw_author_keywords",
        "raw_index_keywords",
    ]

    for col in reported_columns:

        if col in documents.columns:
            column_list.append(col)

    documents = documents[column_list]
    if "global_citations" in documents.columns:
        documents = documents.sort_values(by="global_citations", ascending=False)

    documents = documents.head(top_n)

    for index, row in documents.iterrows():

        for col in reported_columns:

            if col not in row.index:
                continue

            if col == "document_title":
                print("      document_title :", end="")
                print(
                    textwrap.fill(
                        row[col],
                        width=115,
                        initial_indent=" " * 23,
                        subsequent_indent=" " * 23,
                        fix_sentence_endings=True,
                    )[22:]
                )
                continue

            if col == "abstract":
                if not pd.isna(row[col]):
                    print("            abstract :", end="")
                    print(
                        textwrap.fill(
                            row[col],
                            width=115,
                            initial_indent=" " * 23,
                            subsequent_indent=" " * 23,
                            fix_sentence_endings=True,
                        )[22:]
                    )
                continue

            if col in [
                "raw_author_keywords",
                "author_keywords",
                "raw_index_keywords",
                "index_keywords",
            ]:
                keywords = row[col]
                if pd.isna(keywords):
                    continue
                keywords = keywords.split("; ")
                print(" {:>19} : {}".format(col, keywords[0]))
                for keyword in keywords[1:]:
                    print(" " * 23 + keyword)
                continue

            print(" {:>19} : {}".format(col, row[col]))

        if index != documents.index[-1]:
            print("-" * 120)
