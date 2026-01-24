from techminer2.io._internals.operations import merge_columns


def create_raw_descriptors(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "raw_keywords",
            "raw_noun_phrases",
        ],
        target="raw_descriptors",
        root_directory=root_directory,
    )
