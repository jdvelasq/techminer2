"""Chnage Scopus default column names to TechMiner2 default column names."""

import pathlib

import pandas as pd  #  type: ignore

from ._message import message

SCOPUS_2_TECHMINER_TAGS = {
    "Abbreviated Source Title": "abbr_source_title",
    "Abstract": "raw_abstract",
    "Affiliations": "affiliations",
    "Art. No.": "art_no",
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


def rename_columns_in_database_files(root_dir):
    """Change Scopus original names."""

    message("Applying Scopus tags to database files")

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data.rename(columns=SCOPUS_2_TECHMINER_TAGS, inplace=True)
        #
        # Other columns names not in the standard Scopus format
        data.columns = [name.lower().replace(".", "").replace(" ", "_") for name in data.columns]
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
