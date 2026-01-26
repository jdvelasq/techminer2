from techminer2.io._internals.operations import transform_column


def normalize_global_citation_count(root_directory: str) -> int:

    return transform_column(
        source="global_citation_count",
        target="global_citation_count",
        function=lambda w: w.fillna(0).astype(int),
        root_directory=root_directory,
    )
