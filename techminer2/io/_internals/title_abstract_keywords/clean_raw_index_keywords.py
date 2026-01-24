from .helpers import clean_raw_keyterms


def clean_raw_index_keywords(root_directory: str) -> int:

    return clean_raw_keyterms(
        source="raw_index_keywords",
        target="raw_index_keywords",
        root_directory=root_directory,
    )
