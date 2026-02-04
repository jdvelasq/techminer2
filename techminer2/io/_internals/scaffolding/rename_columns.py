from pathlib import Path

import pandas as pd  # type: ignore

from techminer2.enums import Field

SCOPUS_TO_TM2 = {
    #
    # A
    #
    "Abbreviated Source Title": Field.SRC_TITLE_ABBR_RAW.value,
    "Abstract": Field.ABS_RAW.value,
    "Affiliations": Field.AFFIL_RAW.value,
    "Art. No.": Field.ART_NO.value,
    "Author full names": Field.AUTH_FULL.value,
    "Author Keywords": Field.AUTH_KEY_RAW.value,
    "Author(s) ID": Field.AUTH_ID_RAW.value,
    "Authors with affiliations": Field.AUTH_AFFIL.value,
    "Authors": Field.AUTH_RAW.value,
    #
    # C
    #
    "Chemicals/CAS": Field.CAS_REG_NUMBER.value,
    "Cited by": Field.CIT_COUNT_GLOBAL.value,
    "CODEN": Field.CODEN.value,
    "Conference code": Field.CONF_CODE.value,
    "Conference date": Field.CONF_DATE.value,
    "Conference location": Field.CONF_LOC.value,
    "Conference name": Field.CONF_NAME.value,
    "Correspondence Address": Field.CORRESP.value,
    #
    # D
    #
    "Document Type": Field.DOC_TYPE_RAW.value,
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
    "Index Keywords": Field.IDX_KEY_RAW.value,
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
    "Molecular Sequence Numbers": Field.SEQ_NUM.value,
    #
    # O
    #
    "Open Access": Field.OA.value,
    #
    # P
    #
    "Page count": Field.PAGE_COUNT.value,
    "Page end": Field.PAGE_LAST.value,
    "Page start": Field.PAGE_FIRST.value,
    "Publication Stage": Field.PUB_STAGE.value,
    "Publisher": Field.PUBLISHER.value,
    "PubMed ID": Field.PUBMED.value,
    #
    # R
    #
    "References": Field.REF_RAW.value,
    #
    # S
    #
    "Source title": Field.SRC_TITLE_RAW.value,
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
