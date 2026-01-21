from techminer2.io._internals.operators.fill_nulls import fill_nulls


def normalize_abbr_source_title(root_directory):

    return fill_nulls(
        source="abbr_source_title",
        target="source_title",
        root_directory=root_directory,
    )
