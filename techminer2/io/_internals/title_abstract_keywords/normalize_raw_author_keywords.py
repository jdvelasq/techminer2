from techminer2.io._internals.operations import clean_raw_keywords


def normalize_raw_author_keywords(root_directory: str) -> int:

    return clean_raw_keywords(
        source="raw_author_keywords",
        target="raw_author_keywords",
        root_directory=root_directory,
    )
