"""
Document Viewer
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> document_viewer('author_keywords', 'fintech', top_n=1, directory=directory)
      document_title : The digital revolution in financial inclusion: international development in the fintech era
             authors : Gabor D; Brooks S
    global_citations : 146
            pub_year : 2017
            abstract : this paper examines the growing importance of digital-based financial inclusion as a form of
                       organising development interventions through networks of state institutions, international
                       development organisations, philanthropic investment and fintech companies.  the
                       fintechphilanthropydevelopment complex generates digital ecosystems that map, expand and
                       monetise digital footprints.  its know thy (irrational) customer vision combines behavioural
                       economics with predictive algorithms to accelerate access to, and monitor engagement with,
                       finance.  the digital revolution adds new layers to the material cultures of financial(ised)
                       inclusion, offering the state new ways of expanding the inclusion of the legible, and global
                       finance new forms of profiling poor households into generators of financial assets.
 raw_author_keywords : behavioural economics
                       digital technologies
                       financial inclusion
                       financialisation
                       fintech
                       governmentality
                       international development
  raw_index_keywords : economic development
                       financial system
                       globalization
                       government
                       institutional framework
                       international organization
                       investment
                       material culture



"""
import textwrap

import pandas as pd

from .utils import load_filtered_documents


def document_viewer(
    column,
    text,
    case=False,
    flags=0,
    regex=True,
    top_n=10,
    directory="./",
):

    documents = load_filtered_documents(directory)
    contains = documents[column].str.contains(text, case=case, flags=flags, regex=regex)
    contains = contains.dropna()
    contains = contains[contains]
    documents = documents.loc[contains.index, :]

    column_list = []

    reported_columns = [
        "document_title",
        "authors",
        "global_citations",
        "source_title",
        "pub_year",
        "abstract",
        "raw_author_keywords",
        "raw_index_keywords",
    ]

    for column in reported_columns:
        if column in documents.columns:
            column_list.append(column)

    documents = documents[column_list]
    if "global_citations" in documents.columns:
        documents = documents.sort_values(by="global_citations", ascending=False)

    documents = documents.head(top_n)

    for index, row in documents.iterrows():

        for column in reported_columns:

            if column not in row.index:
                continue

            if column == "document_title":
                print("      document_title :", end="")
                print(
                    textwrap.fill(
                        row[column],
                        width=115,
                        initial_indent=" " * 23,
                        subsequent_indent=" " * 23,
                        fix_sentence_endings=True,
                    )[22:]
                )
                continue

            if column == "abstract":
                print("            abstract :", end="")
                print(
                    textwrap.fill(
                        row[column],
                        width=115,
                        initial_indent=" " * 23,
                        subsequent_indent=" " * 23,
                        fix_sentence_endings=True,
                    )[22:]
                )
                continue

            if column in [
                "raw_author_keywords",
                "author_keywords",
                "raw_index_keywords",
                "index_keywords",
            ]:
                keywords = row[column]
                if pd.isna(keywords):
                    continue
                keywords = keywords.split("; ")
                print(" {:>19} : {}".format(column, keywords[0]))
                for keyword in keywords[1:]:
                    print(" " * 23 + keyword)
                continue

            print(" {:>19} : {}".format(column, row[column]))

        if index != documents.index[-1]:
            print("-" * 120)
