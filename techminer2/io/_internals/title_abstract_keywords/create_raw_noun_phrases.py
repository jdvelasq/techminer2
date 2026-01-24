from techminer2.io._internals.operations import merge_columns


def create_raw_noun_phrases(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "raw_abstract_noun_phrases",
            "raw_document_title_noun_phrases",
        ],
        target="raw_noun_phrases",
        root_directory=root_directory,
    )
