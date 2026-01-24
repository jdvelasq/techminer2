from techminer2.io._internals.operations import clean_raw_keywords


def normalize_raw_index_keywords(root_directory: str) -> int:

    return clean_raw_keywords(
        source="raw_index_keywords",
        target="raw_index_keywords",
        root_directory=root_directory,
    )
