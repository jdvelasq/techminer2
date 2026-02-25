from pathlib import Path

import pandas as pd  # type: ignore

from techminer2.enums import CorpusField

SCOPUS_TO_TM2 = {
    #
    # A
    #
    "Abbreviated Source Title": CorpusField.SRC_TITLE_ABBR_RAW.value,
    "Abstract": CorpusField.ABS_RAW.value,
    "Affiliations": CorpusField.AFFIL_RAW.value,
    "Art. No.": CorpusField.ART_NO.value,
    "Author full names": CorpusField.AUTH_FULL.value,
    "Author Keywords": CorpusField.AUTH_KEY_RAW.value,
    "Author(s) ID": CorpusField.AUTH_ID_RAW.value,
    "Authors with affiliations": CorpusField.AUTH_AFFIL.value,
    "Authors": CorpusField.AUTH_RAW.value,
    #
    # C
    #
    "Chemicals/CAS": CorpusField.CAS_REG_NUMBER.value,
    "Cited by": CorpusField.GCS.value,
    "CODEN": CorpusField.CODEN.value,
    "Conference code": CorpusField.CONF_CODE.value,
    "Conference date": CorpusField.CONF_DATE.value,
    "Conference location": CorpusField.CONF_LOC.value,
    "Conference name": CorpusField.CONF_NAME.value,
    "Correspondence Address": CorpusField.CORRESP.value,
    #
    # D
    #
    "Document Type": CorpusField.DOC_TYPE_RAW.value,
    "DOI": CorpusField.DOI.value,
    #
    # E
    #
    "Editors": CorpusField.EDITOR.value,
    "EID": CorpusField.EID.value,
    #
    # F
    #
    "Funding Details": CorpusField.FUND_DETAILS.value,
    "Funding Texts": CorpusField.FUND_TEXTS.value,
    #
    # I
    #
    "Index Keywords": CorpusField.IDX_KEY_RAW.value,
    "ISBN": CorpusField.ISBN.value,
    "ISSN": CorpusField.ISSN.value,
    "Issue": CorpusField.ISSUE.value,
    #
    # L
    #
    "Language of Original Document": CorpusField.LANGUAGE.value,
    "Link": CorpusField.LINK.value,
    #
    # M
    #
    "Manufacturers": CorpusField.MANUFACTURER.value,
    "Molecular Sequence Numbers": CorpusField.SEQ_NUMBER.value,
    #
    # O
    #
    "Open Access": CorpusField.OA.value,
    #
    # P
    #
    "Page count": CorpusField.PAGE_COUNT.value,
    "Page end": CorpusField.PAGE_LAST.value,
    "Page start": CorpusField.PAGE_FIRST.value,
    "Publication Stage": CorpusField.PUBSTAGE.value,
    "Publisher": CorpusField.PUBLISHER.value,
    "PubMed ID": CorpusField.PUBMED.value,
    #
    # R
    #
    "References": CorpusField.REF_RAW.value,
    #
    # S
    #
    "Source title": CorpusField.SRC_TITLE_RAW.value,
    "Source": CorpusField.SOURCE.value,
    "Sponsors": CorpusField.FUND_SPONSORS.value,
    #
    # T
    #
    "Title": CorpusField.TITLE_RAW.value,
    "Tradenames": CorpusField.TRADENAME.value,
    #
    # V
    #
    "Volume": CorpusField.VOL.value,
    #
    # Y
    #
    "Year": CorpusField.PUBYEAR.value,
}


def rename_columns(root_directory: str) -> int:

    processed_dir = Path(root_directory) / "ingest" / "processed"
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
