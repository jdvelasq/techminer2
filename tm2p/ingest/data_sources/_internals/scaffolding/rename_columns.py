from pathlib import Path

import pandas as pd  # type: ignore

from tm2p.enums import CorpusField

SCOPUS_TO_TM2 = {
    #
    # A
    #
    "Abbreviated Source Title": CorpusField.SRC_ISO4_RAW.value,
    "Abstract": CorpusField.ABSTR_RAW.value,
    "Affiliations": CorpusField.AFFIL_RAW.value,
    "Art. No.": CorpusField.ARN.value,
    "Author full names": CorpusField.AUTH_FULL.value,
    "Author Keywords": CorpusField.AUTHKW_RAW.value,
    "Author(s) ID": CorpusField.AUTHID_RAW.value,
    "Authors with affiliations": CorpusField.AUTHAFFIL.value,
    "Authors": CorpusField.AUTH_RAW.value,
    #
    # C
    #
    "Chemicals/CAS": CorpusField.CAS_REG_NO.value,
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
    "Document Type": CorpusField.PUBTYPE_RAW.value,
    "DOI": CorpusField.DOI.value,
    #
    # E
    #
    "Editors": CorpusField.EDITOR.value,
    "EID": CorpusField.EID.value,
    #
    # F
    #
    "Funding Details": CorpusField.FUND_DET.value,
    "Funding Texts": CorpusField.FUND_TXT.value,
    #
    # I
    #
    "Index Keywords": CorpusField.IDXKW_RAW.value,
    "ISBN": CorpusField.ISBN.value,
    "ISSN": CorpusField.ISSN.value,
    "Issue": CorpusField.ISSUE.value,
    #
    # L
    #
    "Language of Original Document": CorpusField.LANG.value,
    "Link": CorpusField.LINK.value,
    #
    # M
    #
    "Manufacturers": CorpusField.MANUFACTURER.value,
    "Molecular Sequence Numbers": CorpusField.SEQ_NO.value,
    #
    # O
    #
    "Open Access": CorpusField.OA.value,
    #
    # P
    #
    "Page count": CorpusField.PG_COUNT.value,
    "Page end": CorpusField.PG_LAST.value,
    "Page start": CorpusField.PG_FIRST.value,
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
    "Source title": CorpusField.SRC_RAW.value,
    "Source": CorpusField.DB_SRC.value,
    "Sponsors": CorpusField.FUND_SPONS.value,
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
    "Year": CorpusField.YEAR.value,
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
