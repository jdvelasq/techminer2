from techminer2.io._internals.operations.coalesce_column import coalesce_column


def normalize_abbr_source_title(root_directory):

    return coalesce_column(
        source="abbr_source_title",
        target="source_title",
        root_directory=root_directory,
    )
