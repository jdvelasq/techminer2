from techminer2.io._internals.operations.coalesce_column import coalesce_column


def normalize_source_title_abbr(root_directory: str) -> int:

    return coalesce_column(
        source="source_title_abbr",
        target="source_title",
        root_directory=root_directory,
    )
