from techminer2.io._internals.operations import merge_columns


def compose_descriptors_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "keywords_raw",
            "noun_phrases_raw",
        ],
        target="descriptors_raw",
        root_directory=root_directory,
    )
