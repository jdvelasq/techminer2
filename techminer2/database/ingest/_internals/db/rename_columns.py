# flake8: noqa
"""Chnage Scopus default column names to TechMiner2 default column names."""

import pathlib
import sys

import pandas as pd  # type: ignore

SCOPUS_2_TECHMINER_TAGS = {
    "Abbreviated Source Title": "abbr_source_title",
    "Abstract": "raw_abstract",
    "Affiliations": "affiliations",
    "Art. No.": "scopus_art_no",
    "Author full names": "author_full_names",
    "Author Keywords": "raw_author_keywords",
    "Author(s) ID": "raw_authors_id",
    "Authors with affiliations": "authors_with_affiliations",
    "Authors": "raw_authors",
    "Chemicals/CAS": "casregnumber",
    "Cited by": "global_citations",
    "CODEN": "coden",
    "Conference code": "conference_code",
    "Conference date": "conference_date",
    "Conference location": "conference_location",
    "Conference name": "conference_name",
    "Correspondence Address": "correspondence_address",
    "Document Type": "raw_document_type",
    "DOI": "doi",
    "Editors": "editors",
    "EID": "eid",
    "Funding Details": "funding_details",
    "Funding Texts": "funding_texts",
    "Index Keywords": "raw_index_keywords",
    "ISBN": "isbn",
    "ISSN": "issn",
    "Issue": "issue",
    "Language of Original Document": "language",
    "Link": "link",
    "Manufacturers": "manufacturers",
    "Molecular Sequence Numbers": "molecular_sequence_numbers",
    "Open Access": "open_access",
    "Page count": "page_count",
    "Page end": "page_end",
    "Page start": "page_start",
    "Publication Stage": "publication_stage",
    "Publisher": "publisher",
    "PubMed ID": "pubmed",
    "References": "raw_global_references",
    "Source title": "raw_source_title",
    "Source": "source",
    "Sponsors": "sponsors",
    "Title": "raw_document_title",
    "Tradenames": "tradenames",
    "Volume": "volume",
    "Year": "year",
}


def internal__rename_columns(root_dir):
    """Change Scopus original names."""

    sys.stderr.write("INFO  Applying Scopus tags to database files\n")
    sys.stderr.flush()

    database_file = pathlib.Path(root_dir) / "data/processed/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    dataframe.rename(columns=SCOPUS_2_TECHMINER_TAGS, inplace=True)
    dataframe.columns = [
        # Other columns names not in the standard Scopus format
        name.lower().replace(".", "").replace(" ", "_")
        for name in dataframe.columns
    ]
    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
