import sys
import textwrap

import pandas as pd


def print_documents(documents, file=sys.stdout):

    column_list = []

    reported_columns = [
        "document_title",
        "authors",
        "global_citations",
        "source_name",
        "pub_year",
        "abstract",
        "author_keywords",
        "index_keywords",
    ]

    for column in reported_columns:
        if column in documents.columns:
            column_list.append(column)

    documents = documents[column_list]
    if "global_citations" in documents.columns:
        documents = documents.sort_values(by="global_citations", ascending=False)

    for index, row in documents.iterrows():

        for column in reported_columns:

            if column not in row.index:
                continue

            if column == "document_title":
                print("           document_title :", end="", file=file)
                print(
                    textwrap.fill(
                        row[column],
                        width=120,
                        initial_indent=" " * 28,
                        subsequent_indent=" " * 28,
                        fix_sentence_endings=True,
                    )[27:],
                    file=file,
                )
                continue

            if column == "abstract":
                print("                 abstract :", end="", file=file)
                print(
                    textwrap.fill(
                        row[column],
                        width=120,
                        initial_indent=" " * 28,
                        subsequent_indent=" " * 28,
                        fix_sentence_endings=True,
                    )[27:],
                    file=file,
                )
                continue

            if column in [
                "source_name",
                "author_keywords",
                "author_keywords_cleaned",
                "index_keywords",
                "index_keywords_cleaned",
            ]:
                keywords = row[column]
                if pd.isna(keywords):
                    continue
                keywords = keywords.split("; ")
                print(" {:>24} : {}".format(column, keywords[0]), file=file)
                for keyword in keywords[1:]:
                    print(" " * 28 + keyword, file=file)
                continue

            print(" {:>24} : {}".format(column, row[column]), file=file)

        if index != documents.index[-1]:
            print("-" * 125, file=file)
