from pathlib import Path

from tm2p._intern.enum.field import Field

from ..get_datab_marker import get_datab_marker
from ._renam_col import renam_col

OPENALEX_TO_TM2 = {
    "id": Field.ART_NO.value,
    "abstract": Field.ABSTR_RAW.value,
    "authorships.author.display_name": Field.AUTH_FULL_NAME.value,
    "authorships.author.id": Field.AUTHID.value,
    "authorships.author.orcid": Field.ORCID.value,
    "authorships.countries": Field.CTRY_ISO2.value,
    "authorships.institutions.display_name": Field.ORG.value,
    "authorships.institutions.id": Field.ORG_ID.value,
    "authorships.is_corresponding": Field.IS_CORRESPOND.value,
    "best_oa_location.license": Field.OA_LICENSE.value,
    "cited_by_count": Field.GCS.value,
    "corresponding_institution_ids": Field.CORRESPOND_ORG_ID.value,
    "display_name": Field.TITLE_RAW.value,
    "doi": Field.DOI.value,
    "funders.display_name": Field.FUND_DET.value,
    "fwci": Field.FWCI.value,
    "ids.pmid": Field.PUBMED.value,
    "is_retracted": Field.IS_RETRACTED.value,
    "language": Field.LANG.value,
    "open_access.is_oa": Field.IS_OA.value,
    "open_access.oa_status": Field.OA.value,
    "primary_location.source.display_name": Field.SRC.value,
    "primary_location.source.id": Field.SRC_ID.value,
    "primary_location.source.issn_l": Field.ISSN.value,
    "primary_location.source.type": Field.SRC_TYPE.value,
    "primary_topic.display_name": Field.ASJC.value,
    "publication_date": Field.DATE.value,
    "publication_year": Field.YEAR.value,
    "type": Field.DOCTYPE.value,
}


PUBMED_TO_TM2 = {
    "AB": Field.ABSTR_RAW.value,  #         → Abstract
    "AD": Field.AFFIL.value,  #             → Affiliations
    "AID": Field.DOI.value,  #              → DOI / Article Identifier
    "AU": Field.AUTH_RAW.value,  #          → Authors
    "AUID": Field.ORCID.value,  #           → ORCID
    "CI": Field.COPYRIGHT.value,  #         → Copyright
    "CN": Field.CORP_AUTH.value,  #         → Corporate Author
    "COIS": Field.COIS.value,  #            → Conflict of Interest Statement
    "CRDT": Field.CRDT.value,  #            → Creation Date
    "CRF": Field.CRF.value,  #              → Corrected and Republished From
    "CRI": Field.CRI.value,  #              → Corrected and Republished In
    "CTI": Field.CTI.value,  #              → Collective Title
    "DA": Field.DA.value,  #                → Date Created
    "DEP": Field.DEP.value,  #              → Date of Electronic Publication
    "DP": Field.YEAR.value,  #              → Year / Date
    "EDAT": Field.EDAT.value,  #            → Entry Date
    "FAU": Field.AUTH_FULL_NAME.value,  #   → Authors (Full Name)
    "FED": Field.EDITOR.value,  #           → Editors
    "FIR": Field.FIR.value,  #              → Full Investigator Name
    "GR": Field.FUND_DET.value,  #          → Funding Details
    "IRAD": Field.IRAD.value,  #            → Investigator Affiliation
    "IS": Field.ISSN.value,  #              → ISSN
    "JT": Field.SRC.value,  #               → Source Title
    "LA": Field.LANG.value,  #              → Language of Original Document
    "LID": Field.ART_NO.value,  #           → ART_NO
    "MH": Field.IDXKW_RAW.value,  #         → Index Keywords (controlled vocabulary)
    "MHDA": Field.MHDA.value,  #            → MeSH Date
    "MID": Field.MID.value,  #              → Manuscript ID
    "NI": Field.FUND_TXT.value,  #          → Grant Number
    "OT": Field.AUTHKW_RAW.value,  #        → Author Keywords
    "OTO": Field.OTHER_TERM.value,  #       → Other Terms
    "OWN": Field.OWN.value,  #              → Database Owner
    "PG": Field.PG_FIRST_LAST.value,  #     → Page Start–End
    "PHST": Field.PHST.value,  #            → Publication History
    "PL": Field.PUB_CTRY.value,  #          → Country of Publication
    "PMCID": Field.PMCID.value,  #          → PubMed Central ID
    "PMID": Field.PUBMED.value,  #          → PubMed ID
    "PT": Field.PUBTYPE.value,  #           → Document Type
    "PUBM": Field.PUBLISHER.value,  #       → Publisher
    "RF": Field.N_GCR.value,  #             → Reference Count
    "RIN": Field.RIN.value,  #              → Retraction In
    "RN": Field.CAS_REG_NO.value,  #        → Registry Number
    "SB": Field.SUBJ_SUBSET.value,  #       → Subject Subset
    "SI": Field.SUPPL_INF.value,  #         → Supplement Information
    "SO": Field.SRC_CITATION_INFO.value,  # → Source Title + Citation Info
    "STAT": Field.PUBSTAGE.value,  #        → Publication Status
    "TA": Field.SRC_ISO4.value,  #          → Source Title (abbreviated)
    "TI": Field.TITLE_RAW.value,  #         → Title
    "TT": Field.TRANSL_TITLE.value,  #      → Translated Title
    "VI": Field.VOL.value,  #               → Volume
}


