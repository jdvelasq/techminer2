from techminer2.io._internals.operations import extract_uppercase


def normalize_raw_abstract_nouns_and_phrases(root_directory: str) -> int:

    return extract_uppercase(
        source="abstract",
        target="raw_abstract_nouns_and_phrases",
        root_directory=root_directory,
    )
