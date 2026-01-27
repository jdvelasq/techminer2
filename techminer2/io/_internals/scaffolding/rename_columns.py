from pathlib import Path

import pandas as pd  # type: ignore

SCOPUS_2_TECHMINER_TAGS = {
    "Abbreviated Source Title": "source_title_abbr",
    "Abstract": "abstract_raw",
    "Affiliations": "affiliations",
    "Art. No.": "scopus_art_no",
    "Author full names": "author_full_names",
    "Author Keywords": "author_keywords_raw",
    "Author(s) ID": "author_ids_raw",
    "Authors with affiliations": "authors_with_affiliations",
    "Authors": "authors_raw",
    "Chemicals/CAS": "casregnumber",
    "Cited by": "global_citation_count",
    "CODEN": "coden",
    "Conference code": "conference_code",
    "Conference date": "conference_date",
    "Conference location": "conference_location",
    "Conference name": "conference_name",
    "Correspondence Address": "correspondence_address",
    "Document Type": "document_type_raw",
    "DOI": "doi",
    "Editors": "editors",
    "EID": "eid",
    "Funding Details": "funding_details",
    "Funding Texts": "funding_texts",
    "Index Keywords": "index_keywords_raw",
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
    "References": "global_references_raw",
    "Source title": "source_title_raw",
    "Source": "source",
    "Sponsors": "sponsors",
    "Title": "document_title_raw",
    "Tradenames": "tradenames",
    "Volume": "volume",
    "Year": "year",
}


def rename_columns(root_directory: str) -> int:

    processed_dir = Path(root_directory) / "data" / "processed"
    main_file = processed_dir / "main.csv.zip"
    references_file = processed_dir / "references.csv.zip"

    files_processed = 0

    for file in [main_file, references_file]:

        if not file.exists():
            continue

        files_processed += 1

        data_frame = pd.read_csv(
            file,
            encoding="utf-8",
            compression="zip",
            low_memory=False,
        )

        data_frame.rename(columns=SCOPUS_2_TECHMINER_TAGS, inplace=True)
        data_frame.columns = pd.Index(
            [
                # Other columns names not in the standard Scopus format
                name.lower().replace(".", "").replace(" ", "_")
                for name in data_frame.columns
            ]
        )
        data_frame.to_csv(
            file,
            sep=",",
            encoding="utf-8",
            index=False,
            compression="zip",
        )

    return files_processed