SCOPUS_TO_TM2 = {
    #
    # A
    #
    "Abbreviated Source Title": Field.SRC_ISO4.value,
    "Abstract": Field.ABSTR_RAW.value,
    "Acronym": Field.ACRONYM.value,
    "Affiliations": Field.AFFIL.value,
    "Art. No.": Field.ART_NO.value,
    "Author full names": Field.AUTH_FULL_NAME.value,
    "Author Keywords": Field.AUTHKW_RAW.value,
    "Author(s) ID": Field.AUTHID.value,
    "Authors with affiliations": Field.AUTH_WITH_AFFIL.value,
    "Authors": Field.AUTH_RAW.value,
    #
    # C
    #
    "Chemicals/CAS": Field.CAS_REG_NO.value,
    "Cited by": Field.GCS.value,
    "CODEN": Field.CODEN.value,
    "Conference code": Field.CONF_CODE.value,
    "Conference date": Field.CONF_DATE.value,
    "Conference location": Field.CONF_LOC.value,
    "Conference name": Field.CONF_NAME.value,
    "Correspondence Address": Field.CORRESPOND_ADDR.value,
    #
    # D
    #
    "Document Type": Field.DOCTYPE.value,
    "DOI": Field.DOI.value,
    #
    # E
    #
    "Editors": Field.EDITOR.value,
    "EID": Field.EID.value,
    #
    # F
    #
    "Funding Details": Field.FUND_DET.value,
    "Funding Texts": Field.FUND_TXT.value,
    #
    # I
    #
    "Index Keywords": Field.IDXKW_RAW.value,
    "ISBN": Field.ISBN.value,
    "ISSN": Field.ISSN.value,
    "Issue": Field.ISSUE.value,
    #
    # L
    #
    "Language of Original Document": Field.LANG.value,
    "Link": Field.SCOPUS_LINK.value,
    #
    # M
    #
    "Manufacturers": Field.MANUFACTURER.value,
    "Molecular Sequence Numbers": Field.SEQ_NO.value,
    #
    # O
    #
    "Open Access": Field.OA.value,
    #
    # P
    #
    "Page count": Field.PG_COUNT.value,
    "Page end": Field.PG_LAST.value,
    "Page start": Field.PG_FIRST.value,
    "Publication Stage": Field.PUBSTAGE.value,
    "Publisher": Field.PUBLISHER.value,
    "PubMed ID": Field.PUBMED.value,
    #
    # R
    #
    "References": Field.GCR_FREE_TEXT.value,
    #
    # S
    #
    "Source title": Field.SRC.value,
    "Source": Field.DATABASE.value,
    "Sponsors": Field.FUND_SPONS.value,
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
    "Year": Field.YEAR.value,
}


WOS_TO_TM2 = {
    "AB": Field.ABSTR_RAW.value,
    "AF": Field.AUTH_FULL_NAME.value,
    "AU": Field.AUTH_RAW.value,
    "BE": Field.EDITOR.value,
    "BN": Field.ISBN.value,
    "BP": Field.PG_FIRST.value,
    "C1": Field.AFFIL.value,
    "CR": Field.GCR_WOS_FORMAT.value,
    "DE": Field.AUTHKW_RAW.value,
    "DI": Field.DOI.value,
    "DT": Field.DOCTYPE.value,
    "EI": Field.ISSNE.value,
    "EM": Field.EMAIL.value,
    "EP": Field.PG_LAST.value,
    "FU": Field.FUND_DET.value,
    "FX": Field.FUND_TXT.value,
    "ID": Field.IDXKW_RAW.value,
    "IS": Field.ISSUE.value,
    "J9": Field.SRC_J9.value,
    "JI": Field.SRC_ISO4.value,
    "LA": Field.LANG.value,
    "NR": Field.N_GCR.value,
    "OA": Field.OA.value,
    "OI": Field.ORCID.value,
    "PA": Field.PUBLISHER_ADDRESS.value,
    "PD": Field.DATE.value,
    "PG": Field.PG_COUNT.value,
    "PI": Field.PUBLISHER_CITY.value,
    "PT": Field.PUBTYPE.value,
    "PU": Field.PUBLISHER.value,
    "PY": Field.YEAR.value,
    "RI": Field.AUTHID.value,
    "RP": Field.CORRESPOND_ADDR.value,
    "SC": Field.WOS_SC.value,
    "SN": Field.ISSN.value,
    "SO": Field.SRC.value,
    "TC": Field.GCS.value,
    "TI": Field.TITLE_RAW.value,
    "U1": Field.WOS_U1.value,
    "U2": Field.WOS_U2.value,
    "UT": Field.EID.value,
    "VL": Field.VOL.value,
    "WC": Field.ASJC.value,
    "Z9": Field.WOS_Z9.value,
}


def s02_renam_col(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    mapping = {
        "OpenAlex": OPENALEX_TO_TM2,
        "PubMed": PUBMED_TO_TM2,
        "Scopus": SCOPUS_TO_TM2,
        "WoS": WOS_TO_TM2,
    }[marker]

    main_file = Path(root_directory) / "ingest" / "process" / "main.csv.zip"
    files_processed = renam_col(main_file, mapping)

    return files_processed
