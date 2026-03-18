from pathlib import Path


def get_datab_marker(root_directory: str) -> str:

    ingest_path = Path(root_directory) / "ingest" / "process"

    openalex = ingest_path / "_OPENALEX"
    if openalex.exists():
        return "OpenAlex"

    pubmed = ingest_path / "_PUBMED"
    if pubmed.exists():
        return "PubMed"

    scopus = ingest_path / "_SCOPUS"
    if scopus.exists():
        return "Scopus"

    wos = ingest_path / "_WOS"
    if wos.exists():
        return "WoS"

    raise ValueError("No marker file found in the ingest process directory.")
