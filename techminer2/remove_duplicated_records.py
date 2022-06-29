# ----< Drop duplicates >------------------------------------------------------


def _drop_duplicates(documents):
    documents = documents.copy()
    if "doi" in documents.columns:
        duplicated_doi = (documents.doi.duplicated()) & (~documents.doi.isna())
        documents = documents[~duplicated_doi]

    if (
        "authors" in documents.columns
        and "document_title" in documents.columns
        and "year" in documents.columns
        and "source_name" in documents.columns
    ):
        subset = ("authors", "document_title", "year", "source_name")
        documents = documents.drop_duplicates(subset=subset)
    return documents
