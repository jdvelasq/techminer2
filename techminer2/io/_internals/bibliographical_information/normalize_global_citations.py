from techminer2.io._internals.operations import transform_column


def normalize_global_citations(root_directory: str) -> int:

    return transform_column(
        source="global_citations",
        target="global_citations",
        function=lambda w: w.fillna(0).astype(int),
        root_directory=root_directory,
    )
