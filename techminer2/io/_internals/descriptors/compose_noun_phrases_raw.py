from techminer2.io._internals.operations import merge_columns


def compose_noun_phrases_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "abstract_noun_phrases_raw",
            "document_title_noun_phrases_raw",
        ],
        target="raw_noun_phrases",
        root_directory=root_directory,
    )
