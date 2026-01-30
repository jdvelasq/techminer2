from pathlib import Path

import pandas as pd  # type: ignore

from techminer2.enums import Field

SCOPUS_TO_TM2 = {
    #
    # A
    #
    "Abbreviated Source Title": Field.SRCTITLE_ABBR.value,
    "Abstract": Field.ABS_RAW.value,
    "Affiliations": Field.AFFIL.value,
    "Art. No.": Field.ARTNUM.value,
    "Author full names": Field.AUTH_FULL.value,
    "Author Keywords": Field.AUTHKEY_RAW.value,
    "Author(s) ID": Field.AUTH_ID_RAW.value,
    "Authors with affiliations": Field.AUTH_AFFIL.value,
    "Authors": Field.AUTH_RAW.value,
    #
    # C
    #
    "Chemicals/CAS": Field.CASREGNUMBER.value,
    "Cited by": Field.CITCOUNT_GLOBAL.value,
    "CODEN": Field.CODEN.value,
    "Conference code": Field.CONFCODE.value,
    "Conference date": Field.CONFDATE.value,
    "Conference location": Field.CONFLOC.value,
    "Conference name": Field.CONFNAME.value,
    "Correspondence Address": Field.CORRESP.value,
    #
    # D
    #
    "Document Type": Field.DOCTYPE_RAW.value,
    "DOI": Field.DOI.value,
    #
    # E
    #
    "Editors": Field.EDITOR.value,
    "EID": Field.EID.value,
    #
    # F
    #
    "Funding Details": Field.FUND_DETAILS.value,
    "Funding Texts": Field.FUND_TEXTS.value,
    #
    # I
    #
    "Index Keywords": Field.IDXKEY_RAW.value,
    "ISBN": Field.ISBN.value,
    "ISSN": Field.ISSN.value,
    "Issue": Field.ISSUE.value,
    #
    # L
    #
    "Language of Original Document": Field.LANGUAGE.value,
    "Link": Field.LINK.value,
    #
    # M
    #
    "Manufacturers": Field.MANUFACTURER.value,
    "Molecular Sequence Numbers": Field.SEQNUM.value,
    #
    # O
    #
    "Open Access": Field.OA.value,
    #
    # P
    #
    "Page count": Field.PAGES.value,
    "Page end": Field.PAGELAST.value,
    "Page start": Field.PAGEFIRST.value,
    "Publication Stage": Field.PUBSTAGE.value,
    "Publisher": Field.PUBLISHER.value,
    "PubMed ID": Field.PUBMED.value,
    #
    # R
    #
    "References": Field.REF_GLOBAL_RAW.value,
    #
    # S
    #
    "Source title": Field.SRCTITLE_RAW.value,
    "Source": Field.SOURCE.value,
    "Sponsors": Field.FUND_SPONSORS.value,
    #
    # T
    #
    "Title": Field.TITLE_RAW.value,
    "Tradenames": Field.TRADENAME.value,
    #
    # V
    #
    "Volume": Field.VOL.value,
    #
    # Y
    #
    "Year": Field.PUBYEAR.value,
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

        dataframe = pd.read_csv(
            file,
            encoding="utf-8",
            compression="zip",
            low_memory=False,
        )

        dataframe.rename(columns=SCOPUS_TO_TM2, inplace=True)
        mapped_names = set(SCOPUS_TO_TM2.values())
        dataframe.columns = pd.Index(
            [
                (
                    name.lower().replace(".", "").replace(" ", "_")
                    if name not in mapped_names
                    else name
                )
                for name in dataframe.columns
            ]
        )
        temp_file = file.with_suffix(".tmp")
        dataframe.to_csv(
            temp_file,
            sep=",",
            encoding="utf-8",
            index=False,
            compression="zip",
        )
        temp_file.replace(file)

    return files_processed
